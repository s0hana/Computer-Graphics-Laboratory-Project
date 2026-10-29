import cv2
import numpy as np

V = [
    [0, 1, 1, 0, 0, 0, 1, 1], 
    [0, 0, 1, 1, 1, 0, 0, 1], 
    [0, 0, 0, 0, 1, 1, 1, 1],  
    [1, 1, 1, 1, 1, 1, 1, 1]   
]
vertex_names = ["A", "B", "C", "D", "E", "F", "G", "H"]

perspective_cases = [
    {
        "name": "1_vanishing_point",
        "window_title": "Cube Projection - 1 Vanishing Point",
        "R0": [0.0, 0.0, 0.0],
        "N":  [0.0, 0.0, 1.0],       
        "C":  [-1.2, 2.2, -2.5]
    },
    {
        "name": "2_vanishing_point",
        "window_title": "Cube Projection - 2 Vanishing Points (Reference Match)",
        "R0": [0.0, 0.0, 0.0],
        "N":  [1.0, 0.0, 1.0],       
        "C":  [-2.0, 3.0, -2.0]
    },
    {
        "name": "3_vanishing_point",
        "window_title": "Cube Projection - 3 Vanishing Points",
        "R0": [0.0, 0.0, 0.0],
        "N":  [1.0, -0.35, 1.0],    
        "C":  [-2.0, 3.0, -2.0]
    }
]

faces = [
    {"indices": [0, 1, 2, 3], "normal": [ 0,  0, -1], "p0": [0, 0, 0]}, 
    {"indices": [5, 6, 7, 4], "normal": [ 0,  0,  1], "p0": [0, 0, 1]}, 
    {"indices": [0, 3, 4, 5], "normal": [-1,  0,  0], "p0": [0, 0, 0]},
    {"indices": [1, 6, 7, 2], "normal": [ 1,  0,  0], "p0": [1, 0, 0]}, 
    {"indices": [3, 2, 7, 4], "normal": [ 0,  1,  0], "p0": [0, 1, 0]}, 
    {"indices": [0, 5, 6, 1], "normal": [ 0, -1,  0], "p0": [0, 0, 0]}  
]

WIN_W, WIN_H = 500, 520
MARGIN = 85

window_positions = {
    "1_vanishing_point": (20, 60),
    "3_vanishing_point": (535, 60),
    "2_vanishing_point": (1050, 60)
}

for case in perspective_cases:
    x0, y0, z0 = case["R0"]
    n1, n2, n3 = case["N"]
    a, b, c    = case["C"]

    d0 = n1 * x0 + n2 * y0 + n3 * z0
    d1 = n1 * a  + n2 * b  + n3 * c
    d  = d0 - d1

    M = [
        [d + a * n1,     a * n2,     a * n3, -a * d0],
        [    b * n1, d + b * n2,     b * n3, -b * d0],
        [    c * n1,     c * n2, d + c * n3, -c * d0],
        [        n1,         n2,         n3,     -d1]
    ]

    V_prime = [[0.0] * 8 for _ in range(4)]
    for row in range(4):
        for col in range(8):
            for k in range(4):
                V_prime[row][col] += M[row][k] * V[k][col]

    proj_3d = []
    print(f"\n{case['window_title']}")
    for i in range(8):
        W = V_prime[3][i]
        x_p = V_prime[0][i] / W
        y_p = V_prime[1][i] / W
        z_p = V_prime[2][i] / W
        proj_3d.append((x_p, y_p, z_p))
        print(f"  {vertex_names[i]}' = ({x_p:.3f}, {y_p:.3f}, {z_p:.3f})")

    vps = {}
    if n1 != 0:
        vps['VP1 (x-axis)'] = (round(a + d / n1, 3), round(b, 3), round(c, 3))
    if n2 != 0:
        vps['VP2 (y-axis)'] = (round(a, 3), round(b + d / n2, 3), round(c, 3))
    if n3 != 0:
        vps['VP3 (z-axis)'] = (round(a, 3), round(b, 3), round(c + d / n3, 3))
    print(f"Vanishing Points: {vps}")

    xs = [p[0] for p in proj_3d]
    ys = [p[1] for p in proj_3d]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)

    span_x = max_x - min_x if max_x != min_x else 1.0
    span_y = max_y - min_y if max_y != min_y else 1.0
    scale = min((WIN_W - 2 * MARGIN) / span_x, (WIN_H - 2 * MARGIN) / span_y)

    cx = (min_x + max_x) / 2.0
    cy = (min_y + max_y) / 2.0

    pts_2d = []
    for x_p, y_p, _ in proj_3d:
        px = int(WIN_W / 2.0 + (x_p - cx) * scale)
        py = int(WIN_H / 2.0 - (y_p - cy) * scale)
        pts_2d.append((px, py))

    img = np.ones((WIN_H, WIN_W, 3), dtype=np.uint8) * 255

    for face in faces:
        nx, ny, nz = face["normal"]
        px0, py0, pz0 = face["p0"]

        vx = a - px0
        vy = b - py0
        vz = c - pz0

        if (nx * vx + ny * vy + nz * vz) > 0:
            idx = face["indices"]
            for k in range(4):
                p1 = pts_2d[idx[k]]
                p2 = pts_2d[idx[(k + 1) % 4]]
                cv2.line(img, p1, p2, (0, 0, 0), 1, cv2.LINE_AA)

    cv2.imshow(case["window_title"], img)
    if case["name"] in window_positions:
        wx, wy = window_positions[case["name"]]
        cv2.moveWindow(case["window_title"], wx, wy)

    cv2.imwrite(f"{case['name']}.png", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
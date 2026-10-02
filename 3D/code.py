import math

def multiply_matrices(m1, m2):
    result = [[0.0] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            for k in range(4):
                result[i][j] += m1[i][k] * m2[k][j]
    return result

def multiply_matrix_vector(m, v):
    result = [0.0] * 4
    for i in range(4):
        for k in range(4):
            result[i] += m[i][k] * v[k]
    return result

def get_translation_matrix(tx, ty, tz):
    return [
        [1.0, 0.0, 0.0, tx],
        [0.0, 1.0, 0.0, ty],
        [0.0, 0.0, 1.0, tz],
        [0.0, 0.0, 0.0, 1.0]
    ]

def get_alignment_matrix(a, b, c):
    length_v = math.sqrt(a**2 + b**2 + c**2)
    lambd = math.sqrt(b**2 + c**2)
    if lambd == 0:
        val = a / abs(a) if a != 0 else 1.0
        return [
            [0.0, 0.0, -val, 0.0],
            [0.0, 1.0, 0.0,  0.0],
            [val, 0.0, 0.0,  0.0],
            [0.0, 0.0, 0.0,  1.0]
        ]

    return [
        [lambd / length_v, (-a * b) / (lambd * length_v), (-a * c) / (lambd * length_v), 0.0],
        [0.0,              c / lambd,                     -b / lambd,                    0.0],
        [a / length_v,     b / length_v,                  c / length_v,                  0.0],
        [0.0,              0.0,                           0.0,                           1.0]
    ]

def transpose_matrix(m):
    return [[m[j][i] for j in range(4)] for i in range(4)]

def get_z_rotation_matrix(angle_degrees):
    theta = math.radians(angle_degrees)
    cos_t = math.cos(theta)
    sin_t = math.sin(theta)
    return [
        [cos_t, -sin_t, 0.0, 0.0],
        [sin_t,  cos_t, 0.0, 0.0],
        [0.0,    0.0,   1.0, 0.0],
        [0.0,    0.0,   0.0, 1.0]
    ]

def solve_problem_6_3():
    px = float(input("Enter location point P (x-coordinate): "))
    py = float(input("Enter location point P (y-coordinate): "))
    pz = float(input("Enter location point P (z-coordinate): "))

    a = float(input("Enter direction vector V (x-component): "))
    b = float(input("Enter direction vector V (y-component): "))
    c = float(input("Enter direction vector V (z-component): "))
    x = float(input("Enter point to rotate (x-coordinate): "))
    y = float(input("Enter point to rotate (y-coordinate): "))
    z = float(input("Enter point to rotate (z-coordinate): "))
    angle = float(input("Enter rotation angle in degrees: "))

    T_minus_P = get_translation_matrix(-px, -py, -pz)
    A_V = get_alignment_matrix(a, b, c)
    R_K = get_z_rotation_matrix(angle)
    A_V_inv = transpose_matrix(A_V)
    T_P = get_translation_matrix(px, py, pz)

    M1 = multiply_matrices(A_V, T_minus_P)
    M2 = multiply_matrices(R_K, M1)
    M3 = multiply_matrices(A_V_inv, M2)
    transformation_matrix = multiply_matrices(T_P, M3)

    print()
    print("Transformation Matrix (R_theta, L): ")
    for row in transformation_matrix:
        print(f"[{row[0]:8.4f}, {row[1]:8.4f}, {row[2]:8.4f}, {row[3]:8.4f}]")

    print()
    point_vector = [x, y, z, 1.0]
    rotated_vector = multiply_matrix_vector(transformation_matrix, point_vector)
    print(f"Final Coordinate Value: {rotated_vector[0]:.4f}, {rotated_vector[1]:.4f}, {rotated_vector[2]:.4f}")
    print()
if __name__ == "__main__":
    solve_problem_6_3()
import cv2
import random
import time

def draw_pixel(image, x, y, color):
    height, width = image.shape[:2]
    pixel_x = x
    pixel_y = height - 1 - y
    if 0 <= pixel_x < width and 0 <= pixel_y < height:
        image[pixel_y, pixel_x] = color

def draw_midpoint_ellipse(image, xc, yc, rx, ry):
    x = 0
    y = ry
    total = 0
    t0 = time.perf_counter_ns()
    d1 = (ry ** 2) - (rx ** 2 * ry) + (0.25 * rx ** 2)
    dx = 2 * (ry ** 2) * x
    dy = 2 * (rx ** 2) * y
    t1 = time.perf_counter_ns()
    total += (t1 - t0)
    while dx < dy:
        points = [
            (xc + x, yc + y), (xc - x, yc + y),
            (xc + x, yc - y), (xc - x, yc - y)
    ]
        
        t0 = time.perf_counter_ns()
        if d1 < 0:
            x += 1
            dx = dx + (2 * ry ** 2)
            d1 = d1 + dx + (ry ** 2)
        else:
            x += 1
            y -= 1
            dx = dx + (2 * ry ** 2)
            dy = dy - (2 * rx ** 2)
            d1 = d1 + dx - dy + (ry ** 2)
        t1 = time.perf_counter_ns()
        total += (t1 - t0)

        for px, py in points:
            draw_pixel(image, px, py, (255, 0, 0))

    t0 = time.perf_counter_ns()
    d2 = ((ry ** 2) * ((x + 0.5) ** 2)) + ((rx ** 2) * ((y - 1) ** 2)) - ((rx ** 2) * (ry ** 2))
    t1 = time.perf_counter_ns()
    total += (t1 - t0)

    while y >= 0:
        points = [
            (xc + x, yc + y), (xc - x, yc + y),
            (xc + x, yc - y), (xc - x, yc - y)
        ]

        t0 = time.perf_counter_ns()
        if d2 > 0:
            y -= 1
            dy = dy - (2 * rx ** 2)
            d2 = d2 + (rx ** 2) - dy
        else:
            x += 1
            y -= 1
            dx = dx + (2 * ry ** 2)
            dy = dy - (2 * rx ** 2)
            d2 = d2 + dx - dy + (rx ** 2)
        t1 = time.perf_counter_ns()
        total += (t1 - t0)

        for px, py in points:
            draw_pixel(image, px, py, (255, 0, 0))

    return total

img_path = r"D:\4_1\4.1 Term\Computer Graphics\Lab\e98e07fd-9a72-4c80-8788-f7c831ef54b8.jpeg"
img = cv2.imread(img_path)
height, width = img.shape[:2]

n = int(input("Enter number of ellipses: "))
ellipse_params = []
for i in range(n):
    rx = random.randint(20, 150)
    ry = random.randint(20, 150)
    xc = random.randint(rx, width - rx - 1)
    yc = random.randint(ry, height - ry - 1)
    ellipse_params.append([rx, ry, xc, yc])

total_midpoint = 0
for param in ellipse_params:
    rx, ry, xc, yc = param
    total_midpoint += draw_midpoint_ellipse(img, xc, yc, rx, ry)

total_midpoint_seconds = total_midpoint / 1000000000.0

print(f"Time required for Midpoint Ellipse Algorithm: {total_midpoint_seconds:.6f} seconds")

cv2.imshow("Multiple Ellipses", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

output_path = r"D:\4_1\4.1 Term\Computer Graphics\Lab\ouput\e98e07fd-9a72-4c80-8788-f7c831ef54b8.jpeg"
cv2.imwrite(output_path, img)
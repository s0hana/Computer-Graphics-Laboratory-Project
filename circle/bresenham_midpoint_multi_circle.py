import cv2
import random
import time

def draw_pixel(image, x, y, color):
    height, width = image.shape[:2]
    pixel_x = x
    pixel_y = height - 1 - y
    if 0 <= pixel_x < width and 0 <= pixel_y < height:
        image[pixel_y, pixel_x] = color

def draw_bresenham_circle(image, xc, yc, r):
    x = 0
    y = r
    d = 3 - (r << 1)
    total = 0
    while x <= y:
        t0 = time.perf_counter_ns()
        points = [(xc + x, yc + y), (xc + y, yc + x), (xc - x, yc + y), (xc - y, yc + x), (xc - x, yc - y), (xc - y, yc - x), (xc + x, yc - y), (xc + y, yc - x)]
        if d < 0:
            d = d + (x << 2) + 6
        else:
            d = d + ((x - y) << 2) + 10
            y = y - 1
        x = x + 1
        t1 = time.perf_counter_ns()
        total = total + (t1 - t0)
        for px, py in points:
            draw_pixel(image, px, py, (0, 255, 0))
    return total

def draw_midpoint_circle(image, xc, yc, r):
    x = 0
    y = r
    p = 1 - r
    total = 0
    while x <= y:
        t0 = time.perf_counter_ns()
        points = [(xc + x, yc + y), (xc + y, yc + x), (xc - x, yc + y), (xc - y, yc + x), (xc - x, yc - y), (xc - y, yc - x), (xc + x, yc - y), (xc + y, yc - x)]
        if p < 0:
            p = p + (x << 1) + 3
        else:
            p = p + ((x - y) << 1) + 5
            y = y - 1
        x = x + 1
        t1 = time.perf_counter_ns()
        total = total + (t1 - t0)
        for px, py in points:
            draw_pixel(image, px, py, (255, 0, 0))
    return total

img_path = r"D:\4_1\4.1 Term\Computer Graphics\Lab\e98e07fd-9a72-4c80-8788-f7c831ef54b8.jpeg"
img = cv2.imread(img_path)
height, width = img.shape[:2]
#print(height, width)
n = int(input("Enter number of circles: "))
radius_center = []
for i in range(n):
    r = random.randint(30, 200)
    xc = random.randint(r, width - r - 1)
    yc = random.randint(r, height - r - 1)
    radius_center.append([r, xc, yc])

total_bresenham = 0
for i in radius_center:
    r, xc, yc = i
    total_bresenham = total_bresenham + draw_bresenham_circle(img, xc, yc, r)

total_bresenham_seconds = total_bresenham / 1000000000.0

total_midpoint = 0
for i in radius_center:
    r, xc, yc = i
    total_midpoint = total_midpoint + draw_midpoint_circle(img, xc, yc, r)
total_midpoint_seconds = total_midpoint / 1000000000.0

print(f"Time required for Bresemham Algorithm: {total_bresenham_seconds:.6f} seconds.")
print(f"Time required for Midpoint Algorithm: {total_midpoint_seconds:.6f} seconds")
cv2.imshow("Multiple Circles", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
output_path = r"D:\4_1\4.1 Term\Computer Graphics\Lab\circle_output.jpg"
cv2.imwrite(output_path, img)
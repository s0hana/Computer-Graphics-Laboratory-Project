import cv2
import time

img = cv2.imread(r"D:\4_1\4.1 Term\Computer Graphics\Lab\e98e07fd-9a72-4c80-8788-f7c831ef54b8.jpeg")
height, width = img.shape[:2]
original_x1 = int(input("Enter x1: "))
original_y1 = int(input("Enter y1: "))
original_x2 = int(input("Enter x2: "))
original_y2 = int(input("Enter y2: "))


start_time_bresenham = time.perf_counter()
x1 = original_x1
y1 = height - 1 - original_y1
x2 = original_x2
y2 = height - 1 - original_y2

dx = x2 - x1
dy = y2 - y1
if dx >= 0:
    step_x = 1
else:
    step_x = -1
if dy >= 0:
    step_y = 1
else:
    step_y = -1
dx = abs(dx)
dy = abs(dy)
x = x1
y = y1
if dx >= dy:
    d = (2*dy) - dx
    while x != x2:
        if 0 <= x < width and 0 <= y < height:
            img[y, x] = (0, 0, 255)
        if d < 0:
            d = d + (2*dy)
        else:
            y = y + step_y
            d = d + (2*(dy - dx))
        x = x + step_x
    if 0 <= x < width and 0 <= y < height:
        img[y, x] = (0, 0, 255)
else:
    d = (2*dx) - dy
    while y != y2:
        if 0 <= x < width and 0 <= y < height:
            img[y, x] = (0, 0, 255)
        if d < 0:
            d = d + (2*dx)
        else:
            x = x + step_x
            d = d + (2*(dx - dy))
        y = y + step_y
    if 0 <= x < width and 0 <= y < height:
        img[y, x] = (0, 0, 255)
end_time_bresenham = time.perf_counter()


print("Execution Time for Bresenham =",end_time_bresenham - start_time_bresenham,"seconds")
img = cv2.resize(img, (1200, 600))
cv2.imwrite("outputBresenham.jpeg", img)
cv2.imshow("Bresenham Line", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
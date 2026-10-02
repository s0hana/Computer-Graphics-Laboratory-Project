import cv2
import time
import random

original_img = cv2.imread(r"D:\4_1\4.1 Term\Computer Graphics\Lab\e98e07fd-9a72-4c80-8788-f7c831ef54b8.jpeg")

n = int(input("Enter number of lines: "))

height, width = original_img.shape[:2]

lines = []

for line_no in range(1, n + 1):
    original_x1 = random.randint(0, width - 1)
    original_y1 = random.randint(0, height - 1)
    original_x2 = random.randint(0, width - 1)
    original_y2 = random.randint(0, height - 1)
    lines.append((original_x1, original_y1, original_x2, original_y2))

#dda red
dda_start_time = time.perf_counter()
for original_x1, original_y1, original_x2, original_y2 in lines:
    x1 = original_x1
    y1 = height - 1 - original_y1
    x2 = original_x2
    y2 = height - 1 - original_y2
    dx = x2 - x1
    dy = y2 - y1
    if dx == 0:
        x = x1
        y = y1
        if y1 <= y2:
            while y <= y2:
                if 0 <= x < width and 0 <= y < height:
                    original_img[y, x] = (255, 0, 0)
                y = y + 1
        else:
            while y >= y2:
                if 0 <= x < width and 0 <= y < height:
                    original_img[y, x] = (255, 0, 0)
                y = y - 1
    else:
        m = dy / dx
        if abs(m) < 1:
            x = x1
            y = y1
            if x1 <= x2:
                while x <= x2:
                    xi = round(x)
                    yi = round(y)
                    if 0 <= xi < width and 0 <= yi < height:
                        original_img[yi, xi] = (255, 0, 0)
                    x = x + 1
                    y = y + m
            else:
                while x >= x2:
                    xi = round(x)
                    yi = round(y)
                    if 0 <= xi < width and 0 <= yi < height:
                        original_img[yi, xi] = (255, 0, 0)
                    x = x - 1
                    y = y - m
        else:
            x = x1
            y = y1
            if y1 <= y2:
                while y <= y2:
                    xi = round(x)
                    yi = round(y)
                    if 0 <= xi < width and 0 <= yi < height:
                        original_img[yi, xi] = (255, 0, 0)
                    y = y + 1
                    x = x + (1 / m)
            else:
                while y >= y2:
                    xi = round(x)
                    yi = round(y)
                    if 0 <= xi < width and 0 <= yi < height:
                        original_img[yi, xi] = (255, 0, 0)
                    y = y - 1
                    x = x - (1 / m)
dda_end_time = time.perf_counter()
dda_execution_time = dda_end_time - dda_start_time

#normal green
normal_start_time = time.perf_counter()
for original_x1, original_y1, original_x2, original_y2 in lines:
    x1 = original_x1
    y1 = height - 1 - original_y1
    x2 = original_x2
    y2 = height - 1 - original_y2
    m = 0
    c = 0
    if x2 != x1:
        m = (y2 - y1) / (x2 - x1)
        c = y1 - m*x1
        x = x1
        if x1 < x2:
            while x <= x2:
                y = m*x + c
                xi = round(x)
                yi = round(y)
                if 0 <= xi < width and 0 <= yi < height:
                    original_img[yi, xi] = (0, 255, 0)
                x = x + 0.4
        elif x1 > x2:
            while x >= x2:
                y = m*x + c
                xi = round(x)
                yi = round(y)
                if 0 <= xi < width and 0 <= yi < height:
                    original_img[yi, xi] = (0, 255, 0)
                x = x - 0.4
    else:
        y = min(y1, y2)
        while y <= max(y1, y2):
            xi = round(x1)
            yi = round(y)
            if 0 <= xi < width and 0 <= yi < height:
                original_img[yi, xi] = (0, 255, 0)
            y = y + 0.4
normal_end_time = time.perf_counter()
normal_execution_time = normal_end_time - normal_start_time

#bresenham blue
bresenham_start_time = time.perf_counter()
for original_x1, original_y1, original_x2, original_y2 in lines:
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
                original_img[y, x] = (0, 0, 255)
            if d < 0:
                d = d + (2*dy)
            else:
                y = y + step_y
                d = d + (2*(dy - dx))
            x = x + step_x
        if 0 <= x < width and 0 <= y < height:
            original_img[y, x] = (0, 0, 255)
    else:
        d = (2*dx) - dy
        while y != y2:
            if 0 <= x < width and 0 <= y < height:
                original_img[y, x] = (0, 0, 255)
            if d < 0:
                d = d + (2*dx)
            else:
                x = x + step_x
                d = d + (2*(dx - dy))
            y = y + step_y
        if 0 <= x < width and 0 <= y < height:
            original_img[y, x] = (0, 0, 255)
bresenham_end_time = time.perf_counter()
bresenham_execution_time = (bresenham_end_time - bresenham_start_time)

#dda int m purple
start_time_dda_int_m = time.perf_counter()
for original_x1, original_y1, original_x2, original_y2 in lines:
    x1 = original_x1
    y1 = height - 1 - original_y1
    x2 = original_x2
    y2 = height - 1 - original_y2
    dx = x2 - x1
    dy = y2 - y1
    if dx == 0:
        x = x1
        y = y1
        if y1 <= y2:
            while y <= y2:
                if 0 <= x < width and 0 <= y < height:
                    original_img[y, x] = (255, 105, 180)
                y = y + 1
        else:
            while y >= y2:
                if 0 <= x < width and 0 <= y < height:
                    original_img[y, x] = (255, 105, 180)
                y = y - 1
    else:
        m = dy / dx
        m = round(m)
        if m == 0:
            x = x1
            y = y1
            if x1 <= x2:
                while x <= x2:
                    if 0 <= x < width and 0 <= y < height:
                        original_img[y, x] = (255, 105, 180)
                    x = x + 1
            else:
                while x >= x2:
                    if 0 <= x < width and 0 <= y < height:
                        original_img[y, x] = (255, 105, 180)
                    x = x - 1
        elif abs(m) < 1:
            x = x1
            y = y1
            if x1 <= x2:
                while x <= x2:
                    if 0 <= x < width and 0 <= y < height:
                        original_img[y, x] = (255, 105, 180)
                    x = x + 1
                    y = y + m
            else:
                while x >= x2:
                    if 0 <= x < width and 0 <= y < height:
                        original_img[y, x] = (255, 105, 180)
                    x = x - 1
                    y = y - m
        else:
            x = x1
            y = y1
            if y1 <= y2:
                while y <= y2:
                    xi = round(x)
                    yi = round(y)
                    if 0 <= xi < width and 0 <= yi < height:
                        original_img[yi, xi] = (255, 105, 180)
                    y = y + 1
                    x = x + (1 / m)
            else:
                while y >= y2:
                    xi = round(x)
                    yi = round(y)
                    if 0 <= xi < width and 0 <= yi < height:
                        original_img[yi, xi] = (255, 105, 180)
                    y = y - 1
                    x = x - (1 / m)
end_time_dda_int_m = time.perf_counter()
rounded_m_execution_time = (end_time_dda_int_m - start_time_dda_int_m)

print("Normal Equation Execution Time =",normal_execution_time,"seconds")
print("DDA Execution Time =",dda_execution_time,"seconds")
print("Rounded m Execution Time =",rounded_m_execution_time,"seconds")
print("Bresenham Execution Time =",bresenham_execution_time,"seconds")

h, w = original_img.shape[:2]
#print("Combined Image Height:", h)
#print("Combined Image Width:", w)

cv2.imwrite("Combined_img.jpeg",original_img)
cv2.imshow("DDA vs Normal Equation vs Bresenham vs Rounded m",original_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
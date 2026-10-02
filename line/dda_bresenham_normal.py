import cv2
import time

img = cv2.imread(r"D:\4_1\4.1 Term\Computer Graphics\Lab\e98e07fd-9a72-4c80-8788-f7c831ef54b8.jpeg")
height, width = img.shape[:2]

#print(f"Height: {height}, Width: {width}")

original_x1 = int(input("Enter x1: "))
original_y1 = int(input("Enter y1: "))
original_x2 = int(input("Enter x2: "))
original_y2 = int(input("Enter y2: "))


#dda green
start_time_dda = time.perf_counter()
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
                img[y, x] = (0, 255, 0)
            y = y + 1
    else:
        while y >= y2:
            if 0 <= x < width and 0 <= y < height:
                img[y, x] = (0, 255, 0)
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
                    img[yi, xi] = (0, 255, 0)
                x = x + 1
                y = y + m
        else:
            while x >= x2:
                xi = round(x)
                yi = round(y)
                if 0 <= xi < width and 0 <= yi < height:
                    img[yi, xi] = (0, 255, 0)
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
                    img[yi, xi] = (0, 255, 0)
                y = y + 1
                x = x + (1 / m)
        else:
            while y >= y2:
                xi = round(x)
                yi = round(y)
                if 0 <= xi < width and 0 <= yi < height:
                    img[yi, xi] = (0, 255, 0)
                y = y - 1
                x = x - (1 / m)

end_time_dda = time.perf_counter()


#rounded m red
start_time_dda_int_m = time.perf_counter()
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
                img[y, x] = (0, 255, 0)
            y = y + 1
    else:
        while y >= y2:
            if 0 <= x < width and 0 <= y < height:
                img[y, x] = (0, 255, 0)
            y = y - 1
else:
    m = dy / dx
    m = round(m)
    if m == 0:
        x = x1
        if x1 <= x2:
            while x <= x2:
                if 0 <= x < width and 0 <= y < height:
                    img[y, x] = (0, 255, 0)
                x = x + 1
        else:
            while x >= x2:
                if 0 <= x < width and 0 <= y < height:
                    img[y, x] = (0, 255, 0)
                x = x - 1
    elif abs(m) < 1:
        x = x1
        y = y1
        if x1 <= x2:
            while x <= x2:
                if 0 <= x < width and 0 <= y < height:
                    img[y, x] = (0, 255, 0)
                x = x + 1
                y = y + m
        else:
            while x >= x2:
                if 0 <= x < width and 0 <= y < height:
                    img[y, x] = (0, 255, 0)
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
                    img[yi, xi] = (0, 0, 255)
                y = y + 1
                x = x + (1 / m)
        else:
            while y >= y2:
                xi = round(x)
                yi = round(y)
                if 0 <= xi < width and 0 <= yi < height:
                    img[yi, xi] = (0, 0, 255)
                y = y - 1
                x = x - (1 / m)

end_time_dda_int_m = time.perf_counter()


#normal equation blue
start_time_normal = time.perf_counter()
x1 = original_x1
y1 = height - 1 - original_y1
x2 = original_x2
y2 = height - 1 - original_y2
m = 0
c = 0
if x2 != x1:
    m = (y2 - y1) / (x2 - x1)
    c = y1 - m * x1
    x = x1
    if x1 <= x2:
        while x <= x2:
            y = m * x + c
            xi = round(x)
            yi = round(y)
            if 0 <= xi < width and 0 <= yi < height:
                img[yi, xi] = (255, 0, 0)
            x = x + 1.5
    else:
        while x >= x2:
            y = m * x + c
            xi = round(x)
            yi = round(y)
            if 0 <= xi < width and 0 <= yi < height:
                img[yi, xi] = (255, 0, 0)
            x = x - 1.5
else:
    y = y1
    if y1 <= y2:
        while y <= y2:
            xi = round(x1)
            yi = round(y)
            if 0 <= xi < width and 0 <= yi < height:
                img[yi, xi] = (255, 0, 0)
            y = y + 1.5
    else:
        while y >= y2:
            xi = round(x1)
            yi = round(y)
            if 0 <= xi < width and 0 <= yi < height:
                img[yi, xi] = (255, 0, 0)
            y = y - 1.5

end_time_normal = time.perf_counter()


#bresenham yellow
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
            img[y, x] = (0, 255, 255)
        if d < 0:
            d = d + (2*dy)
        else:
            y = y + step_y
            d = d + (2*(dy - dx))
        x = x + step_x
    if 0 <= x < width and 0 <= y < height:
        img[y, x] = (0, 255, 255)
else:
    d = (2*dx) - dy
    while y != y2:
        if 0 <= x < width and 0 <= y < height:
            img[y, x] = (0, 255, 255)
        if d < 0:
            d = d + (2*dx)
        else:
            x = x + step_x
            d = d + (2*(dx - dy))
        y = y + step_y
    if 0 <= x < width and 0 <= y < height:
        img[y, x] = (0, 255, 255)

end_time_bresenham = time.perf_counter()


print("Execution Time for DDA =",end_time_dda - start_time_dda,"seconds")
print("Execution Time for DDA round m =",end_time_dda_int_m - start_time_dda_int_m,"seconds")
print("Execution Time for normal method =",end_time_normal - start_time_normal,"seconds")
print("Execution Time for Bresenham =",end_time_bresenham - start_time_bresenham,"seconds")


img = cv2.resize(img, (1200, 600))
cv2.imwrite("output.jpeg", img)
cv2.imshow("Lab 1", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
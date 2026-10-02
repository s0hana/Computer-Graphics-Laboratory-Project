import cv2

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
    while x <= y:
        points = [(xc + x, yc + y), (xc + y, yc + x), (xc - x, yc + y), (xc - y, yc + x), (xc - x, yc - y), (xc - y, yc - x), (xc + x, yc - y), (xc + y, yc - x)]
        for px, py in points:
                draw_pixel(image, px, py, (0, 255, 0))
        if d < 0:
            d = d + (x << 2) + 6
        else:
            d = d + ((x - y) << 2) + 10
            y = y - 1
        x = x + 1


def draw_midpoint_circle(image, xc, yc, r):
    x = 0
    y = r
    p = 1 - r
    while x <= y:
        points = [(xc + x, yc + y), (xc + y, yc + x), (xc - x, yc + y), (xc - y, yc + x), (xc - x, yc - y), (xc - y, yc - x), (xc + x, yc - y), (xc + y, yc - x)]
        for px, py in points:
            draw_pixel(image, px, py, (255, 0, 0))
        if p < 0:
            p = p + (x << 1) + 3
        else:
            p = p + ((x - y)<<1) + 5
            y = y - 1
        x = x + 1


img_path = r"D:\4_1\4.1 Term\Computer Graphics\Lab\e98e07fd-9a72-4c80-8788-f7c831ef54b8.jpeg"
img = cv2.imread(img_path)

height, width = img.shape[:2]
xc = width // 2
yc = height // 2
r = 100
draw_bresenham_circle(img, xc, yc, r)
draw_midpoint_circle(img, xc, yc, r)
#img = cv2.resize(img, (700, 700))
cv2.imshow("Circle", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
output_path = r"D:\4_1\4.1 Term\Computer Graphics\Lab\circle_output_1.jpg"
cv2.imwrite(output_path, img)


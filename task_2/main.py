import numpy as np
import cv2 as cv


def draw_cat(path):
    img = cv.imread(path, cv.IMREAD_COLOR)
    assert img is not None, "Path error"
    cv.circle(img, (126, 170), 25, (255, 0, 0), 3)
    cv.circle(img, (213, 170), 25, (255, 0, 255), 3)
    cv.line(img, (150, 210), (166, 235), (12, 6, 202), 7)
    cv.line(img, (170, 235), (192, 210), (24, 6, 202), 7)
    nose = np.array([[150, 210], [155, 209], [160, 208], [165, 207], [170, 206], [175, 207], [180, 208], [185, 209]], np.int32)
    nose = nose.reshape((-1, 1, 2))
    cv.polylines(img, [nose], True, (12, 6, 202), 4)
    left_ear = np.array([[50, 120], [46, 90], [42, 80], [38, 50], [42, 40], [46, 30], [50, 25],
                         [60, 35], [70, 45], [80, 55], [100, 65], [110, 85], [50, 120]], np.int32)
    left_ear = left_ear.reshape((-1, 1, 2))
    cv.polylines(img, [left_ear], False, (12, 6, 202), 6)
    right_ear = np.array([[250, 120], [220, 70], [240, 50], [250, 40], [280, 30],
                          [290, 60], [291, 97], [250, 120]], np.int32)
    right_ear = right_ear.reshape((-1, 1, 2))
    cv.polylines(img, [right_ear], False, (12, 6, 202), 6)
    cv.imshow(path, img)
    cv.imwrite("saved_image.jpg", img)
    cv.waitKey()


if __name__ == '__main__':
    draw_cat("cat.jpg")

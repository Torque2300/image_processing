import cv2
from matplotlib import pyplot as plt


def adaptive_transformation(path, type):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    assert img is not None, "Error while opening the image"
    if type == 'gaussian':
        adaptive_threshold = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                                                cv2.THRESH_BINARY, 9, 3)
    if type == 'mean':
        adaptive_threshold = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 3)
    plt.imshow(adaptive_threshold, 'gray')
    plt.show()


if __name__ == '__main__':
    print("print gaussian or mean for the adaptive threshold")
    adaptive_transformation('book_page.jpg', 'gaussian')

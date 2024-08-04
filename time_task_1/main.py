import cv2 as cv
import numpy as np


def create_noisy_image(path, noise_level):
    img = cv.imread(path, cv.IMREAD_GRAYSCALE)
    assert img is not None, "Path is incorrect"
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            noise = np.random.normal(0, noise_level)
            if noise + img[i][j] > 255:
                img[i][j] = 255
            elif noise + img[i][j] < 0:
                img[i][j] = 0
            else:
                img[i][j] = noise + img[i, j]
    return img


def create_noisy_images(path, n, noise_range):
    array = []
    for i in range(n):
        noise = np.random.randint(0, noise_range)
        array.append(create_noisy_image(path, noise))
    return np.array(array)


def filtrate_noisy_images(images: np.array):
    filtrated_image = np.zeros_like(images[0])
    for i in range(images.shape[1]):
        for j in range(images.shape[2]):
            mean_value = 0
            for k in range(images.shape[0]):
                mean_value += images[k][i][j]
            filtrated_image[i][j] = mean_value / images.shape[0]
            if filtrated_image[i][j] > 255:
                filtrated_image[i][j] = 255
            if filtrated_image[i][j] < 0:
                filtrated_image[i][j] = 0
    return filtrated_image


def main():
    array = create_noisy_images("girl.jpg", 5, 100)
    for i in range(5):
        cv.imshow("noise", array[i])
        cv.waitKey()
    clear = filtrate_noisy_images(array)
    cv.imshow("clear", clear)
    cv.waitKey()


if __name__ == "__main__":
    main()

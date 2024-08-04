import cv2


def pixel_brightness_counter(path, brightness):
    img = cv2.imread(path, cv2.IMREAD_COLOR)
    n = 0
    print(type(img[1, 2][0]))
    for x in range(0, img.shape[0]):
        for y in range(0, img.shape[1]):
            if (int(img[x, y][0]) + int(img[x, y][1]) + int(img[x, y][2])) / 3 > brightness:
                n += 1
    return n / (img.shape[0] * img.shape[1]) * 100


def show_image(path):
    img = cv2.imread(path, cv2.IMREAD_COLOR)
    assert img is not None, "Error"
    cv2.imshow(path, img)
    print("Enter any value while image is opened to close the image and terminate the process")
    cv2.waitKey()


if __name__ == '__main__':
    print("Enter Brightness value:")
    brightness = int(input())
    print(pixel_brightness_counter('square.jpg', brightness))
    show_image('square.jpg')

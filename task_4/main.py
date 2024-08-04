import tkinter
import cv2 as cv
from matplotlib import pyplot as plt
from tkinter import *


class MainApplication:
    def __init__(self, master, path):
        self.master = master
        self.img = cv.imread(path, cv.IMREAD_COLOR)
        assert self.img is not None, "Path is not correct"
        self.alpha_slider = tkinter.Scale(self.master, from_=0, to=30, orient=HORIZONTAL, length=1500,
                                          command=self.update_value)
        self.alpha_slider.pack()
        self.alpha_slider.set(1.0)
        self.alpha_value = self.alpha_slider.get()
        self.beta_slider = tkinter.Scale(self.master, from_=0, to=30, orient=HORIZONTAL, length=1500,
                                         command=self.update_value)
        self.beta_slider.pack()
        self.beta_value = self.beta_slider.get()
        self.gamma_slider = tkinter.Scale(self.master, from_=0, to=3, orient=HORIZONTAL, length=1500,
                                          command=self.update_value, resolution=0.2)
        self.gamma_slider.pack()
        self.gamma_slider.set(10.0)
        self.gamma_value = self.gamma_slider.get()

    def update_value(self, event):
        self.alpha_value = self.alpha_slider.get()
        self.beta_value = self.beta_slider.get()
        self.gamma_value = self.gamma_slider.get()
        converted = cv.convertScaleAbs((self.img / 255) ** self.gamma_value * 255,
                                       alpha=self.alpha_value,
                                       beta=self.beta_value)
        cv.imshow('converted', converted)


def draw_histogram(path, is_equalized):
    img = cv.imread(path, cv.IMREAD_GRAYSCALE)
    assert img is not None, "Path error"
    if is_equalized:
        img = cv.equalizeHist(img)
    hist = cv.calcHist([img], [0], None, [256], [0, 256])
    plt.hist(img.ravel(), 256, [0, 256])
    plt.show()


def main():
    master = Tk()
    app = MainApplication(master, 'everest.jpg')
    draw_histogram('everest.jpg', True)
    master.mainloop()


if __name__ == "__main__":
    main()

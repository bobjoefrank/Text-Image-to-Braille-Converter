import numpy as np 
import cv2
from matplotlib import pyplot
from scipy import ndimage

# bunch of values we can vary
surfHessian = 500


def main():
    input_img = cv2.imread("./test_images/IMG_0567.JPG", -1)
    input_img = cv2.resize(input_img, (0,0), fx=0.3, fy=0.3)
    input_img = ndimage.rotate(input_img, 270)
    cv2.imshow("input", input_img)

    key = chr(cv2.waitKey(0))
    while key != 'q':
        key = cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__=="__main__":
    main()

import numpy as np 
import cv2
import matplotlib
matplotlib.use('PS')
from matplotlib import pyplot as plt
from scipy import ndimage

from model.serve import load_model, predict

# bunch of values we can vary
surfHessian = 500

def main():
    # input_img = cv2.imread("./test_images/IMG_0567.JPG", -1)
    # input_img = cv2.resize(input_img, (0,0), fx=0.1, fy=0.1)
    # input_img = ndimage.rotate(input_img, 270)

    
    
    # orb = cv2.ORB_create()
    # keypoints = orb.detect(input_img, None)
    # keypoints, descriptors = orb.compute(input_img, keypoints)
    
    # input_img = cv2.drawKeypoints(input_img, keypoints, None, (255,0,0), 4)

    # cv2.imshow("input", input_img)

    # key = chr(cv2.waitKey(0))
    # while key != 'q':
    #     key = cv2.waitKey(0)
    # cv2.destroyAllWindows()

    cap = cv2.VideoCapture(0)
    ret_open = cap.isOpened()
    if(not ret_open):
        return -1

    # Load the model and the mapping.
    model, mapping = load_model("model/bin")

    while(cap.isOpened()):
        ret, frame = cap.read()
        
        if ret == True:
            height, width, channels = frame.shape
            crop_img = frame[(int)(height/2-30):(int)(height/2+30), (int)(width/2-18):(int)(width/2+18)]
            # cv2.rectangle(frame,(width//2-30,height//2-30),(width//2+30,height//2+30),(0,0,255),3,-1)
            cv2.imshow('frame', frame)
            crop_gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
            # equi_gray = cv2.equalizeHist(crop_gray)
            clipLimit = 10.0
            tileGridSize = (4,4)
            clahe = cv2.createCLAHE(clipLimit, tileGridSize)
            equi_gray = clahe.apply(crop_gray)
            kernel = np.ones((7,7),np.uint8)
            opening_gray = cv2.morphologyEx(equi_gray, cv2.MORPH_OPEN, kernel)
            invert_img = cv2.bitwise_not(opening_gray)

            height, width = invert_img.shape
            for i in range(height):
                for j in range(width):
                    if invert_img.item(i,j) < 150:
                        invert_img.itemset((i,j),0)
            
            cv2.imshow('invert_img', invert_img)

            # Make a prediction on PNG image.
            print(predict(invert_img, model, mapping))

            key = chr(cv2.waitKey(0))
            if key == 'q':
                break
    cap.release()
    cv2.destroyAllWindows()            



if __name__=="__main__":
    main()

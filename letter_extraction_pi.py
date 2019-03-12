from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import numpy as np 
import cv2
import matplotlib
matplotlib.use('PS')
from matplotlib import pyplot as plt
from scipy import ndimage

from model.serve import load_model, predict
from servo import *

# bunch of values we can vary
surfHessian = 500
width = 320
height = 240
box_height = 24
box_width = 17

def main():
    
    # Load the model and the mapping.
    model, mapping = load_model("model/bin")

    # initialize the camera and grab a reference to the raw camera capture
    camera = PiCamera()
    camera.resolution = (width, height)
    camera.framerate = 20
    rawCapture = PiRGBArray(camera, size=(width, height))
    
    # allow the camera to warmup
    time.sleep(0.1)
    
    # capture frames from the camera
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        # grab the raw NumPy array representing the image, then initialize the timestamp
        # and occupied/unoccupied text
        image = frame.array
    
        # image processing
        crop_img = image[(int)(height/2-box_height):(int)(height/2+box_height), (int)(width/2-box_width):(int)(width/2+box_width)]
        crop_gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
        invert_img = cv2.bitwise_not(crop_gray)
        clipLimit = 40.0
        tileGridSize = (1,1)
        clahe = cv2.createCLAHE(clipLimit, tileGridSize)
        equi_gray = clahe.apply(invert_img)
        kernel = np.ones((3,3),np.uint8)
        erode_gray = cv2.erode(equi_gray, kernel, iterations = 2)
        
        # make padded image
        padded_img = cv2.copyMakeBorder(erode_gray, top=0, bottom=0, left=box_height-box_width+0, right=box_height-box_width+0, borderType= cv2.BORDER_CONSTANT, value=[0] ) 
       
        h, w = padded_img.shape
        for i in range(h):
            for j in range(w):
                if padded_img.item(i,j) < 90:
                    padded_img.itemset((i,j),0)

        # invert for CNN
        #cnn_img = cv2.bitwise_not(padded_img)

        # show images
        cv2.rectangle(image,(width//2-18,height//2-30),(width//2+18,height//2+30),(0,0,255),3,-1)
        cv2.imshow("Frame", image)
        cv2.imshow("gray", crop_gray)
        cv2.imshow("inverted", invert_img)
        cv2.imshow("equilized", equi_gray)
        cv2.imshow("eroded", erode_gray)
        cv2.imshow("padded", padded_img)
        #cv2.imshow("cnn", cnn_img)

        key = cv2.waitKey(1) & 0xFF

        # make letter prediction
        prediction = predict(padded_img, model, mapping)
        print(prediction)

        # activate pins for letter prediction if confidence is above certain threshold
        if float(prediction["confidence"]) >= 60:
            letter_to_pins(prediction["prediction"])
    
        # clear the stream in preparation for the next frame
        rawCapture.truncate(0)
    
        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
            break

if __name__=="__main__":
    main()

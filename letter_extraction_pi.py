import time
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
    
    # initialize the camera and grab a reference to the raw camera capture
    camera = PiCamera()
    camera.resolution = (640, 480)
    camera.framerate = 16
    rawCapture = PiRGBArray(camera, size=(640, 480))
    
    # allow the camera to warmup
    time.sleep(0.1)
    
    # capture frames from the camera
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        # grab the raw NumPy array representing the image, then initialize the timestamp
        # and occupied/unoccupied text
        image = frame.array
    
        # show the frame
        cv2.imshow("Frame", image)
        key = cv2.waitKey(1) & 0xFF
    
        # clear the stream in preparation for the next frame
        rawCapture.truncate(0)
    
        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
            break

if __name__=="__main__":
    main()
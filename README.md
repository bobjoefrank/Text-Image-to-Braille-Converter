# Text-Image-to-Braille-Converter

Our Senior Design Capstone Project aimed to design a device that will help visually-impaired individuals to read text from print such as books and newspapers. 

![](https://github.com/bobjoefrank/Text-Image-to-Braille-Converter/blob/master/documentation/IMG_1013.JPG)

## Project Overview

Our device uses an 8MP Pi Camera connected to a Raspberry Pi 3 that the user would hold and move to scan printed text. Scanned text goes through image processing using [OpenCV](https://opencv.org/) and is fed into a convolution neural network trained on the [EMNIST](https://www.nist.gov/node/1298471/emnist-dataset) Balanced classes dataset.

<p float="left">
  <img src="https://github.com/bobjoefrank/Text-Image-to-Braille-Converter/blob/master/documentation/IMG_1048.PNG" height="550">
  <img src="https://github.com/bobjoefrank/Text-Image-to-Braille-Converter/blob/master/documentation/Screen Shot 2019-03-08 at 01.33.52.png" height="550">
</p>

Identified letters are outputted onto our makeshift braille display made from six servos which uses the [pigpio](http://abyz.me.uk/rpi/pigpio/index.html) library to control the GPIO pins.

<p float="left">
  <img src="https://github.com/bobjoefrank/Text-Image-to-Braille-Converter/blob/master/documentation/IMG_1010.JPG" height="350">
  <img src="https://github.com/bobjoefrank/Text-Image-to-Braille-Converter/blob/master/documentation/IMG_20190218_152720.jpg" height="350">
</p>

## Setup

Install pip3.
```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python3-pip
```
Install OpenCV and image libraries.
```
sudo pip install opencv-contrib-python

sudo apt-get install libhdf5-dev libhdf5-serial-dev libhdf5-100
sudo apt-get install libqtgui4 libqtwebkit4 libqt4-test python3-pyqt5
sudo apt-get install libatlas-base-dev
sudo apt-get install libjasper-dev
sudo apt-get install libgtk-3-dev
```
Install Tensorflow.
```
# https://www.raspberrypi.org/magpi/tensorflow-ai-raspberry-pi/
sudo apt install libatlas-base-dev
pip3 install tensorflow
```
Install pigpio library.
```
wget abyz.me.uk/rpi/pigpio/pigpio.zip
unzip pigpio.zip
cd PIGPIO
make
sudo make install
```
Install dependencies.
```
pip3 install -r model/requirements.txt
```

Connect the servos to the GPIO pins and connect the Pi camera ribbon to the CSI camera slot.

<img src="https://github.com/bobjoefrank/Text-Image-to-Braille-Converter/blob/master/documentation/servo_layout.jpg" height="350">

## Usage
Enable X11 forwarding when you ssh into Pi.
```
ssh -Y pi@raspberrypi.local
```
Start pigpio daemon and then run the program.
```
sudo pigpiod
python3 letter_extraction_pi.py
```
The camera will turn on and the servos will automatically start moving on their own.

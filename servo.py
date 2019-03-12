# start daemon with $ sudo pigpiod
import RPi.GPIO as GPIO
import time
import pigpio

# letter to pins mapping
# pins start from top left and goes down column and then next row
braille_map = { 
        "a" : [True, False, False, False, False, False],
        "b" : [True, True, False, False, False, False],
        "c" : [True, False, False, True, False, False],
        "d" : [True, False, False, True, True, False],
        "e" : [True, False, False, False, True, False],
        "f" : [True, True, False, True, False, False],
        "g" : [True, True, False, True, True, False],
        "h" : [True, True, False, False, True, False],
        "i" : [False, True, False, True, False, False],
        "j" : [False, True, False, True, True, False],
        "k" : [True, False, True, False, False, False],
        "l" : [True, True, True, False, False, False],
        "m" : [True, False, True, True, False, False],
        "n" : [True, False, True, True, True, False],
        "o" : [True, False, True, False, True, False],
        "p" : [True, True, True, True, False, False],
        "q" : [True, True, True, True, True, False],
        "r" : [True, True, True, False, True, False],
        "s" : [False, True, True, True, False, False],
        "t" : [False, True, True, True, True, False],
        "u" : [True, False, True, False, False, True],
        "v" : [True, True, True, False, False, True],
        "w" : [False, True, False, True, True, True],
        "x" : [True, False, True, True, False, True],
        "y" : [True, False, True, True, True, True],
        "z" : [True, False, True, False, True, True],
        "0" : [False, True, False, True, True, False],
        "1" : [True, False, False, False, False, False],
        "2" : [True, True, False, False, False, False],
        "3" : [True, False, False, True, False, False],
        "4" : [True, False, False, True, True, False],
        "5" : [True, False, False, False, True, False],
        "6" : [True, True, False, True, False, False],
        "7" : [True, True, False, True, True, False],
        "8" : [True, True, False, False, True, False],
        "9" : [False, True, False, True, False, False]
        }

#GPIO.setmode(GPIO.BOARD)

#channel_list = [40, 37, 38, 35, 36, 33]
#GPIO.setup(channel_list, GPIO.OUT)

#pin1 = GPIO.PWM(40, 50)
#pin2 = GPIO.PWM(38, 50)
#pin3 = GPIO.PWM(36, 50)
#pin4 = GPIO.PWM(37, 50)
#pin5 = GPIO.PWM(35, 50)
#pin6 = GPIO.PWM(33, 50)

#pin1.start(7.5)
#pin2.start(7.5)
#pin3.start(7.5)
#pin4.start(7.5)
#pin5.start(7.5)
#pin6.start(7.5)

pi = pigpio.pi()

#pin layout 
# 40 37
# 38 35
# 36 33

#add something to keep the pins the same state instead of reassigning new duty cycle
#gets all glitchy if reassigned
#7.5, 5.5

temp0 = False
temp1 = False 
temp2 = False
temp3 = False
temp4 = False
temp5 = False
def letter_to_pins(letter):
    global temp0
    global temp1
    global temp2
    global temp3
    global temp4
    global temp5
    mapping = braille_map[letter.lower()]
    if mapping[0] != temp0:
        temp0 = mapping[0]
        if mapping[0] == True:
            pi.set_servo_pulsewidth(21, 1500)
            #pin1.ChangeDutyCycle(7.5)
        else:
            pi.set_servo_pulsewidth(21, 1150)
            #pin1.ChangeDutyCycle(7.5)
    if mapping[1] != temp1:
        temp1 = mapping[1]
        if mapping[1] == True:
            pi.set_servo_pulsewidth(20, 1500)
            #pin2.ChangeDutyCycle(7.5)
        else:
            pi.set_servo_pulsewidth(20, 1150)
            #pin2.ChangeDutyCycle(7.5)
    if mapping[2] != temp2:
        temp2 = mapping[2]
        if mapping[2] == True:
            pi.set_servo_pulsewidth(16, 1500)
            #pin3.ChangeDutyCycle(7.5)
        else:
            pi.set_servo_pulsewidth(16, 1150)
            #pin3.ChangeDutyCycle(7.5)
    if mapping[3] != temp3:
        temp3 = mapping[3]
        if mapping[3] == True:
            pi.set_servo_pulsewidth(26, 1500)
            #pin4.ChangeDutyCycle(7.5)
        else:
            pi.set_servo_pulsewidth(26, 1150)
            #pin4.ChangeDutyCycle(7.5)
    if mapping[4] != temp4:
        temp4 = mapping[4]
        if mapping[4] == True:
            pi.set_servo_pulsewidth(19, 1500)
            #pin5.ChangeDutyCycle(7.5)
        else:
            pi.set_servo_pulsewidth(19, 1150)
            #pin5.ChangeDutyCycle(7.5)
    if mapping[5] != temp5:
        temp5 = mapping[5]
        if mapping[5] == True:
            pi.set_servo_pulsewidth(13, 1500)
            #pin6.ChangeDutyCycle(7.5)
        else:
            pi.set_servo_pulsewidth(13, 1150)
            #pin6.ChangeDutyCycle(7.5)
    # time delay causes lag in system for pins to move
    time.sleep(1)

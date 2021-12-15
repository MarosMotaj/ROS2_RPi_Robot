#! /usr/bin/env python3

"""Class for Cytron MD20A motor driver"""
import time

import RPi.GPIO as GPIO


class Motor:

    def __init__(self, pinAN1=12, pinAN2=13, pinDIG1=26, pinDIG2=25):

        self.pinAN1 = pinAN1
        self.pinAN2 = pinAN2
        self.pinDIG1 = pinDIG1
        self.pinDIG2 = pinDIG2

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        GPIO.setup(self.pinAN1, GPIO.OUT)
        GPIO.setup(self.pinAN2, GPIO.OUT)
        GPIO.setup(self.pinDIG1, GPIO.OUT)
        GPIO.setup(self.pinDIG2, GPIO.OUT)

        # pwm value from 0 to 100 max, set speed of motor rotation
        self.motor1 = GPIO.PWM(self.pinAN1, 100)
        self.motor2 = GPIO.PWM(self.pinAN2, 100)

        self.stop()

    def forward(self, speed_pwm):
        
        GPIO.output(self.pinDIG1, GPIO.HIGH)
        self.motor1.start(speed_pwm)
        GPIO.output(self.pinDIG2, GPIO.LOW)
        self.motor2.start(speed_pwm)

    def reverse(self, speed_pwm):
        
        GPIO.output(self.pinDIG1, GPIO.LOW)
        self.motor1.start(speed_pwm)
        GPIO.output(self.pinDIG2, GPIO.HIGH)
        self.motor2.start(speed_pwm)

    def turn_right(self, speed_pwm):
        
        GPIO.output(self.pinDIG1, GPIO.LOW)
        self.motor1.start(speed_pwm)
        GPIO.output(self.pinDIG2, GPIO.LOW)
        self.motor2.start(speed_pwm)

    def turn_left(self, speed_pwm):
        
        GPIO.output(self.pinDIG1, GPIO.HIGH)
        self.motor1.start(speed_pwm)
        GPIO.output(self.pinDIG2, GPIO.HIGH)
        self.motor2.start(speed_pwm)

    def stop(self):
        
        self.motor1.start(0)
        self.motor2.start(0)




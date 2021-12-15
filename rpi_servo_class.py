#Raspberry Pi
import RPi.GPIO as GPIO
import time
import math

class Servo:

    def rotate(command):
         input_axis_data = math.floor(command*10)/10
         print(f"Command {input_axis_data}")
         GPIO.setmode(GPIO.BCM)
         GPIO.setup(19, GPIO.OUT)
         pwm = GPIO.PWM(19,50)
         pwm.start(7)

         if input_axis_data >= 0:
             desirePosition = (input_axis_data * 100)*2
             print(desirePosition)
             DC = 1./18.*(desirePosition)+2
             pwm.ChangeDutyCycle(DC)
             time.sleep(1)
        # pwm.stop()
        # GPIO.cleanup()

"""         if command > 0:
              time.sleep(0.5)
              if command == 0.2:
                  pwm.ChangeDutyCycle(5)
                  print("pozicia 1")
                  time.sleep(0.5)
              if command == 0.5:
                  pwm.ChangeDutyCycle(7.5)
                  print("pozicia 2")
              if command == 0.7:
                  pwm.ChangeDutyCycle(10)
              if command == 1:
                  pwm.ChangeDutyCycle(12.5)

         if command < 0:
              print("Command je mensie ako 0")
              if command == -0.2:
                  pwm.ChangeDutyCycle(12.5)
              elif command == -0.5:
                  pwm.ChangeDutyCycle(10)
              elif command == -0.7:
                  pwm.ChangeDutyCycle(7.5)
              elif command == -1:
                  pwm.ChangeDutyCycle(5)"""



             #p.ChangeDutyCycle(12.5)
             #time.sleep(0.5)
             #p.ChangeDutyCycle(10)
             #time.sleep(0.5)
             #p.ChangeDutyCycle(7.5)
             #time.sleep(0.5)
             #p.ChangeDutyCycle(5)

#for (pos = 0; pos <= 180; pos += 1) { // goes from 0 degrees to 180 degrees
#    // in steps of 1 degree
#    myservo.write(pos);              // tell servo to go to position in variable 'pos'
#    delay(15);    



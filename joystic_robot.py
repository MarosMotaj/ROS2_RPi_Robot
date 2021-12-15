#! /usr/bin/env python3
#from rpi_servo_class import Servo    moja GPIO servo classa
from text_speech_class import Speach  # moja classa na rozpravanie textu

from motor import Motor
import math

# ROS 2
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy, Range



class MopatorRobot (Node):

    '''
    Creates listener on /command to accept string-style commands.
    Creates listener on /cmd_vel to accept twist messages.
    Creates listener on /joy to accept xbox joystick input.

    '''

    def __init__(self, name):

        super().__init__(name)

        self.motors = Motor()

        self._joy_subscription = self.create_subscription(
            Joy,
            'joy',
            self._joy_callback,
            5)

    def _joy_callback(self, msg):
        '''Translate XBox buttons into speed and spin

        Just use the left joystick (for now):
        LSB left/right  axes[3]     +1 (left) to -1 (right)
        LSB up/down     axes[1]     +1 (up) to -1 (back)
        LB              buttons[5]  1 pressed, 0 otherwise
        '''

        if (msg.axes[1]) > 0:
            self.motors.forward(msg.axes[1]*100)
            print("forward method")

        elif (msg.axes[1]) < 0:
            self.motors.reverse(abs(msg.axes[1])*100)
            print("backward method")


        elif (msg.axes[0]) > 0:
            self.motors.turn_left(msg.axes[0]*100)
            print("turn left method")

        elif (msg.axes[0]) < 0:
            self.motors.turn_right(abs(msg.axes[0])*100)
            print("turn right method")

        else:
            self.motors.stop() 

        '''
        if (abs(msg.axes[1]) == 0) and (abs(msg.axes[0]) == 0):
            self.motors.stop()
        '''
        #if abs(msg.axes[2]) > 0.10:
        #   Servo.rotate(msg.axes[2])


        #if abs(msg.axes[3]) > 0.10:   # move servo up, down
        #   Servo.rotate(msg.axes[3])


        if msg.buttons[3] == 1:
            pass

        if msg.buttons[2] == 1:
            pass


def main(args=None):

    rclpy.init(args=args)

    w = MopatorRobot('MopatorRobot')

    # enable the keyboard controller:
    # ros2 run teleop_twist_keyboard teleop_twist_keyboard
    #
    # enable the joystick:
    # ros2 run joy joy_node
    #
    print("ROBOT IS ACTIVATED!")
    Speach.talk("robot is activated and ready to use")
    rclpy.spin(w)
    rclpy.shutdown()


if __name__ == '__main__':
    main()

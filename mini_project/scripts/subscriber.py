#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64
from sensor_msgs.msg import Joy

def callback(data):
    rospy.loginfo(data)

def display_l():
    rospy.init_node('display_l', anonymous = True)
    rospy.Subscriber("chatter1", Float64, callback)
    rospy.spin()

def display_r():
    rospy.init_node('display_r', anonymous = True)
    rospy.Subscriber("chatter2", Float64, callback)
    rospy.spin()

if __name__ == '__main__':
    display_l()

if __name__ == '__main__':
    display_r()

#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64
from sensor_msgs.msg import Joy

def left_v():
    pub = rospy.Publisher('chatter1', Float64, queue_size = 10)
    rospy.init_node('left', anonymous = True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        zoom_1 = 100*Joy.axes[1]
        rospy.loginfo(zoom_1)
        pub.publish(zoom_1)

def right_v():
    pub = rospy.Publisher('chatter2', Float64, queue_size = 10)
    rospy.init_node('right', anonymous = True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        zoom_2 = 100*Joy.axes[4]
        rospy.loginfo(zoom_2)
        pub.publish(zoom_2)

if __name__ == '__main__':
    left_v()

if __name__ == '__main__':
    right_v()

#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Joy

def callback(data):
    100 * data.axes[1]
    100 * data.axes[4]

def start():
    rospy.init_node('display', anonymous = True)
    rospy.Subscriber("joy", Joy, callback)
    rospy.spin()
    rospy.Publisher('output', Joy, queue_size = 10)
    while not rospy.is_shutdown():
        pub.publish(100 * data.axes[1])
        pub.publish(100 * data.axes[4])

if __name__ == '__main__':
    start()

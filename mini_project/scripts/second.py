#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Joy

def callback(data):
    pub.publish(100 * data.axes[1])
    pub.publish(100 * data.axes[4])

def start():
    rospy.init_node('display', anonymous = True)
    rospy.Subscriber("joy", Joy, callback)
    global pub
    pub = rospy.Publisher('output', Joy, queue_size = 10)
    rospy.spin()

if __name__ == '__main__':
    start()

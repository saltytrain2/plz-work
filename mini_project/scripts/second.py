#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Joy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo("{} {}".format(100 * data.axes[1], 100 * data.axes[4]))
    pub.publish(("{} {}".format(100 * data.axes[1], 100 * data.axes[4])))

def start():
    rospy.init_node('display', anonymous = True)
    rospy.Subscriber("joy", Joy, callback)
    global pub
    pub = rospy.Publisher('output', String, queue_size = 10)
    rospy.spin()

if __name__ == '__main__':
    try:
        start()
    except rospy.ROSInterruptException:
        pass

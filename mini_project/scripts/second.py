#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Joy

def callback(data):
    rospy.loginfo(Joy.axes[1], Joy.axes[4], data.data)

def display():
    rospy.init_node('display', anonymous = True)
    rospy.Subscriber("joy", Joy, callback)
    rospy.spin()

if __name__ == '__main__':
    display()

def output():
    pub = rospy.Publisher('outputs', String, queue_size = 10)
    rospy.init_node('output', anonymous = True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        rospy.loginfo(display())
        pub.publish(display())
        rate.sleep()

if __name__ == '__main__':
    try:
        output()
    except rospy.ROSInterruptException:
        pass

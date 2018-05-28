#!/usr/bin/python
# -*- coding: utf-8 -*- 
#       FileName:  talker.py
#
#    Description:
#
#        Version:  1.0
#        Created:  2018-05-24 10:12:40
#  Last Modified:  2018-05-28 10:15:28
#       Revision:  none
#       Compiler:  gcc
#
#         Author:  zt ()
#   Organization:

import rospy
from std_msgs.msg import String


def myhook():
    print 'is_shutdown time %s' % rospy.get_time()


def talker():
    pub = rospy.Publisher('chat2', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rospy.on_shutdown(myhook)
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        str = 'test %s' % rospy.get_name()

        # rospy.loginfo(str)

        pub.publish(str)
        rate.sleep()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass


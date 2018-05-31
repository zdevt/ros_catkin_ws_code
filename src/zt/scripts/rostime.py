#!/usr/bin/env python
#-*- coding:utf-8 -*-
#       FileName:  rostime.py
#
#    Description:
#
#        Version:  1.0
#        Created:  2018-05-31 16:03:44
#  Last Modified:  2018-05-31 16:08:56
#       Revision:  none
#       Compiler:  gcc
#
#         Author:  zt ()
#   Organization:

import rospy


def talker():
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        now = rospy.get_rostime()
        rospy.loginfo("Current time %i %i", now.secs, now.nsecs)
        rate.sleep()


if __name__ == '__main__':
    talker()

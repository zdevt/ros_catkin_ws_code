#!/usr/bin/env python
#-*- coding:utf-8 -*-
#       FileName:  numpy_talker.py
#
#    Description:
#
#        Version:  1.0
#        Created:  2018-05-25 16:51:32
#  Last Modified:  2018-05-25 16:56:22
#       Revision:  none
#       Compiler:  gcc
#
#         Author:  zt ()
#   Organization:

import rospy
from rospy.numpy_msg import numpy_msg
from zt.msg import Floats

import numpy


def talker():
    rospy.init_node('talker',anonymous=True)
    pub = rospy.Publisher('FLOATS',numpy_msg(Floats),queue_size=10)
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        a = numpy.array([1.11110,2.1,3.2],dtype=numpy.float32)
        pub.publish(a)
        rate.sleep()

if __name__ == "__main__":
    talker();



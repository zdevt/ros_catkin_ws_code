#!/usr/bin/env python
#-*- coding:utf-8 -*-
#       FileName:  listenner_numpy.py
#
#    Description:
#
#        Version:  1.0
#        Created:  2018-05-25 16:28:55
#  Last Modified:  2018-05-25 16:49:18
#       Revision:  none
#       Compiler:  gcc
#
#         Author:  zt ()
#   Organization:

import rospy
from zt.msg import Floats
from rospy.numpy_msg import numpy_msg

def callback(data):
    print( rospy.get_time(), "i heard %s" %str(data.data))

def listener():
    rospy.init_node('listener')
    rospy.Subscriber('FLOATS',numpy_msg(Floats),callback)
    rospy.spin()

if __name__ == "__main__":
    listener()


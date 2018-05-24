#!/usr/bin/env python
#-*- coding:utf-8 -*-
#       FileName:  listenner.py
#
#    Description:
#
#        Version:  1.0
#        Created:  2018-05-24 10:18:05
#  Last Modified:  2018-05-24 10:23:53
#       Revision:  none
#       Compiler:  gcc
#
#         Author:  zt ()
#   Organization:

import rospy
from std_msgs.msg import String 

def callback(data):
    rospy.loginfo(data.data)

def listenner():
    rospy.init_node('listenner',anonymous=True)
    sub=rospy.Subscriber('chat2',String,callback)
    rospy.spin()


if __name__ == "__main__":
    listenner()

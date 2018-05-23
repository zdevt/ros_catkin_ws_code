#!/usr/bin/env python
#-*- coding:utf-8 -*-
#       FileName:  listener.py
#
#    Description:
#
#        Version:  1.0
#        Created:  2018-05-23 15:48:05
#  Last Modified:  2018-05-23 15:50:45
#       Revision:  none
#       Compiler:  gcc
#
#         Author:  zt ()
#   Organization:

import rospy
from std_msgs.msg import String


def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "i heard %s", data.data)

def listener():
    rospy.init_node('listener',anonymous=True)
    rospy.Subscriber('chatter',String,callback)
    rospy.spin()


if __name__ == '__main__':
    listener()


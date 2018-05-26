#!/usr/bin/python
# -*- coding: utf-8 -*-

#       FileName:  video_listener.py
#
#    Description:
#
#        Version:  1.0
#        Created:  2018-05-26 13:19:37
#  Last Modified:  2018-05-26 15:10:17
#       Revision:  none
#       Compiler:  gcc
#
#         Author:  zt ()
#   Organization:

import cv2
import imutils
import rospy
import numpy as np

from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image


def callback(data):
    frame = CvBridge().imgmsg_to_cv2(data, 'bgr8')
    cv2.imshow('frame', frame)


def listenner():
    rospy.init_node('listenner', anonymous=True)
    sub = rospy.Subscriber('video', Image, callback)
    rospy.spin()


if __name__ == '__main__':
    listener()

#!/usr/bin/python
# -*- coding: utf-8 -*-

#       FileName:  video_listener.py
#
#    Description:
#
#        Version:  1.0
#        Created:  2018-05-26 13:19:37
#  Last Modified:  2018-06-01 09:01:50
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
# from sensor_msgs.msg import Image
from sensor_msgs.msg import CompressedImage


def callback(data):
    #frame = CvBridge().imgmsg_to_cv2(data, 'bgr8')
    frame = CvBridge().compressed_imgmsg_to_cv2(data, 'bgr8')
    cv2.imshow('frame', frame)
    cv2.waitKey(1)


def listener():
    rospy.init_node('listener', anonymous=True)
    sub = rospy.Subscriber('video', CompressedImage, callback)
    rospy.spin()


if __name__ == '__main__':
    listener()

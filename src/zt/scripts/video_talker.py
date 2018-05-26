#!/usr/bin/python
# -*- coding: utf-8 -*-

#       FileName:  video_talker.py
#
#    Description:
#
#        Version:  1.0
#        Created:  2018-05-26 11:15:48
#  Last Modified:  2018-05-26 15:11:20
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


def GetImgAndPub():
    rospy.init_node('video_talker', anonymous=True)
    pub = rospy.Publisher('video', Image, queue_size=10)
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FPS, 10)

    while cap.isOpened() and not rospy.is_shutdown():
        (_, frame) = cap.read()
        frame = imutils.resize(frame, width=300)
        data = CvBridge().cv2_to_imgmsg(frame, 'bgr8')
        pub.publish(data)
        cv2.imshow('frame', frame)
        cv2.waitKey(1)

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    GetImgAndPub()


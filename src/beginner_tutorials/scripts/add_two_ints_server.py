#!/usr/bin/env python
#-*- coding:utf-8 -*-
#       FileName:  add_two_ints_server.py
#
#    Description:
#
#        Version:  1.0
#        Created:  2018-05-23 15:56:34
#  Last Modified:  2018-05-23 17:10:36
#       Revision:  none
#       Compiler:  gcc
#
#         Author:  zt ()
#   Organization:

from beginner_tutorials.srv import *
import rospy

def handle_add_two_ints(req):
    print ( "Returning [%s + %s = %s]" % (req.a,req.b,(req.a+req.b)))
    return AddTwoIntsResponse(req.a+req.b)

def add_two_ints_server():
    rospy.init_node('add_two_ints_server')
    s = rospy.Service('add_two_ints', AddTwoInts, handle_add_two_ints)
    print("Ready to add two ints.")
    rospy.spin()

if __name__ == "__main__":
    add_two_ints_server()




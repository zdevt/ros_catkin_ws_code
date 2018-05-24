#!/usr/bin/env python
#-*- coding:utf-8 -*-
#       FileName:  zt_server.py
#
#    Description:
#
#        Version:  1.0
#        Created:  2018-05-24 14:13:12
#  Last Modified:  2018-05-24 14:28:50
#       Revision:  none
#       Compiler:  gcc
#
#         Author:  zt ()
#   Organization:

from zt.srv import *
import rospy

def handle_zt(req):
    print("Returning[%s*%s=%s]"%(req.A,req.B,req.A*req.B))
    return ztResponse(req.A*req.B)

def zt_server():
    rospy.init_node('zt_server')
    s = rospy.Service('zt',zt,handle_zt)
    print("zt ready")
    rospy.spin()

if __name__ == "__main__":
    zt_server()


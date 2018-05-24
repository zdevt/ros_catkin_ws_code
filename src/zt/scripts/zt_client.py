#!/usr/bin/env python
#-*- coding:utf-8 -*-
#       FileName:  zt_client.py
#
#    Description:
#
#        Version:  1.0
#        Created:  2018-05-24 14:17:54
#  Last Modified:  2018-05-24 14:26:29
#       Revision:  none
#       Compiler:  gcc
#
#         Author:  zt ()
#   Organization:

import sys
import rospy
from zt.srv import  *

def zt_clilent(x,y):
    rospy.wait_for_service('zt')
    try:
        zt1 = rospy.ServiceProxy('zt',zt)
        resp1 = zt1(x,y)
        return resp1.C
    except rospy.ServiceException,e:
        print("service error %s" %e)

if __name__ == "__main__":
    if  len(sys.argv) == 3 :
        x = float(sys.argv[1])
        y = float(sys.argv[2])
    else:
        sys.exit(1)
    print("%s*%s=%s" %(x,y,zt_clilent(x,y)))



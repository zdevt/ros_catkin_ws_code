#!/usr/bin/env python
#-*- coding:utf-8 -*-
#       FileName:  add_two_ints.client.py
#
#    Description:
#
#        Version:  1.0
#        Created:  2018-05-23 17:13:28
#  Last Modified:  2018-05-23 17:18:50
#       Revision:  none
#       Compiler:  gcc
#
#         Author:  zt ()
#   Organization:

import sys
import rospy
from beginner_tutorials.srv import *

def add_two_ints_client(x,y):
    rospy.wait_for_service('add_two_ints')
    try:
        add_two_ints = rospy.ServiceProxy('add_two_ints',AddTwoInts)
        resp1 = add_two_ints(x,y)
        return resp1.sum;
    except rospy.ServiceException,e:
        print("ServiceException %s"%e)

def usage():
    return "%s [x y]" % sys.argv[0]


if __name__ == "__main__":
    if len(sys.argv) == 3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    else:
        print usage()
        sys.exit(1)

    print("requesting %s+%s"%(x,y))
    print("%s + %s=%s"%(x,y,add_two_ints_client(x,y)))




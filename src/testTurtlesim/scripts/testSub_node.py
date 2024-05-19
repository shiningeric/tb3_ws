#!/usr/bin/env python

from communication.pos_sub import pose_subscriber
import rospy

if __name__ == "__main__":
    try:
        pose_subscriber()
    except rospy.ROSInterruptException:
        pass

#!/usr/bin/env python

from communication.vel_pub import velocity_publisher
import rospy

if __name__ == "__main__":
    try:
        velocity_publisher()
    except rospy.ROSInterruptException:
        pass

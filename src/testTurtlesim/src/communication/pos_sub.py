#!/usr/bin/env python

import rospy
from turtlesim.msg import Pose

def poseCallback(msg):
    rospy.loginfo(f"Turtle pose: x={msg.x},y={msg.y}")


def pose_subscriber():
    rospy.init_node("pose_subscriber")
    rospy.Subscriber("/turtle1/pose",Pose, poseCallback)
    rospy.spin()


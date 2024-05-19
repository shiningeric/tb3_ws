#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

def velocity_publisher():
    rospy.init_node("velocity_publisher")

    vel_pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)

    rate = rospy.Rate(10)

    while not rospy.is_shutdown():

        vel_msg = Twist()
        vel_msg.linear.x = 0.5
        vel_msg.angular.z = 0.2

        vel_pub.publish(vel_msg)
        info = f"Publish turtle linear & angular velocity command {vel_msg.linear.x} and {vel_msg.angular.z}"
        rospy.loginfo(info)
        rate.sleep()


    

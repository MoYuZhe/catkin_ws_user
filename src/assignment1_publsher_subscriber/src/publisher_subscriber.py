#!/usr/bin/env python
import rospy
from std_msgs.msg import String, Float32

def callback(data):

    yaw_message = rospy.get_caller_id() + " I heard " + str(data.data)
    publisher.publish(yaw_message)
   

rospy.init_node('assignment1_publisher_subscriber', anonymous=True)
publisher = rospy.Publisher("/assignment1_publisher_subscriber", String, queue_size=10)
rospy.Subscriber("/yaw", Float32, callback)
rospy.spin()


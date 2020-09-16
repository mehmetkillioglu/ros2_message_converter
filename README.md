# ros2_message_converter
Ros2_message_converter is a lightweight ROS2 package and Python library to convert from Python dictionaries and JSON messages to rclpy messages, and vice versa

'''python
from ros2_message_converter import message_converter
from std_msgs.msg import String
msg_json = { "data": "Hello, Robot" }
msg_ros = message_converter.convert_dictionary_to_ros_message("std_msgs/String",)
msg_json = message_converter.convert_ros_message_to_dictionary(msg_ros)

'''


References:
[uos/rospy_message_converter](https://github.com/uos/rospy_message_converter)

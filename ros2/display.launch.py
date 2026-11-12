"""
URDF modelini RViz2'de gösterir ve eklemleri kaydırıcılarla oynatmanızı sağlar.

Çalıştırma (ROS 2 Jazzy/Humble, depo kökünden):
    ros2 launch ros2/display.launch.py

Gerekli paketler:
    sudo apt install ros-$ROS_DISTRO-robot-state-publisher \
                     ros-$ROS_DISTRO-joint-state-publisher-gui ros-$ROS_DISTRO-rviz2
RViz açılınca: Fixed Frame = world, Add -> RobotModel, Description Topic = /robot_description
"""
import os
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    urdf_yolu = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             "..", "urdf", "rrr_kol.urdf")
    with open(urdf_yolu, encoding="utf-8") as f:
        robot_tanimi = f.read()

    return LaunchDescription([
        Node(package="robot_state_publisher", executable="robot_state_publisher",
             parameters=[{"robot_description": robot_tanimi}]),
        Node(package="joint_state_publisher_gui", executable="joint_state_publisher_gui"),
        Node(package="rviz2", executable="rviz2"),
    ])

"""İki düğümü birlikte başlatır:  ros2 launch kol_ornek ornek.launch.py"""
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(package="kol_ornek", executable="yayinci", name="eklem_yayinci",
             parameters=[{"frekans_hz": 10.0}], output="screen"),
        Node(package="kol_ornek", executable="abone", name="uc_hesaplayici", output="screen"),
    ])
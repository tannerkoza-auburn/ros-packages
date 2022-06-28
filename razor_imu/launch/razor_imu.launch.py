import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    config = os.path.join(
        get_package_share_directory("razor_imu"), "config", "razor_imu.yaml"
    )

    return LaunchDescription(
        [
            Node(
                package="razor_imu",
                executable="razor_imu_node",
                namespace="razor_imu",
                name="imu",
                parameters=[config],
            )
        ]
    )

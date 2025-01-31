import os
import sys

import launch
import launch_ros.actions
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    ld = launch.LaunchDescription([
        launch_ros.actions.Node(
            package='exomy',
            executable='robot_node.py',
            name='robot',
            output='screen'
        ),
        launch_ros.actions.Node(
            package='exomy',
            executable='motor_node.py',
            name='motors',
            output='screen'
        ),
        launch_ros.actions.Node(
            package='exomy',
            executable='joystick_parser_node.py',
            name='joystick',
            output='screen'
        ),
        launch_ros.actions.Node(
            package='joy',
            executable='joy_node',
            name='joy_node',
            parameters=[
                {
                    'coalesce_interval': '0.05'
                }
            ]
        ),
        launch_ros.actions.Node(
            package='web_video_server',
            executable='web_video_server',
            name='web_video_server',
            output='screen',
            parameters=[
                {
                    'default_transport': 'compressed'
                },
                {
                    'quality': '50'
                }
            ]
        ),
        launch_ros.actions.Node(
            package='usb_cam',
            executable='usb_cam_node',
            name='pi_cam',
            output='screen',
            parameters=[
                {
                    'framerate': '10'
                },
                {
                    'video_device': '/dev/video0'
                },
                {
                    'image_width': '640'
                },
                {
                    'image_height': '480'
                },
                {
                    'pixel_format': 'yuyv'
                },
                {
                    'camera_frame_id': 'pi_cam'
                },
                {
                    'io_method': 'mmap'
                }
            ]
        ),
        launch.actions.IncludeLaunchDescription(
            launch.launch_description_sources.PythonLaunchDescriptionSource(
                os.path.join(get_package_share_directory(
                    'rosbridge_server'), 'launch/rosbridge_websocket.launch.py')
            )
        )
    ])
    return ld


if __name__ == '__main__':
    generate_launch_description()

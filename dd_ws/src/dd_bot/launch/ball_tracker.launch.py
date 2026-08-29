import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch.substitutions import PythonExpression
from launch.actions import DeclareLaunchArgument


def generate_launch_description():

    my_package_name='dd_bot'
    
    tracker_params = os.path.join(get_package_share_directory(my_package_name),'config','ball_tracker_params.yaml')

    tracker_launch = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory('ball_tracker'), 'launch', 'ball_tracker.launch.py')]),
                    launch_arguments={'params_file': tracker_params,
                                    'image_topic': '/camera/image_raw',
                                    'cmd_vel_topic': '/cmd_vel_tracker',
                                    'enable_3d_tracker': 'true',  # True, for detection and following
                                    'tune_detection': 'false',   #Tuning, Reminder: Change the parameters in ball_tracker_params.yaml
                                    'follow_only': 'false',
                                    'detect_only': 'false'}.items())

    return LaunchDescription([
        tracker_launch,
    ])

import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():
    simloto7 = launch_ros.actions.Node(
            package='simloto7',
            executable='simloto7',
            )
    test_subscriber = launch_ros.actions.Node(
            package='simloto7',
            executable='test_subscriber',
            output='screen'
            )

    return launch.LaunchDescription([simloto7, test_subscriber]) 

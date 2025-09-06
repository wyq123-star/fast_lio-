from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    Key_read_node = Node(
        package='turtlesim',
        executable='turtle_teleop_key',
        name='key_listener',
        output='screen',        # 确保输出到屏幕，便于调试
        # emulate_tty=True,       # 关键尝试：启用终端仿真
        prefix='xterm -e',    # (可选) 尝试让节点在xterm终端中运行，如果系统支持的话
    )

    Key_listen_node = Node(
        package='node',
        executable='sub',
        name='key_subscriber',
        output='screen',        # 确保输出到屏幕，便于调试
        # emulate_tty=True,       # 关键尝试：启用终端仿真
        # prefix='xterm -e',    # (可选) 尝试让节点在xterm终端中运行，如果系统支持的话
    )

    launchDescription = LaunchDescription(
        [
            Key_read_node,
            Key_listen_node,
        ]
    )
    return launchDescription
#!/usr/bin/env python3
# coding:utf-8
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist  # 导入Twist消息类型
import subprocess

class KeyboardListener(Node):
    def __init__(self):
        super().__init__('keyboard_listener')
        self.launch_triggered = False
        
        # 创建订阅者，订阅/turtle1/cmd_vel话题
        self.subscription = self.create_subscription(
            Twist,
            '/turtle1/cmd_vel',
            self.cmd_vel_callback,
            10
        )
        self.subscription  # 防止未使用变量警告
        
        self.get_logger().info("Keyboard listener node started. Waiting for messages...")

    def cmd_vel_callback(self, msg):
        # 检查是否已经触发过，避免重复启动
        if not self.launch_triggered:
            self.get_logger().info("检测到速度命令，正在启动目标launch文件...")
            try:
                # 使用subprocess.Popen在后台启动launch文件
                # ROS2使用ros2 launch命令[6](@ref)
                process_slam = subprocess.Popen(["ros2", "launch", "fast_lio", "mapping.launch.py"])
                process_bag = subprocess.Popen(["ros2", "bag", "play", "/home/yutou/ros2_ws/bag/篮筐数据包/04-10-16-46/04-10-16-46_0.db3"])
                self.launch_triggered = True
                self.get_logger().info("目标launch文件已启动 (PID: %d)" % process_slam.pid)
            except Exception as e:
                self.get_logger().error("启动launch文件失败: %s" % str(e))

def main(args=None):
    rclpy.init(args=args)
    node = KeyboardListener()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
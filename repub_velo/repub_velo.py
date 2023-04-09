import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from builtin_interfaces.msg import Time

class Sub_and_Repub_Velo(Node):

    def __init__(self):
        super().__init__('velo_subscriber')
        self.get_logger().info(f"Republishing /scan -> /scan_new")

        self.publisher = self.create_publisher(LaserScan, '/scan_new', 100)
        self._velo_subscription = self.create_subscription(
            LaserScan, # msg_type
            '/scan', # topic
            self._velo_listener_callback,  # callback
            100)


    def _velo_listener_callback(self, msg):
        msg.angle_increment = 0.0070124836
        msg.header.frame_id = "lidar_1_link"
        # msg.header.stamp = self.get_clock().now().to_msg()

        self.publisher.publish(msg)


def main(args=None):
    rclpy.init(args=args)

    velo_subscriber = Sub_and_Repub_Velo()
    rclpy.spin(velo_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    velo_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
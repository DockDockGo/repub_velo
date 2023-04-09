import rclpy
from rclpy.node import Node
from std_msgs.msg import Header
from builtin_interfaces.msg import Time
from sensor_msgs.msg import PointCloud2

class Sub_and_Repub_Velo(Node):

    def __init__(self):
        super().__init__('velo_pcd_repub')
        self.get_logger().info(f"Republishing /velodyne_points -> /velo_pts_new")

        self.publisher = self.create_publisher(PointCloud2, '/velo_pts_new', 100)
        self._velo_subscription = self.create_subscription(
            PointCloud2, #msg_type
            '/velodyne_points', #topic
            self._velo_listener_callback,  # callback
            1000)


    def _velo_listener_callback(self, msg):
        # print("before stamp", msg.header.stamp)
        # msg.header.stamp = self.get_clock().now().to_msg()
        # print("after stamp", msg.header.stamp)

        # set the header
        header_msg = Header()
        header_msg.stamp = self.get_clock().now().to_msg()
        msg.header = header_msg

        self.publisher.publish(msg)


def main(args=None):
    rclpy.init(args=args)

    velo_pcd_repub = Sub_and_Repub_Velo()
    rclpy.spin(velo_pcd_repub)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    velo_pcd_repub.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
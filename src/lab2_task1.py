
import rclpy
from rclpy.node import Node


class FahadTask1(Node):
    def __init__(self):
        super().__init__('fahad_L2T1')
        self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        self.get_logger().info('Fahad:221678')


def main(args=None):
    rclpy.init(args=args)
    node = FahadTask1()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()


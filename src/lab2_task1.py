
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


from setuptools import setup

package_name = 'lab2'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    install_requires=['setuptools'],
    entry_points={
        'console_scripts': [
            'fahad_l2t1 = lab2.lab2_task1:main',
        ],
    },a
)



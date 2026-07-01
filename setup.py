from setuptools import find_packages, setup

package_name = 'my_robot_controller'

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Nisarg',
    maintainer_email='your_email@gmail.com',
    description='A ROS2 Python package containing basic robot controller nodes for TurtleSim using rclpy.',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            "test_node = my_robot_controller.my_first_node:main",
            "draw_circle_node = my_robot_controller.draw_circle:main"
        ],
    },
)

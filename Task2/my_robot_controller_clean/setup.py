from setuptools import setup

package_name = 'my_robot_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        (
            'share/ament_index/resource_index/packages',
            ['resource/' + package_name],
        ),
        (
            'share/' + package_name,
            ['package.xml'],
        ),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Suchitra S',
    maintainer_email='sec25am076@sairamtap.edu.in',
    description='ROS 2 waypoint navigation using Nav2 Simple Commander',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'waypoint_navigation = my_robot_controller.waypoint_navigation:main',
        ],
    },
)

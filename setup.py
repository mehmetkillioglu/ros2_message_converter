from setuptools import setup, find_packages

package_name = 'ros2_message_converter'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    #packages=find_packages("ros2_message_converter"),  # include all packages under src
    #package_dir={"": "src"},   # tell distutils packages are under src
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Mehmet Killioglu',
    maintainer_email='mehmet.killioglu@tuni.fi',
    description='ROS1 websocket bridge converter',
    license='BSD-3',
    entry_points={
        'console_scripts': [
        ],
    },
)

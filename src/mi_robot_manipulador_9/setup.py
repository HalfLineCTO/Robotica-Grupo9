from setuptools import setup

package_name = 'mi_robot_manipulador_9'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='juan',
    maintainer_email='je.cardona@uniandes.edu.co',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'my_node = mi_robot_manipulador_9.my_node:main',
            'robot_manipulator_teleop = mi_robot_manipulador_9.robot_manipulator_teleop:main',
            'conectionserial = mi_robot_manipulador_9.conectionserial:main'
        ],
    },
)

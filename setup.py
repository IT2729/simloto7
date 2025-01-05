from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'simloto7'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py')),
        (os.path.join('share', package_name), glob('config/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Itsuki Terasawa',
    maintainer_email='s21c1083jp@s.chibakoudai.jp',
    description='simulator of loto7',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'simloto7 = simloto7.simloto7:main',
            'test_subscriber = simloto7.test_subscriber:main',
        ],
    },
)

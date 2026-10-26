
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
    },
)

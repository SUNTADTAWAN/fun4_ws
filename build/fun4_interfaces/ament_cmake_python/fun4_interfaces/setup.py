from setuptools import find_packages
from setuptools import setup

setup(
    name='fun4_interfaces',
    version='0.0.0',
    packages=find_packages(
        include=('fun4_interfaces', 'fun4_interfaces.*')),
)

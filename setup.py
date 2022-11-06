from setuptools import setup, find_packages
import os
path = pathroot = os.path.split(os.path.realpath(__file__))[0]
setup(
    name='stabby',
    version='0.1.0',
    packages=find_packages(),
    entry_points = {
        'console_scripts': ['stabby=simple_tabby.terminal:main'],
    }
)

# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='quapy',
    version='0.3.0',
    description='Python interface for qua-kit scenarios',
    author='Jiaxi Gu',
    author_email='jiaxi.gu@epfl.ch',
    license='MIT',
    install_requires=['matplotlib', 'shapely'],
    packages=['quapy'],
    py_modules=['quapy']
)

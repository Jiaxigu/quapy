# -*- coding: utf-8 -*-

from setuptools import setup


with open('LICENSE') as f:
    license = f.read()

setup(
    name='quapy',
    version='0.1.0',
    description='Python interface for qua-kit scenarios',
    author='Jiaxi Gu',
    author_email='jiaxi.gu@epfl.ch',
    license='MIT',
    install_requires=['matplotlib', 'shapely'],
    packages=['quapy']
    py_modules=['quapy']
)
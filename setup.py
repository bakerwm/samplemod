# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='sample',
    version='0.0.1',
    description='Sample package',
    long_description=readme,
    author='Baker W',
    author_email='me@abc.com',
    url='https://github.com/abc',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)


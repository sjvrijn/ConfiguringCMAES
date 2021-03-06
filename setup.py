from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(
    name='modular-cmaes-framework',
    version='0.0.0',
    description='A modular evolutionary algorithm framework mostly tailored to a modular implementation of the CMA-ES',
    long_description=long_description,
    author='Sander van Rijn',
    author_email='s.j.van.rijn@liacs.leidenuniv.nl',
    packages=['modularcmaes'],
)

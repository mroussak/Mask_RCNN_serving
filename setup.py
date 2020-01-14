from setuptools import setup, find_packages, Extension

#compile_args = ['-fopenmp']
#link_args = ['-fopenmp']
compile_args = []
link_args = []

setup(
    name='mrcnn_serving_ready',
    version=0.1,
    packages=find_packages(),

    author="M. Rusakov",
    author_email="maxime@icardio.ai",
    description="package for serving mask rcnn model."
    )
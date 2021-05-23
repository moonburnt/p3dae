from setuptools import find_packages, setup

VERSION = "0.1.0"

with open("README.md") as f:
    long_description = f.read()

setup(
    name="p3dae",
    version=VERSION,
    description="p3dae - audio effects library for Panda3D",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/moonburnt/p3dae",
    author="moonburnt",
    author_email="moonburnt@disroot.org",
    license="MIT",
    classifiers=["Programming Language :: Python :: 3"],
    packages=find_packages(),
    install_requires=["panda3d>=1.10"],
    )

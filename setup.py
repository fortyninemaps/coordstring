import sys
from numpy import get_include
from setuptools import setup, Extension

extensions = [Extension("coordstring.coordstring", ["coordstring/coordstring.pyx"])]

setup(
    name = "coordstring",
    version = "0.1.2",
    setup_requires = ["numpy>=1.10"],
    install_requires = ["numpy>=1.10"],
    author = "Nat Wilson",
    author_email = "natw@fortyninemaps.com",
    packages = ["coordstring"],
    ext_modules = extensions,
    include_dirs = [get_include()],
    package_data = {"coordstring": ["*.pxd"]},
    url = "https://github.com/fortyninemaps/coordstring",
    description = "Fast collection for geospatial coordinates",
    classifiers = ["Programming Language :: Python :: 2",
                   "Programming Language :: Python :: 2.7",
                   "Programming Language :: Python :: 3",
                   "Programming Language :: Python :: 3.4",
                   "Programming Language :: Python :: 3.5",
                   "Programming Language :: Python :: 3.6",
                   "Topic :: Scientific/Engineering",
                   "Topic :: Scientific/Engineering :: GIS",
                   "License :: OSI Approved :: MIT License"],
    license = "MIT License"
)

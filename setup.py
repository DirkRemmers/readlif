from setuptools import setup
from os import path

# The text of the README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    README = f.read()

# This call to setup() does all the work
setup(
    name="readlif",
    version="0.1.0",
    description="Fast Leica LIF file reader written in python",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/nimne/readlif",
    author="Nick Negretti",
    author_email="nick.negretti@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
    packages=["readlif"],
    include_package_data=True,
    install_requires=["Pillow>=4.2.0"],
    test_suite='unittest2.collector'
)

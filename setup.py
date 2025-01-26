from setuptools import setup, find_packages
from os import path


BASEDIR = path.abspath(path.dirname(__file__))


with open(path.join(BASEDIR, "version.py"), "r", encoding="utf-8") as v:
    for line in v.readlines():
        if line.startswith("__version__"):
            if '"' in line:
                version = line.split('"')[1]
            else:
                version = line.split("'")[1]

with open(path.join(BASEDIR, "README.md"), "r") as f:
    long_description = f.read()


setup(
    name='computerthings',
    version=version,
    license='BSD-3',
    author='DirtyWork Solutions Limited',
    author_email='howdy@dirtywork.solutions',
    url='https://github.com/dirtyworksolutions/computerthings',
    description='Library for representing, and engaging all things computing. Including abstract classes, ',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True
)

import codecs
import io
import os
import re

from setuptools import setup, find_packages

SETUP_DIR = os.path.dirname(os.path.abspath(__file__))


def read(*parts):
    with codecs.open(os.path.join(SETUP_DIR, *parts), 'r') as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


# List all of your Python package dependencies in the
# requirements.txt file
def readfile(filename, split=False):
    with io.open(filename, encoding="utf-8") as stream:
        if split:
            return stream.read().split("\n")
        return stream.read()


readme = readfile("README.rst", split=True)[3:]  # skip title
requires = [
    # minimal requirements listing
    "dataembedder >= 0.3",
    "cmlibs.maths >= 0.3",
    "cmlibs.utils >= 0.4",
    "cmlibs.zinc >= 3.99",
    "cmlibs.widgets >= 2.3",
    "PySide6"
]
source_license = readfile("LICENSE")

setup(
    name='mapclientplugins.dataembedderstep',
    version=find_version('mapclientplugins', 'dataembedderstep', '__init__.py'),
    description='',
    long_description='\n'.join(readme) + source_license,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
    ],
    author='Richard Christie',
    author_email='',
    url='https://github.com/ABI-Software/mapclientplugins.dataembedderstep',
    packages=find_packages(exclude=['ez_setup', ]),
    namespace_packages=['mapclientplugins'],
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
)

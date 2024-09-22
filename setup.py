#
# Copyright 2018 Joachim Lusiardi
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os.path
from setuptools import find_packages, setup


with open("README.md", "r") as fh:
    long_description = fh.read()

def read(rel_path: str) -> str:
    here = os.path.abspath(os.path.dirname(__file__))
    # intentionally *not* adding an encoding option to open
    with open(os.path.join(here, rel_path)) as fp:
        return fp.read()


def get_version(rel_path: str) -> str:
    for line in read(rel_path).splitlines():
        if line.startswith("__version__"):
            # __version__ = "0.9"
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    raise RuntimeError("Unable to find version string.")


setup(
    name='homekit',
    packages=find_packages(exclude=['tests']),
    version=get_version("homekit/version.py"),
    description='Python code to interface HomeKit Accessories and Controllers',
    author='Joachim Lusiardi',
    author_email='pypi@lusiardi.de',
    url='https://github.com/jlusiardi/homekit_python',
# Commented out as download_url is no longer used due to regular misuse and issues
#    download_url='https://github.com/jlusiardi/homekit_python/archive/0.18.0.tar.gz',
    keywords=['HomeKit'],
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Home Automation',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop'
    ],
    install_requires=[
        'hkdf',
        'ed25519',
        'cryptography>=2.5',
        'tlv8>=0.9.0',
    ],
    extras_require={
        'IP': ['zeroconf==0.32.0'],
        'BLE': ['dbus-python', 'gatt', 'pygobject']
    },
    license='Apache License 2.0',
    long_description=long_description,
    long_description_content_type="text/markdown",
)

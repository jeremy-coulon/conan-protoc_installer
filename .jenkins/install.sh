#!/bin/bash

set -e
set -x

virtualenv conan
source conan/bin/activate
pip install --upgrade pip
pip install conan
pip install conan_package_tools

conan user

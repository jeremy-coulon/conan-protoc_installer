#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from conans import ConanFile, CMake


class TestPackageConan(ConanFile):
    settings = "os", "arch"

    def test(self):
        self.run("protoc --version", run_environment=True)
        addressbook = os.path.join(self.source_folder, "addressbook.proto")
        self.run("protoc --cpp_out=. --java_out=. --proto_path={source_folder} {file}".format(source_folder=self.source_folder, file=addressbook), run_environment=True)

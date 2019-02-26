#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil
from conans import ConanFile, tools, AutoToolsBuildEnvironment


class ProtobufConan(ConanFile):
    name = "protoc_installer"
    version = "2.5.0"
    url = "https://github.com/bincrafters/conan-protoc_installer"
    homepage = "https://github.com/protocolbuffers/protobuf"
    topics = ("protocol-buffers", "protocol-compiler", "serialization", "rpc")
    author = "Bincrafters <bincrafters@gmail.com>"
    description = ("protoc is a compiler for protocol buffers definitions files. It can can "
                   "generate C++, Java and Python source code for the classes defined in PROTO_FILE.")
    license = "BSD-3-Clause"
    exports = ["LICENSE.md"]
    settings = "os_build", "arch_build"
    short_paths = True

    def source(self):
        tools.get("{0}/archive/v{1}.tar.gz".format(self.homepage, self.version))
        files = os.listdir("protobuf-%s" % self.version)
        for f in files:
            shutil.move(os.path.join("protobuf-%s" % self.version, f), ".")
        os.rmdir("protobuf-%s" % self.version)
        tools.get("https://github.com/google/googletest/archive/release-1.5.0.tar.gz")
        os.rename("googletest-release-1.5.0", "gtest")

#        cmake.definitions["protobuf_WITH_ZLIB"] = False

    def build(self):
        self.run("./autogen.sh")
        autotools = AutoToolsBuildEnvironment(self)
        autotools.configure(args=["--without-zlib", "--enable-static=false"])
        autotools.make()

    def package(self):
        autotools = AutoToolsBuildEnvironment(self)
        autotools.install()

    def package_info(self):
        self.env_info.PATH.append(os.path.join(self.package_folder, "bin"))
        protoc = "protoc.exe" if self.settings.os_build == "Windows" else "protoc"
        self.env_info.PROTOC_BIN = os.path.normpath(os.path.join(self.package_folder, "bin", protoc))

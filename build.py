#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import platform

from cpt.packager import ConanMultiPackager


if __name__ == "__main__":
    builder = ConanMultiPackager(username="exalead")
    if platform.system() == "Windows":
        builder.add(settings={"compiler": "gcc", "compiler.version": "5", "compiler.libcxx": "libstdc++11", "compiler.exception": "seh", "compiler.threads": "win32"},
                env_vars={"LDFLAGS": "-static -static-libgcc -static-libstdc++"},
                build_requires={"*": ["mingw_installer/1.0@conan/stable", "msys2_installer/20161025@bincrafters/stable"]})
    else:
        builder.add()
    builder.run()

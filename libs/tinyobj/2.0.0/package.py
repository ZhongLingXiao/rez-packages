import platform

name = "tinyobjloader"

version = "2.0.0"

authors = [
    "Syoyo Fujita"
]

description = \
    """
    Tiny but powerful single file wavefront obj loader written in C++03. 
    No dependency except for C++ STL. It can parse over 10M polygons with moderate memory and time.
    """

build_requires = [
    "cmake"
]

requires = []

variants = []

if platform.system() == "Darwin":
    variants.append(["platform-osx", "arch-x86_64"])
elif platform.system() == "Linux":
    variants.append(["platform-linux", "arch-x86_64"])

uuid = "tnyobjloader-2.0.0"


def commands():
    # NOTICE: 
    # User should add these 2 lines in their own cmake file
    # include_directories($ENV{REZ_TINYOBJLOADER_ROOT})

    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")
import platform

name = "filesystem"

version = "0.1.0"

authors = [
    "Wenzel Jakob"
]

description = \
    """
     A simple class for manipulating paths on Linux/Windows/Mac OS
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

uuid = "filesystem-0.1.0"


def commands():
    # NOTICE: 
    # User should add these 2 lines in their own cmake file
    # include_directories($ENV{REZ_FILESYSTEM_ROOT})

    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")
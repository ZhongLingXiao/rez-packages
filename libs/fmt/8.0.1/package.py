import platform

name = "fmt"

version = "8.0.1"

authors = [
    "Victor Zverovich and Jonathan Müller "
]

description = \
    """
    {fmt} is an open-source formatting library providing a fast and safe alternative to C stdio and C++ iostreams.
    """

build_requires = [
    "cmake"
]

requires = [
]

variants = []

if platform.system() == "Darwin":
    variants.append(["platform-osx", "arch-x86_64"])
elif platform.system() == "Linux":
    variants.append(["platform-linux", "arch-x86_64"])

uuid = "fmt-8.0.1"


def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.CMAKE_PREFIX_PATH.append("{root}/lib/cmake/fmt")

    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")
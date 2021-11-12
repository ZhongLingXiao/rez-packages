import platform

name = "eigen"

version = "3.4.0"

authors = [
    "Benoît Jacob (founder) and Gaël Guennebaud (guru)"
]

description = \
    """
    Eigen is a C++ template library for linear algebra: matrices, vectors, numerical solvers, and related algorithms.
    """

build_requires = [
    "cmake"
]

requires = []

variants = []

if platform.system() == "Darwin":
    variants.append(["platform-osx", "arch-x86-64"])
elif platform.system() == "Linux":
    variants.append(["platform-linux", "arch-x86_64"])

uuid = "eigen-3.4.0"


def commands():
    # NOTICE: 
    # User should add these 2 lines in their own cmake file
    #
    # include_directories($ENV{REZ_EIGEN_ROOT})
    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")
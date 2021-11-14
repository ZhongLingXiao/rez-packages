import platform

name = "pugixml"

version = "1.11.4"

authors = [
    "zeux"
]

description = \
    """
    pugixml is a C++ XML processing library, which consists of a DOM-like interface with rich traversal/modification capabilities, 
    an extremely fast XML parser which constructs the DOM tree from an XML file/buffer, and an XPath 1.0 implementation for complex 
    data-driven tree queries. Full Unicode support is also available, with Unicode interface variants and conversions between different 
    Unicode encodings (which happen automatically during parsing/saving).
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

uuid = "pugixml-1.11.4"


def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.CMAKE_PREFIX_PATH.append("{root}/lib/cmake/pugixml")

    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")
name = "kazen"

version = "2021"

authors = [
    "kazen"
]

description = \
    """
    kazen deps for renderer dev.
    """

requires = [
    # TODO: non-std, however is convenient for development. Move these to other suite in final commit. 
    "cmake-3.20",
    "oiio-2.2.15",
    "embree-3.13",
    "pugixml-1.11.4",
    "fmt-8.0.1",
    "tinyobjloader-2.0.0",
    
    # CY2021 standard
    "boost-1.73",
    "python-3.7",
    "openexr-2.4.3",
    "tbb-2021.2",
    "ocio-2.0.1"
]

uuid = "kazen-2021"
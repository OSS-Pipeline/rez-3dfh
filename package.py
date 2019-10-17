name = "3dfh"

version = "1.6.13"

authors = [
    "DNA Research"
]

description = \
    """
    Houdini plugin for the 3Delight renderer.
    """

requires = [
    "3delight_core-{version}".format(version=str(version)),
    "cmake-3+",
    "houdini-17.5+<18.5"
]

variants = [
    ["platform-linux"]
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

uuid = "3dfh-{version}".format(version=str(version))

def commands():
    env.HOUDINI_PATH.append("{root}/houdini/" + str(env.REZ_HOUDINI_MAJOR_VERSION) + "." + str(env.REZ_HOUDINI_MINOR_VERSION))

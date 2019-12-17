name = "3dfh"

version = "1.7.15"

authors = [
    "DNA Research"
]

description = \
    """
    Houdini plugin for the 3Delight renderer.
    """

requires = [
    "3delight-{version}".format(version=str(version)),
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
    import os

    env.HOUDINI_PACKAGE_DIR.append(
        os.path.join(
            str(env.REZ_3DELIGHT_ROOT),
            "houdini",
            str(env.REZ_HOUDINI_MAJOR_VERSION) + "." + str(env.REZ_HOUDINI_MINOR_VERSION),
        )
    )

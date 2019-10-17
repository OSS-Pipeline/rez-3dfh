CMAKE_MINIMUM_REQUIRED(VERSION 3.0)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

# 3DFH
rez_set_archive(
    # This is a relative path from the ${REZ_REPO_PAYLOAD_DIR} environment variable,
    # that is pointing to the root directory where we can find all the archives of the package
    # we can build, using the following hierarchy:
    # "${REZ_REPO_PAYLOAD_DIR}/project_name/archive.what.ever"
    DELIGHT_FOR_HOUDINI_URL 3delight/3DelightNSI-${REZ_BUILD_PROJECT_VERSION}-Linux-x86_64.tar.xz
    https://www.3delight.com/download
)

# The environment variable REZ_TMP_PATH is meant to point to a location such as "/tmp/rez".
set(EXTRACT_DIR $ENV{REZ_TMP_PATH}/3dfh/${REZ_BUILD_PROJECT_VERSION})

# We configure/build/install 3DFH through the ExternalProject_Add macro,
# using three different shell scripts for each of these steps.
# If necessary, it is possible to skip one of these steps by replacing the command
# by "", an empty string.
ExternalProject_Add(
    REZ_DELIGHT_FOR_HOUDINI
    URL ${DELIGHT_FOR_HOUDINI_URL}
    PREFIX 3dfh
    SOURCE_DIR ${EXTRACT_DIR}
    PATCH_COMMAND ""
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ""
    BUILD_COMMAND ""
    INSTALL_COMMAND bash ${CMAKE_SOURCE_DIR}/install.sh ${EXTRACT_DIR}
)

# We use a bogus CMake "install" step in order to be able to properly finish
# and get out of the CMake script.
install(
    CODE
    "execute_process(
        COMMAND echo \"\n[CMAKE] 3DFH-${REZ_BUILD_PROJECT_VERSION} PACKAGE SETUP FINISHED!\n\"
    )"
)

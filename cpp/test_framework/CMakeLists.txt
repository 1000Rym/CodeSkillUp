cmake_minimum_required(VERSION 3.0.0)
SET(PROJECT_NAME "CPPTestFramework")
SET(VERSION "0.1.0")
project(${PROJECT_NAME} VERSION ${VERSION})

include_directories(src)

add_subdirectory(src)
add_subdirectory(lib/googletest)
add_subdirectory(test)
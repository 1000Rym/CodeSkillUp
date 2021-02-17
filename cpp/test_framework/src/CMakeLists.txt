# Recursively add all .h and .cpp files to the list directories.
file(GLOB_RECURSE SOURCES LIST_DIRECTORIES true *.h *.cpp)

# Set binary argument
set(BIN ${CMAKE_PROJECT_NAME})
set(SRC_FILES ${SOURCES})

add_executable(${BIN}_run ${SRC_FILES})

add_library(${BIN}_lib STATIC ${SOURCES})
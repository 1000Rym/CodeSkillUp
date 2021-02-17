set(BIN ${CMAKE_PROJECT_NAME}_test)

# recursively add the header, and source code. 
file(GLOB_RECURSE SOURCES LIST_DIRECTORIES false *.h *.cpp)
add_executable(${BIN} ${SOURCES})
add_test(NAME ${BIN} COMMAND ${BIN})
target_link_libraries(${BIN} PUBLIC ${CMAKE_PROJECT_NAME}_lib gtest)

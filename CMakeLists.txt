cmake_minimum_required(VERSION 3.15)
project(hw-2 CXX)
enable_testing()

add_executable(main main.cpp)

find_program(PYTHON3 python3 REQUIRED)
configure_file(
    "${PROJECT_SOURCE_DIR}/test.py"
    "${CMAKE_BINARY_DIR}/test.py"
    COPYONLY
)
add_test(
    NAME main
    COMMAND ${PYTHON3} -m test ./main
    WORKING_DIRECTORY ${CMAKE_BINARY_DIR}
)

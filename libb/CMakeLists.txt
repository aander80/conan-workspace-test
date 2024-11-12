cmake_minimum_required(VERSION 3.15)
project(libb CXX)

configure_file(
    ${CMAKE_SOURCE_DIR}/src/libb.cpp.in
    ${CMAKE_BINARY_DIR}/src/libb.cpp
)

add_library(libb
    ${CMAKE_BINARY_DIR}/src/libb.cpp
)
target_include_directories(libb PUBLIC include)

set_target_properties(libb PROPERTIES PUBLIC_HEADER "include/libb.h")
install(TARGETS libb)

cmake_minimum_required(VERSION 3.15)
project(liba CXX)

configure_file(
    ${CMAKE_SOURCE_DIR}/src/liba.cpp.in
    ${CMAKE_BINARY_DIR}/src/liba.cpp
)

add_library(liba
    ${CMAKE_BINARY_DIR}/src/liba.cpp
)
target_include_directories(liba PUBLIC include)

set_target_properties(liba PROPERTIES PUBLIC_HEADER "include/liba.h")
install(TARGETS liba)

cmake_minimum_required(VERSION 3.15)
project(app CXX)

find_package(liba REQUIRED)
find_package(libb REQUIRED)

configure_file(
    ${CMAKE_SOURCE_DIR}/src/app.cpp.in
    ${CMAKE_BINARY_DIR}/src/app.cpp
)

add_executable(app
    ${CMAKE_BINARY_DIR}/src/app.cpp
    ${CMAKE_SOURCE_DIR}/src/main.cpp
)
target_link_libraries(app
    liba::liba
    libb::libb
)

install(
    TARGETS app DESTINATION "."
    RUNTIME DESTINATION bin
    ARCHIVE DESTINATION lib
    LIBRARY DESTINATION lib
)

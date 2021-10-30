cmake_minimum_required(VERSION 3.5)

project(opencv_ocr_demo LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++2a")

find_package(OpenCV REQUIRED)

find_package(PkgConfig REQUIRED)
pkg_search_module(TESSERACT REQUIRED tesseract)

add_executable(${PROJECT_NAME} rec.cpp)

include_directories(${TESSERACT_INCLUDE_DIRS})
link_directories(${TESSERACT_LIBRARY_DIRS})
target_link_libraries(${PROJECT_NAME} ${TESSERACT_LIBRARIES})

# directory of opencv headers
include_directories(${OpenCV_INCLUDE_DIRS})
# directory of opencv library
link_directories(${OpenCV_LIBRARY_DIRS})
# opencv libraries
target_link_libraries(${PROJECT_NAME} ${OpenCV_LIBS})

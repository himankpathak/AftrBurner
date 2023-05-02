cmake_minimum_required(VERSION 3.15)
project(aftrburner CXX)




add_library(aftrburner src/aftrburner.cpp)
target_include_directories(aftrburner PUBLIC include)



set_target_properties(aftrburner PROPERTIES PUBLIC_HEADER "include/aftrburner.h")
install(TARGETS aftrburner)

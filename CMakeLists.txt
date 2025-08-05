cmake_minimum_required(VERSION 3.16)
project(cmaps LANGUAGES NONE)

# 查找 Python 解释器
find_package(Python COMPONENTS Interpreter REQUIRED)

# 设置文件路径
set(GENERATE_SCRIPT "${CMAKE_CURRENT_SOURCE_DIR}/generate_files.py")
set(CMAPS_FILE "${CMAKE_CURRENT_SOURCE_DIR}/cmaps/cmaps.py")

# 检查生成脚本是否存在
if(NOT EXISTS ${GENERATE_SCRIPT})
    message(FATAL_ERROR "Generate script not found: ${GENERATE_SCRIPT}")
endif()

# 打印调试信息
message(STATUS "Python executable: ${Python_EXECUTABLE}")
message(STATUS "Generate script: ${GENERATE_SCRIPT}")
message(STATUS "Cmaps file: ${CMAPS_FILE}")

# 自定义目标：生成动态文件
add_custom_target(generate_files
    COMMAND ${Python_EXECUTABLE} ${GENERATE_SCRIPT}
    WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
    COMMENT "Generating cmaps dynamic files..."
    VERBATIM
)

# 自定义命令：生成 cmaps.py
add_custom_command(
    OUTPUT ${CMAPS_FILE}
    COMMAND ${Python_EXECUTABLE} ${GENERATE_SCRIPT}
    DEPENDS ${GENERATE_SCRIPT}
    WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
    COMMENT "Generating cmaps file"
    VERBATIM
)

# 创建一个伪目标来确保文件被生成
add_custom_target(ensure_generated_files ALL
    DEPENDS ${CMAPS_FILE}
)

# 安装 Python 包（scikit-build-core 会处理这个）
# 我们只需要确保生成的文件存在
install(FILES ${CMAPS_FILE} DESTINATION "cmaps/")

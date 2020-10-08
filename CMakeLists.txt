if(NOT ENABLE_GUI)
  return()
endif()

option(BUILD_WRS2019 "Building the WRS2019 files" ON)
if(NOT BUILD_WRS2019)
  return()
endif()

if(UNIX)
  add_custom_target(
    symlink_to_WRS2019 ALL
    COMMAND ${CMAKE_COMMAND} -E create_symlink
    ${CMAKE_CURRENT_SOURCE_DIR} ${CNOID_BINARY_SHARE_DIR}/WRS2019)
endif()

install(DIRECTORY
  model
  project
  script
  test
  DESTINATION ${CNOID_SHARE_SUBDIR}/WRS2019)

add_subdirectory(controller)

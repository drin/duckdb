include_directories(../../../third_party/httplib/)

# To link extensions into DuckDB and auto-load them on startup, we generated an
# include file and a loader function based on the `DUCKDB_EXTENSION_NAMES`
# parameter.


# >> Generate "generated_extension_headers.hpp"
# NOTE: variables to be substituted: `EXT_HEADER_INCLUDES`
get_statically_linked_extensions("${DUCKDB_EXTENSION_NAMES}"
                                 STATICALLY_LINKED_EXTENSIONS)

set(EXT_HEADER_INCLUDES "")
foreach(EXT_NAME IN LISTS STATICALLY_LINKED_EXTENSIONS)
  string(TOUPPER ${EXT_NAME} EXT_NAME_UPPERCASE)
  if(${DUCKDB_EXTENSION_${EXT_NAME_UPPERCASE}_SHOULD_LINK})
    set(EXT_INCLUDE "#include \"${EXT_NAME}_extension.hpp\"")
    set(EXT_HEADER_INCLUDES "${EXT_HEADER_INCLUDES}${EXT_INCLUDE}\n"
  endif()
endforeach()

# Generate the file itself
configure_file(
  generated_extension_headers.hpp.in
  "${PROJECT_BINARY_DIR}/codegen/include/generated_extension_headers.hpp")


# >> Generate "generated_extension_headers.hpp"
# NOTE: variables to be substituted: `EXT_HEADER_INCLUDES`
set(EXT_LOADER_NAME_LIST "")
set(EXT_LOADER_BODY "")
foreach(EXT_NAME IN LISTS STATICALLY_LINKED_EXTENSIONS)
  string(TOUPPER ${EXT_NAME} EXT_NAME_UPPERCASE)
  if(${DUCKDB_EXTENSION_${EXT_NAME_UPPERCASE}_SHOULD_LINK})

    # Assumes lowercase input!
    string(REPLACE "_" ";" EXT_NAME_SPLIT ${EXT_NAME})
    set(EXT_NAME_CAMELCASE "")
    foreach(EXT_NAME_PART IN LISTS EXT_NAME_SPLIT)
      string(SUBSTRING ${EXT_NAME_PART} 0 1 FIRST_LETTER)
      string(SUBSTRING ${EXT_NAME_PART} 1 -1 REMAINDER)
      string(TOUPPER ${FIRST_LETTER} FIRST_LETTER)
      set(EXT_NAME_CAMELCASE "${EXT_NAME_CAMELCASE}${FIRST_LETTER}${REMAINDER}")
    endforeach()

    set(EXT_LOADER_NAME_LIST "${EXT_LOADER_NAME_LIST},\n\t\"${EXT_NAME}\"")
    set(EXT_LOADER_BODY
        "${EXT_LOADER_BODY}\
  if (extension==\"${EXT_NAME}\") {
      db.LoadStaticExtension<${EXT_NAME_CAMELCASE}Extension>();
      return true;
  }
")
  endif()
endforeach()

# trim comma
if(NOT ${EXT_LOADER_NAME_LIST} STREQUAL "")
  string(SUBSTRING ${EXT_LOADER_NAME_LIST} 1 -1 EXT_NAME_VECTOR_INITIALIZER)
endif()

# Load test paths for extensions whose SQLLogicTests need to be registered
set(EXT_TEST_PATH_LIST "")
foreach(EXT_NAME IN LISTS DUCKDB_EXTENSION_NAMES)
  string(TOUPPER ${EXT_NAME} EXT_NAME_UPPERCASE)
  if(${DUCKDB_EXTENSION_${EXT_NAME_UPPERCASE}_LOAD_TESTS})
    set(EXT_TEST_PATH_LIST
        "${EXT_TEST_PATH_LIST},\n\t\"${DUCKDB_EXTENSION_${EXT_NAME_UPPERCASE}_TEST_PATH}\""
    )
  endif()
endforeach()

if(${DISABLE_EXTENSION_LOAD})
  add_definitions(-DDUCKDB_DISABLE_EXTENSION_LOAD)
endif()

if(NOT ${EXT_TEST_PATH_LIST} STREQUAL "")
  string(SUBSTRING ${EXT_TEST_PATH_LIST} 1 -1 EXT_TEST_PATH_INITIALIZER)
endif()

set(GENERATED_CPP_FILE
    ${PROJECT_BINARY_DIR}/codegen/src/generated_extension_loader.cpp)

# Generate the file itself
configure_file(generated_extension_loader.cpp.in "${GENERATED_CPP_FILE}")


# >> Create a target that uses the generated source file
add_definitions(-DGENERATED_EXTENSION_HEADERS=1)

add_library(duckdb_generated_extension_loader OBJECT ${GENERATED_CPP_FILE})
set(generated_loader_obj_files
    $<TARGET_OBJECTS:duckdb_generated_extension_loader>)

# add the generated header file (by adding the directory it was generated into)
include_directories("${PROJECT_BINARY_DIR}/codegen/include/")

if(${EXIT_TIME_DESTRUCTORS_WARNING})
  set(CMAKE_CXX_FLAGS_DEBUG
      "${CMAKE_CXX_FLAGS_DEBUG} -Wno-exit-time-destructors")
endif()

add_library_unity(
  duckdb_main_extension
  OBJECT
  extension_alias.cpp
  extension_helper.cpp
  extension_install.cpp
  extension_load.cpp
  extension_util.cpp)

set(ALL_OBJECT_FILES
    ${ALL_OBJECT_FILES} $<TARGET_OBJECTS:duckdb_main_extension>
    ${ALL_OBJECT_FILES} ${generated_loader_obj_files}
    PARENT_SCOPE)

add_extension_definitions(duckdb_main_extension)

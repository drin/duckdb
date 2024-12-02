# ------------------------------
# Conditional build arguments

if get_option('DEBUG_STACKTRACE')
  add_project_arguments('-DDUCKDB_DEBUG_STACKTRACE', language: 'cpp')
endif


# ------------------------------
# Headers and Sources

# Sources
duckdb_common_sources = [
   'allocator.cpp'
  ,'assert.cpp'
  ,'bind_helpers.cpp'
  ,'box_renderer.cpp'
  ,'cgroups.cpp'
  ,'compressed_file_system.cpp'
  ,'constants.cpp'
  ,'checksum.cpp'
  ,'encryption_state.cpp'
  ,'exception.cpp'
  ,'exception_format_value.cpp'
  ,'extra_type_info.cpp'
  ,'file_buffer.cpp'
  ,'file_system.cpp'
  ,'filename_pattern.cpp'
  ,'fsst.cpp'
  ,'gzip_file_system.cpp'
  ,'hive_partitioning.cpp'
  ,'http_util.cpp'
  ,'pipe_file_system.cpp'
  ,'local_file_system.cpp'
  ,'multi_file_list.cpp'
  ,'multi_file_reader.cpp'
  ,'error_data.cpp'
  ,'opener_file_system.cpp'
  ,'printer.cpp'
  ,'radix_partitioning.cpp'
  ,'re2_regex.cpp'
  ,'random_engine.cpp'
  ,'string_util.cpp'
  ,'enum_util.cpp'
  ,'symbols.cpp'
  ,'render_tree.cpp'
  ,'tree_renderer.cpp'
  ,'types.cpp'
  ,'virtual_file_system.cpp'
  ,'windows_util.cpp'
]


# ------------------------------
# Build targets and artifacts

# >> Include targets
if not get_option('CLANG_TIDY')
  subdir(adbc)
endif

# >> Artifacts from subdirectories
subdir(arrow)
subdir(crypto)
subdir(enums)
subdir(exception)
subdir(operator)
subdir(progress_bar)
subdir(tree_renderer)
subdir(row_operations)
subdir(serializer)
subdir(sort)
subdir(types)
subdir(value_operations)
subdir(vector_operations)

# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_common = static_library('duckdb_common'
  ,duckdb_common_sources
  ,include_directories: [ libduckdb_inc ]
  ,cpp_args           : [ '-Wno-exit-time-destructors' ]
  ,build_by_default   : false
  ,install            : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_common.extract_all_objects()


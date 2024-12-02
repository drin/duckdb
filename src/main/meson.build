# ------------------------------
# Conditional build arguments

# FORCE_QUERY_LOG is empty string if unset
if get_option('FORCE_QUERY_LOG') != ''
  buildarg_val = '-DDUCKDB_FORCE_QUERY_LOG="' + get_option('FORCE_QUERY_LOG') '"'
  add_project_arguments(buildarg_val, language: 'cpp')
endif


# ------------------------------
# Headers and Sources

# Sources
duckdb_main_sources = [
   'appender.cpp'
  ,'attached_database.cpp'
  ,'client_config.cpp'
  ,'client_context_file_opener.cpp'
  ,'client_context.cpp'
  ,'client_context_wrapper.cpp'
  ,'client_data.cpp'
  ,'client_verify.cpp'
  ,'connection_manager.cpp'
  ,'chunk_scan_state.cpp'
  ,'config.cpp'
  ,'connection.cpp'
  ,'database.cpp'
  ,'database_path_and_type.cpp'
  ,'database_manager.cpp'
  ,'db_instance_cache.cpp'
  ,'error_manager.cpp'
  ,'extension.cpp'
  ,'extension_install_info.cpp'
  ,'materialized_query_result.cpp'
  ,'pending_query_result.cpp'
  ,'prepared_statement.cpp'
  ,'prepared_statement_data.cpp'
  ,'profiling_info.cpp'
  ,'relation.cpp'
  ,'query_profiler.cpp'
  ,'query_result.cpp'
  ,'stream_query_result.cpp'
  ,'valid_checker.cpp'
]


# ------------------------------
# Build targets and artifacts

# >> Include targets
if not get_option('CLANG_TIDY')
  subdir(capi)
endif

# >> Artifacts from subdirectories
subdir(extension)
subdir(relation)
subdir(secret)
subdir(settings)
subdir(buffered_data)
subdir(chunk_scan_state)

# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_main = static_library('duckdb_main'
  ,duckdb_main_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_main.extract_all_objects()


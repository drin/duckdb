# NOTE: commit_id and version_str are defined in the top-level build file (meson.build)
add_project_arguments(f'-DDUCKDB_SOURCE_ID="@commid_id@"', language: 'cpp')
add_project_arguments(f'-DDUCKDB_VERSION="@version_str@"', language: 'cpp')

# ------------------------------
# Headers and Sources

# Sources
duckdb_func_table_version_sources = [
   'pragma_version.cpp'
]


# ------------------------------
# Build targets and artifacts


# >> Artifacts from subdirectories


# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_func_table_version = static_library('duckdb_func_table_version'
  ,duckdb_func_table_version_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_func_table_version.extract_all_objects()


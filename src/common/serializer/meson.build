
# ------------------------------
# Headers and Sources

# Sources
duckdb_common_serializer_sources = [
   'binary_serializer.cpp'
  ,'binary_deserializer.cpp'
  ,'buffered_file_reader.cpp'
  ,'buffered_file_writer.cpp'
  ,'memory_stream.cpp'
  ,'serializer.cpp'
]


# ------------------------------
# Build targets and artifacts


# >> Artifacts from subdirectories


# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_common_serializer = static_library('duckdb_common_serializer'
  ,duckdb_common_serializer_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_common_serializer.extract_all_objects()


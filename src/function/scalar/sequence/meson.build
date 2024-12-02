
# ------------------------------
# Headers and Sources

# Sources
duckdb_func_seq_sources = [
   'nextval.cpp'
]


# ------------------------------
# Build targets and artifacts


# >> Artifacts from subdirectories


# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_func_seq = static_library('duckdb_func_seq'
  ,duckdb_func_seq_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_func_seq.extract_all_objects()


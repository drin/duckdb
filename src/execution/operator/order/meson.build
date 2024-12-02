
# ------------------------------
# Headers and Sources

# Sources
duckdb_operator_order_sources = [
   'physical_order.cpp'
  ,'physical_top_n.cpp'
]


# ------------------------------
# Build targets and artifacts


# >> Artifacts from subdirectories


# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_operator_order = static_library('duckdb_operator_order'
  ,duckdb_operator_order_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_operator_order.extract_all_objects()


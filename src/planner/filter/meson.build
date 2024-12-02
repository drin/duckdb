# ------------------------------
# Headers and Sources

# Sources
planner_filter_sources = [
   'conjunction_filter.cpp'
  ,'constant_filter.cpp'
  ,'null_filter.cpp'
  ,'struct_filter.cpp'
  ,'optional_filter.cpp'
]


# ------------------------------
# Build artifacts (libraries)

# An object library (only its objects will be linked against)
objlib_duckdb_planner_filter = static_library('duckdb_planner_filter'
  ,planner_filter_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_planner_filter.extract_all_objects()


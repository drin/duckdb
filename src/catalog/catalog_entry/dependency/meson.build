# ------------------------------
# Headers and Sources

# Sources
dependency_dependent_entry_sources = [
   'dependency_entry.cpp'
  ,'dependency_subject_entry.cpp'
  ,'dependency_dependent_entry.cpp'
]


# ------------------------------
# Build artifacts (libraries)

# An object library (only its objects will be linked against)
objlib_duckdb_dependency_dependent_entry = static_library('duckdb_dependency_dependent_entry'
  ,dependency_dependent_entry_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_dependency_dependent_entry.extract_all_objects()


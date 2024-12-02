
# ------------------------------
# Headers and Sources

# Sources
duckdb_verification_sources = [
   'copied_statement_verifier.cpp'
  ,'external_statement_verifier.cpp'
  ,'fetch_row_verifier.cpp'
  ,'prepared_statement_verifier.cpp'
  ,'deserialized_statement_verifier.cpp'
  ,'statement_verifier.cpp'
  ,'parsed_statement_verifier.cpp'
  ,'no_operator_caching_verifier.cpp'
  ,'unoptimized_statement_verifier.cpp'
]


# ------------------------------
# Build targets and artifacts


# >> Artifacts from subdirectories


# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_verification = static_library('duckdb_verification'
  ,duckdb_verification_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_verification.extract_all_objects()


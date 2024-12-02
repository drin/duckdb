# ------------------------------
# Headers and Sources

# Sources
optimizer_rules_sources = [
   'arithmetic_simplification.cpp'
  ,'case_simplification.cpp'
  ,'comparison_simplification.cpp'
  ,'conjunction_simplification.cpp'
  ,'constant_folding.cpp'
  ,'date_part_simplification.cpp'
  ,'distributivity.cpp'
  ,'empty_needle_removal.cpp'
  ,'enum_comparison.cpp'
  ,'equal_or_null_simplification.cpp'
  ,'in_clause_simplification_rule.cpp'
  ,'join_dependent_filter.cpp'
  ,'like_optimizations.cpp'
  ,'move_constants.cpp'
  ,'ordered_aggregate_optimizer.cpp'
  ,'regex_optimizations.cpp'
  ,'timestamp_comparison.cpp'
]


# ------------------------------
# Build artifacts (libraries)

# An object library (only its objects will be linked against)
objlib_duckdb_optimizer_rules = static_library('duckdb_optimizer_rules'
  ,optimizer_rules_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_optimizer_rules.extract_all_objects()


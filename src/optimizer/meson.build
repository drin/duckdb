# ------------------------------
# Headers and Sources

# Sources
optimizer_sources = [
   'build_probe_side_optimizer.cpp'
  ,'column_binding_replacer.cpp'
  ,'column_lifetime_analyzer.cpp'
  ,'empty_result_pullup.cpp'
  ,'common_aggregate_optimizer.cpp'
  ,'compressed_materialization.cpp'
  ,'cse_optimizer.cpp'
  ,'cte_filter_pusher.cpp'
  ,'deliminator.cpp'
  ,'expression_heuristics.cpp'
  ,'expression_rewriter.cpp'
  ,'filter_combiner.cpp'
  ,'filter_pullup.cpp'
  ,'filter_pushdown.cpp'
  ,'in_clause_rewriter.cpp'
  ,'join_filter_pushdown_optimizer.cpp'
  ,'optimizer.cpp'
  ,'regex_range_filter.cpp'
  ,'remove_duplicate_groups.cpp'
  ,'remove_unused_columns.cpp'
  ,'statistics_propagator.cpp'
  ,'limit_pushdown.cpp'
  ,'topn_optimizer.cpp'
  ,'unnest_rewriter.cpp'
  ,'sampling_pushdown.cpp'
]


# ------------------------------
# Build artifacts (libraries)

# >> Artifacts from subdirectories
subdir('compressed_materialization')
subdir('join_order')
subdir('matcher')
subdir('pullup')
subdir('pushdown')
subdir('rule')
subdir('statistics')


# An object library (only its objects will be linked against)
objlib_duckdb_optimizer = static_library('duckdb_optimizer'
  ,optimizer_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_optimizer.extract_all_objects()


//===----------------------------------------------------------------------===//
//                         DuckDB
//
// duckdb/common/arrow/arrow_wrapper.hpp
//
//
//===----------------------------------------------------------------------===//

#pragma once
#include "duckdb/common/arrow/arrow.hpp"
#include "duckdb/common/helper.hpp"

//! Here we have the internal duckdb classes that interact with Arrow's Internal Header (i.e., duckdb/commons/arrow.hpp)
namespace duckdb {

  // Type forwards
  class QueryResult;
  class DataChunk;


  struct ArrowSchemaWrapper {
    // Attributes
    ArrowSchema arrow_schema;

    // Constructors/Destructors
    ~ArrowSchemaWrapper();
    ArrowSchemaWrapper() { arrow_schema.release = nullptr; }
  };


  struct ArrowArrayWrapper {
    ArrowArray arrow_array;

    ~ArrowArrayWrapper();

    ArrowArrayWrapper() {
      arrow_array.length  = 0;
      arrow_array.release = nullptr;
    }

    ArrowArrayWrapper(ArrowArrayWrapper &&other) noexcept : arrow_array(other.arrow_array) {
      other.arrow_array.release = nullptr;
    }
  };


  struct ArrowArrayStreamWrapper {
    // Attributes
    ArrowArrayStream arrow_array_stream;
    int64_t          number_of_rows;

    // Constructors/Destructors
    virtual ~ArrowArrayStreamWrapper();
    ArrowArrayStreamWrapper() { arrow_array_stream.release = nullptr; }

    // Methods
    virtual shared_ptr<ArrowArrayWrapper> GetNextChunk();
    void        GetSchema(ArrowSchemaWrapper &schema);
    const char* GetError();
  };

  struct ArrowUtil {
    static bool TryFetchChunk( ChunkScanState&  scan_state
                              ,ClientProperties options
                              ,idx_t            chunk_size
                              ,ArrowArray*      out
                              ,idx_t&           result_count
                              ,ErrorData&       error);

    static idx_t FetchChunk( ChunkScanState&  scan_state
                            ,ClientProperties options
                            ,idx_t            chunk_size
                            ,ArrowArray*      out);

    private:
      static bool TryFetchNext( QueryResult&           result
                               ,unique_ptr<DataChunk>& out
                               ,ErrorData&             error);
  };

} // namespace duckdb


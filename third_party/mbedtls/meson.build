# >> Dependencies


# >> Conditional build args

# hide global symbols
cppargs_mbedtls = ['-fvisibility=hidden', '-Dc_std=c99']

# disable warnings
if cmp_name == 'msvc'
  cppargs_mbedtls += '/W0'

elif cmp_name == 'clang' or cmp_name == 'gcc'
  cppargs_mbedtls += '-w'

endif


# >> Headers and sources

mbedtls_sources = [
   'mbedtls_wrapper.cpp'
  ,'library' / 'aes.cpp'
  ,'library' / 'aria.cpp'
  ,'library' / 'asn1parse.cpp'
  ,'library' / 'base64.cpp'
  ,'library' / 'bignum.cpp'
  ,'library' / 'camellia.cpp'
  ,'library' / 'cipher.cpp'
  ,'library' / 'cipher_wrap.cpp'
  ,'library' / 'constant_time.cpp'
  ,'library' / 'entropy.cpp'
  ,'library' / 'entropy_poll.cpp'
  ,'library' / 'gcm.cpp'
  ,'library' / 'md.cpp'
  ,'library' / 'oid.cpp'
  ,'library' / 'pem.cpp'
  ,'library' / 'pk.cpp'
  ,'library' / 'pk_wrap.cpp'
  ,'library' / 'pkparse.cpp'
  ,'library' / 'platform_util.cpp'
  ,'library' / 'rsa.cpp'
  ,'library' / 'rsa_alt_helpers.cpp'
  ,'library' / 'sha1.cpp'
  ,'library' / 'sha256.cpp'
  ,'library' / 'sha512.cpp'
]


# >> Build targets

# Include targets
libmbedtls_inc = include_directories('include')

# Library targets
libmbedtls = static_library('duckdb_mbedtls'
  ,mbedtls_sources
  ,include_directories: [ libmbedtls_inc ]
  ,cpp_args           : cppargs_mbedtls
  ,install            : true
)


# >> Final artifacts
# Accumulate into list of includes for third-party libs (external projects)
ep_inc += [libmbedtls_inc]

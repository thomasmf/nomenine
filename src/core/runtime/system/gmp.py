

APPEND_INIT( """
  mp_set_memory_functions( for_gmp_malloc, for_gmp_realloc, for_gmp_free ) ;
""" )

FUNCTION( 'void* for_gmp_malloc( size_t size )', """
  return nom_malloc( size ) ;
""" )

FUNCTION( 'void* for_gmp_realloc( void* ptr, size_t old_size, size_t new_size )', """
  return nom_realloc( ptr, new_size ) ;
""" )

FUNCTION( 'void for_gmp_free( void* ptr, size_t size )', '' )




REGISTER_FLAG( 'no_gc', 'disables garbage collection' )


FUNCTION( 'void* nom_malloc( n_integer size )', """

  $DISABLED( no_gc,
    void* data = $CAST(void*,GC_MALLOC( size )) ;
  )

  $ENABLED( no_gc,
    void* data = $CAST(void*, malloc( size )) ;
  )

  $ERROR( "Out of memory!", $CAST(n_boolean,data != 0) ) ;
  return data ;
""" )


FUNCTION( 'void* nom_realloc( void* old, n_integer size )', """

  $DISABLED( no_gc,
    void* data = $CAST(void*,GC_REALLOC( old, size )) ;
  )

  $ENABLED( no_gc,
    void* data = $CAST( void*, realloc( old, size ) ) ;
  )

  $ERROR( "Out of memory!", $CAST(n_boolean, data != 0) ) ;
  return data ;
""" )


FUNCTION( 'n_string nom_gcstring( n_string src )', """
  n_integer buffer_len = strlen( src ) + 1 ;
  n_string dest = $CAST(n_string,nom_malloc( buffer_len )) ;
  strcpy( dest, src ) ;
  free( src ) ;
  return dest ;
""" )


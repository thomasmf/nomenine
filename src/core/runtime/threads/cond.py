

FUNCTION( 'void nom_cond_finalizer( void* obj, void* cd )', """
  $ERROR( "Failed to destroy cond.", !pthread_cond_destroy( $C(COND,obj)->data ) ) ;
""" )

FUNCTION( 'COND nom_cond_new()', """
  pthread_cond_t* c = $CAST(pthread_cond_t*,nom_malloc( sizeof( pthread_cond_t ) )) ;
  pthread_cond_init( c, NULL ) ;

  COND cond = COND_new( c ) ;

  $DISABLED( no_gc,
    GC_register_finalizer( (void*)cond, nom_cond_finalizer, NULL, 0, 0 ) ;
  )

  return cond ;
""" )


FUNCTION( 'void nom_cond_wait( COND cond, MUTEX mutex )', """
  $ERROR( "Failed to wait for cond", !pthread_cond_wait( cond->data, mutex->data ) ) ;
""" )

FUNCTION( 'void nom_cond_signal( COND cond )', """
  $ERROR( "Failed to signal cond", !pthread_cond_signal( cond->data ) ) ;
""" )

FUNCTION( 'void nom_cond_broadcast( COND cond )', """
  $ERROR( "Failed to broadcast cond", !pthread_cond_broadcast( cond->data ) ) ;
""" )


OBJECT( 'COND',
  attributes = [
    A( 'pthread_cond_t*', 'data' ),
  ]
)


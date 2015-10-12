

FUNCTION( 'void nom_mutex_finalizer( void* obj, void* cd )', """
  $ERROR( "Failed to destroy mutex.", !pthread_mutex_destroy( $C(MUTEX,obj)->data ) ) ;
""" )

FUNCTION( 'MUTEX nom_mutex_new()', """
  pthread_mutex_t* m = $CAST(pthread_mutex_t*,nom_malloc( sizeof( pthread_mutex_t ) )) ;

//  pthread_mutexattr_t attr ;
//  pthread_mutexattr_init( &attr ) ;
//  pthread_mutexattr_settype( &attr, PTHREAD_MUTEX_ADAPTIVE_NP ) ;
//  pthread_mutex_init( m, &attr ) ;

  pthread_mutex_init( m, NULL ) ;

  MUTEX mutex = MUTEX_new( m ) ;

  $DISABLED( no_gc,
    GC_register_finalizer( (void*)mutex, nom_mutex_finalizer, NULL, 0, 0 ) ;
  )

  return mutex ;
""" )


FUNCTION( 'void nom_mutex_lock( MUTEX mutex )', """
  $ERROR( "Failed to lock mutex.", !pthread_mutex_lock( $C(MUTEX,mutex)->data ) ) ;
""" )

FUNCTION( 'void nom_mutex_unlock( MUTEX mutex )', """
  $ERROR( "Failed to unlock mutex.", !pthread_mutex_unlock( $C(MUTEX,mutex)->data ) ) ;
""" )


OBJECT( 'MUTEX',
  attributes = [
    A( 'pthread_mutex_t*', 'data' ),
  ]
)

OBJECT( 'MUTEXED',
  attributes = [
    A( 'MUTEX', 'mutex' ),
  ]
)



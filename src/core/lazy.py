

def LAZY( t, expression ) :
  return PRE( """
    ( {
      static pthread_mutex_t _lock_ = PTHREAD_MUTEX_INITIALIZER ;
      static """ + t + """ _object_ = NULL ;
//      if ( _object_ == NULL ) {
        pthread_mutex_lock( &_lock_ ) ;
        if ( _object_ == NULL ) {
          _object_ = ( """ + expression + """ ) ;
        }
        pthread_mutex_unlock( &_lock_ ) ;
//      }
      _object_ ;
    } )
  """ )



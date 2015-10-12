

def LOG( o ) :
  return PRE( '( nom_log( ' + build_c_string( o ) + ', $CA(' + o + ') ) )' )

def OUT( s = '' ) :
  return PRE( '( printf( \"%04zd\\t%s\\n\", log_counter(), ' + build_c_string( s ) + ' ) )' )

def DUMP( o ) :
  return PRE( '( nom_dump( $CA(' + o + ') ) )' )


FUNCTION( 'void nom_run( n_string file_name )', """
  ANY result = $CALL( evaluate_ANY, $CA(STRING_new( read_source( file_name ) )), ROOT_SCOPE_single() ) ;
  $LOG( result ) ;
""" )

FUNCTION( 'n_string read_source( n_string filename )', """
  n_integer size ;
  n_string result ;
  FILE* f = fopen( filename, "r" ) ;
  if ( f == NULL ) {
    printf( \"IO error: file '%s' not found.\\n\", filename ) ; exit( 1 ) ;
  }
  fseek( f, 0, SEEK_END ) ; size = ftell( f ) ; fseek( f, 0, SEEK_SET ) ;
  result = $CAST( n_string, malloc( size + 1 ) ) ;
  if ( size != fread( result, sizeof( n_character ), size, f ) ) {
    printf( \"IO error: cannot read from file '%s'.\\n\", filename ) ; exit( 1 ) ;
  }
  fclose( f ) ;
  result[ size ] = 0 ;
  return result ;
""" )

FUNCTION( 'n_integer log_counter()', """
  static pthread_mutex_t lock = PTHREAD_MUTEX_INITIALIZER ;
  pthread_mutex_lock( &lock ) ;
  static n_integer counter = 0 ;
  counter += 1 ;
  n_integer x = counter ;
  pthread_mutex_unlock( &lock ) ;
  return x ;
""" )

FUNCTION( 'ANY nom_log( n_string message, ANY object )', """
  printf( \"%04zd\\t%s\\t%s\\n\", log_counter(), message, $DUMP( object ) ) ;
  return object ;
""" )

FUNCTION( 'n_string nom_dump( ANY object )', """
  if ( object ) {
    return object->dump( object ) ;
  } else {
    return "NULL" ;
  }
""" )




REGISTER_FLAG( 'type_checks', 'enable precautionary typechecks' )


def IFLET_SUBSTRUCT( n, t, v ) :
  return PRE( 'if ( !$IS_SUBSTRUCT( ' + t + ', ' + v + ' ) ) break ; ' + t + ' ' + n + ' = $CAST( ' + t + ', ' + v + ' ) ; (void)' + n + ' ;' )

def IS_SUBSTRUCT( t, v ) :
  return PRE( '( TEST_SUBSTRUCT__' + t + '( ' + v + ' ) )' )


def IFLET( n, t, v ) :
  return PRE( 'if ( !$IS( ' + t + ', ' + v + ' ) ) break ; ' + t + ' ' + n + ' = $CAST( ' + t + ', ' + v + ' ) ; (void)' + n + ' ;' )

def IS( t, v ) :
  return PRE( '( ' + t + '_objective == ' + v + '->objective )' )

def CAST( t, o ) :
  return PRE( '( (' + t + ')( ' + o + ' ) )' )

def C( t, o ) :
  return ' '.join( [
    ENABLED( 'type_checks', '( $CAST( ' + t + ', nom_test_substruct( TEST_SUBSTRUCT__' + t + ', $CAST(ANY,' + o + '), "' + t + '",__FILE__, __LINE__ ) ) )' ),
    DISABLED( 'type_checks', CAST( t, o ) ),
  ] )

def CA( o ) :
  return C( 'ANY', o )

TRUE = 1
FALSE = 0


FUNCTION( 'ANY nom_test_substruct( n_boolean (*test_function)( ANY object ), ANY object, n_string expected_type, n_string source_file, n_integer source_line )', """
  if ( !nom_pix_to_objective_verify( object ) ) {
    printf( \"System error in file '%s' at line %zd. Pix and objective does not match for object of type %s.\\n\", source_file, source_line, expected_type ) ;
    exit( EX_SOFTWARE ) ;
  }
  if ( !test_function( object ) ) {
    printf( \"System error in file '%s' at line %zd. Expected %s.\\n\", source_file, source_line, expected_type ) ;
    printf( \"\\tObject %s is of incorrect type.\\n\", $DUMP( object ) ) ;
    exit( EX_SOFTWARE ) ;
  }
  return ( object ) ;
""" )

FUNCTION( 'void nom_error( n_string message, n_boolean value, n_string source_file, n_integer source_line )', """
  if ( !value ) {
    printf( \"System error in file '%s' at line %zd: %s\\n\", source_file, source_line, message ) ;
    exit( EX_SOFTWARE ) ;
  }
  return ;
""" )


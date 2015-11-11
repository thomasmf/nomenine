

REGISTER_FLAG( 'informative_errors', 'enable informative error objects passed with fail' )


ROOT_SCOPE_METHOD(
  MS( ARG( CW( 'dump' ), CG( 'ANY', 'object' ) ), """
    JUMP__return_ANY( CONTEXT, CONTEXT, $CA(STRING_new( $DUMP( PARAM_object ) )) ) ;
  """ )
)


def ERROR( s, v = '$FALSE' ) :
  return PRE( 'nom_error( ( ' + s + ' ), $CAST( n_boolean, ( ' + v + ' ) ), __FILE__, __LINE__ )' )

def NOT_IMPLEMENTED() :
  return ERROR( '"Not implemented"', str( FALSE ) )


FUNCTION( 'void nom_fail( ANY context, n_string message, ANY cause )', """
  JUMP__fail_ANY( context, context, nom_error_new( context, message, cause )  ) ;
""" )

FUNCTION( 'ANY nom_error_new( ANY context, n_string message, ANY cause )', """
  $ENABLED( informative_errors,
    return $CA(ERROR_new( message, context, cause )) ;
  )
  $DISABLED( informative_errors,
    return $NONE ;
  )
""" )


OBJECT( 'ERROR',
  attributes = [
    A( 'n_string', 'message' ),
    A( 'ANY', 'context' ),
    A( 'ANY', 'cause'),
  ],
  methods = [
    MS( ARG( CW( 'log' ) ), """
      printf( "\\tERROR:\\t\\t%s\\n", ACTION->message ) ;
      JUMP__log( CONTEXT, ACTION->cause ) ;
    """ ),
  ],
  dump = D( 'message:\\"%s\\" context:%s', 'object->message, $DUMP( object->cause )' )
)



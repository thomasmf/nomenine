

def RECEIVER() :
  return PRE( 'FRAME__CALL_C_FUNCTION_RECEIVER RECEIVER = FRAME__CALL_C_FUNCTION_RECEIVER_new( $CA(CALL_C_FUNCTION_DEADEND_new()), $NONE ) ;' )

def CALL( m, *p ) :
  return PRE( """
    ( {
      $RECEIVER() ;
      JUMP__""" + m + """( $CA(RECEIVER), """ + ', '.join( p ) + """ ) ;
      RECEIVER->result ;
    } )
  """ )


FRAME( 'CALL_C_FUNCTION_RECEIVER',
  attributes = [
    A( 'ANY', 'result' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      ACTION->result = PARAM_value ;
    """ ),
    MS( ARG( CW( 'fail' ), CG( 'ANY', 'error' ) ), """
      $LOG( PARAM_error ) ;
      $LOG( CONTEXT ) ;
      JUMP__log( $CA(IGNORER_single()), nom_error_new( CONTEXT, "Call failed", PARAM_error ) ) ;
      $ERROR( nom_format_string( "Exiting" ), $FALSE ) ;
    """ ),
  ]
)

OBJECTIVE( 'CALL_C_FUNCTION_DEADEND',
 objective = """
    $ERROR( nom_format_string( "Call failed with unrecognized message to context.\\nThe message was:\\n\\t %s", $DUMP( THAT ) ), $FALSE ) ;
  """
)


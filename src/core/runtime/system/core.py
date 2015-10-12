


TEST( """""" )
TEST( """ none """ )


FRAME( 'ROOT',
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      $OUT( return to root ) ;
      $LOG( PARAM_value ) ;
//      LOG( CONTEXT ) ;
    """ ),
    MS( ARG( CW( 'fail' ), CG( 'ANY', 'error' ) ), """
      $OUT( fail to root ) ;
      JUMP__log( $CA( IGNORER_single() ), PARAM_error ) ;
    """ ),
  ]
)


OBJECTIVE( 'ROOT_DEADEND',
  objective = """
    $OUT( unrecognized message to root ) ;
    $LOG( CONTEXT ) ;
    $LOG( THAT ) ;
  """
)


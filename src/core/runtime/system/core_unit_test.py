

TEST( """""" )
TEST( """ Closure @ () [ : This should N/A !!! ] asdf """ )
TEST( """ This should fail !!! """ )


FRAME( 'CORE_UNIT_TEST',
  attributes = [
    A( 'n_string', 'expression_string' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      printf( "\\tOk\\t\\t[ %s ]\\n", ACTION->expression_string ) ;
    """ ),
    MS( ARG( CW( 'fail' ), CG( 'ANY', 'error' ) ), """
      printf( "\\tFail\\t\\t[ %s ]\\n", ACTION->expression_string ) ;
      JUMP__log( $CA(IGNORER_single()), nom_error_new( CONTEXT, "Core unit test failed", PARAM_error ) ) ;
    """ ),
  ]
)

OBJECTIVE( 'CORE_UNIT_TEST_DEADEND',
  attributes = [
    A( 'n_string', 'expression_string' ),
  ],
  objective =  """
    printf( "\\tN/A\\t\\t[ %s ]\\n\\t\\t\\t%s\\n", ACTION->expression_string, $DUMP( THAT ) ) ;
  """
)


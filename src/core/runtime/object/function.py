

ROOT_SCOPE_METHOD( MD( 'Function', 'FUNCTION_FACTORY_single()' ) )


TEST( """ Function @ x ( Closure @ () [ . 1234 ] ) x == 1234 """ )
TEST( """ Function @ ( Pattern @ ( . [ x ] flatten () ) ) ( Closure @ () [ . 2345 ] ) x == 2345 """ )
TEST( """ Function @ ( Pattern @ ( . [ x ( Integer ) ] flatten () ) ) ( Closure @ () [ : that * ( : that ) ] ) x 9 == 81 """ )
TEST( """ Function @ ( Pattern @ ( . [ x ( Shape @ a ( Integer ) ) ( Shape @ b ( Integer ) ) ] flatten () ) ) ( Closure @ () [ : that a * ( : that b ) ] ) x 8 5 == 40 """ )
TEST( """ . [ if [ f1 ] then [ . 6 ] else [ . 9 ] ] evaluate ( Union @ ( . [ ( Function @ f1 ( Closure @ () [FAIL] ) ) ( Function @ f1 ( Closure @ () [ . 1 ] ) ) () ] flatten () ) ) == 9 """ )


OBJECT( 'FUNCTION_FACTORY',
  methods = [
    MS( ARG( CW( '@' ), CG( 'CLAUSE', 'clause' ), CG( 'ANY', 'action' ) ), """
      JUMP__return_ANY( CONTEXT, CONTEXT, $CA(FUNCTION_new( PARAM_clause, PARAM_action )) ) ;
    """ ),
  ]
)

OBJECTIVE( 'FUNCTION',
  attributes = [
    A( 'ANY', 'clause' ),
    A( 'ANY', 'action' ),
  ],
  objective = """
    JUMP__consume_LIST( $CA(FRAME__TYPE_0_new( CONTEXT, ACTION )), ACTION->clause, THAT ) ;
  """,
  dump = D( 'clause:%s', '$DUMP( object->clause )' )
)

FRAME( 'TYPE_0',
  attributes = [
    A( 'FUNCTION', 'function' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """

      $OPT(
        $IFLET( element, ELEMENT, PARAM_value ) ;
        nom_do_sync( FRAME__TASK_new( $CA(FRAME__ACTION_new( ACTION->parent, element->next )), ACTION->function->action, element->value ) ) ;
      )

      $OPT(
        $IFLET( array, ARRAY_MUTABLE_NOLOCK, PARAM_value ) ;
        $ARRAY_MUTABLE_NOLOCK__NONEMPTY( ACTION->parent, array ) ;
        nom_do_sync( FRAME__TASK_new( $CA(FRAME__ACTION_new( ACTION->parent, $CA(nom_array_mutable_nolock_next( array )) )), ACTION->function->action, nom_array_mutable_nolock_value( array ) ) ) ;
      )

      REFERENCE reference = nom_reference_new( $NONE ) ;
      JUMP__value( $CA(FRAME__SPLIT_new( $CA(FRAME__TYPE_1_new( ACTION->parent, ACTION->function, reference )), PARAM_value, reference )), PARAM_value ) ;
    """ ),
  ]
)

FRAME( 'TYPE_1',
  attributes = [
    A( 'FUNCTION', 'function' ),
    A( 'REFERENCE', 'value' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      nom_do_sync( FRAME__TASK_new( $CA(FRAME__ACTION_new( ACTION->parent, PARAM_value )), ACTION->function->action, ACTION->value->value ) ) ;
    """ ),
  ]
)

FRAME( 'ACTION',
  attributes = [
    A( 'ANY', 'phrase' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      JUMP__return_ANY( ACTION->parent, ACTION->parent, $CA(ELEMENT_new( PARAM_value, ACTION->phrase )) ) ;
    """ ),
    MS( ARG( CW( 'fail' ), CG( 'ANY', 'error' ) ), """
      JUMP__callerContext( $CA(FRAME__FUNCTION_FAIL_new( ACTION->parent, PARAM_error )), ACTION->parent ) ;
    """ ),
  ],
  dump = D( '%s ', '$DUMP( object->parent )' )
)

FRAME( 'FUNCTION_FAIL',
  attributes = [
    A( 'ANY', 'error' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      JUMP__fail_ANY( ACTION->parent, PARAM_value, nom_error_new( CONTEXT, "Function failed", ACTION->error ) ) ;
    """ ),
  ]
)




ROOT_SCOPE_METHOD(
  MD( 'Lazy', 'LAZY_FACTORY_single()' ),
  MO( """
    function lazy ( :: action ( List ) ) [
      Lazy @ ( Stub @ ( : this ) ( : that action ) )
    ]
  """ )
)


TEST( """ . ( Lazy @ ( Stub @ () [ . 3 * 10000 ] ) ) + 1000 + ( Lazy @ ( Stub @ () [ . 10 * 32 ] ) ) == 31320 """ )
TEST( """ . ( lazy [ . 3 * 10000 ] ) + 1000 + ( lazy [ . 10 * 32 ] ) == 31320 """ )


FUNCTION( 'LAZY nom_lazy_new( ANY action )', """
  return LAZY_new( action, nom_promise_new() ) ;
""" )


OBJECT( 'LAZY_FACTORY',
  methods = [
    MS( ARG( CW( '@' ), CG( 'ANY', 'action' ) ), """
      LAZY lazy = nom_lazy_new( PARAM_action ) ;
      JUMP__return_ANY( CONTEXT, CONTEXT, $CA(lazy) ) ;
    """ ),
  ]
)

OBJECTIVE( 'LAZY',
  attributes = [
    A( 'ANY', 'action' ),
    A( 'PROMISE', 'promise' ),
  ],
  objective = """
    $PROMISE_START( ACTION->promise,
      nom_do_sync( FRAME__TASK_new( $CA(FRAME__LAZY_FACTORY_RESULT_new( CONTEXT, ACTION->promise, THAT )), ACTION->action, $NONE ) ) ;
      return ;
    )
    nom_promise_apply( CONTEXT, ACTION->promise, THAT ) ;
  """
)

FRAME( 'LAZY_FACTORY_RESULT',
  attributes = [
    A( 'PROMISE', 'promise' ),
    A( 'ANY', 'that' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      nom_promise_set_fine( ACTION->promise, PARAM_value ) ;
      nom_promise_apply( ACTION->parent, ACTION->promise, ACTION->that ) ;
    """ ),
    MS( ARG( CW( 'fail' ), CG( 'ANY', 'error' ) ), """
      nom_promise_set_fail( ACTION->promise, nom_error_new( ACTION->parent, "Failed to produce lazy object", PARAM_error ) ) ;
      nom_promise_apply( ACTION->parent, ACTION->promise, ACTION->that ) ;
    """ ),
  ]
)




ROOT_SCOPE_METHOD(
  MD( 'Avid', 'AVID_FACTORY_single()' ),
 
  MC( ARG( CW( 'avid' ), CG( 'LIST', 'phrase' ) ), """
    $NOM( CONTEXT, PARAM_phrase,
      Avid @ ( Stub @ ( : this ) ( : that ) )
    ) ;
  """ )
)


TEST( """ . ( avid [ . 3 * 33 ] ) + 1 == 100 """ )


FUNCTION( 'ANY nom_avid_new( ANY context, ANY action )', """
  PROMISE promise = nom_promise_new() ;

  $PROMISE_START( promise,
    nom_do_async( FRAME__TASK_new( $CA(FRAME__AVID_FACTORY_RESULT_new( context, promise )), action, $NONE ) ) ;
  )

  return $CA(promise) ;
""" )


OBJECT( 'AVID_FACTORY',
  methods = [
    MS( ARG( CW( '@' ), CG( 'ANY', 'action' ) ), """
      JUMP__return_ANY( CONTEXT, CONTEXT, nom_avid_new( CONTEXT, PARAM_action ) ) ;
    """ ),
  ]
)

FRAME( 'AVID_FACTORY_RESULT',
  attributes = [
    A( 'PROMISE', 'promise' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      nom_promise_set_fine( ACTION->promise, PARAM_value ) ;
    """ ),
    MS( ARG( CW( 'fail' ), CG( 'ANY', 'error' ) ), """
      nom_promise_set_fail( ACTION->promise, nom_error_new( ACTION->parent, "Failed to produce avid object", PARAM_error ) ) ;
    """ ),
  ]
)


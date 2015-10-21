

ROOT_SCOPE_METHOD( MD( 'Synchronized', 'SYNCHRONIZED_FACTORY_single()' ) )


TEST( """ let t ( Synchronized @ 100 ) [ do [ t ] t + 1 ] == 101 """ )


OBJECT( 'SYNCHRONIZED_FACTORY',
  methods = [
    MS( ARG( CW( '@' ), CG( 'ANY', 'object' ) ), """
      JUMP__return_ANY( CONTEXT, CONTEXT, $CA(SYNCHRONIZED_new( nom_lock_new(), PARAM_object )) ) ;
    """ ),
  ]
)

OBJECTIVE( 'SYNCHRONIZED',
  inherit = [ 'LOCKABLE' ],
  attributes = [
    A( 'ANY', 'object' ),
  ],
  objective = """
    nom_lock_lock( ACTION->lock ) ;
    nom_do_sync( FRAME__TASK_new( $CA(FRAME__SYNCHRONIZED_new( CONTEXT, ACTION )), ACTION->object, THAT ) ) ;
  """
)

FRAME( 'SYNCHRONIZED',
  attributes = [
    A( 'SYNCHRONIZED', 'synchronized' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      nom_lock_unlock( ACTION->synchronized->lock ) ;
      JUMP__return_ANY( ACTION->parent, ACTION->parent, PARAM_value ) ;
    """ ),
    MS( ARG( CW( 'fail' ), CG( 'ANY', 'error' ) ), """
      nom_lock_unlock( ACTION->synchronized->lock ) ;
      nom_fail( ACTION->parent, "Generator failed", $NONE ) ;
    """ ),
  ]
)



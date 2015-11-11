

ROOT_SCOPE_METHOD(
  MD( 'Closure', 'CLOSURE_FACTORY_single()' ),
  MC( ARG( CW( 'closure' ), CG( 'LIST', 'phrase' ) ), """
    $NOM( CONTEXT, PARAM_phrase,
      Closure @ ( : this ) ( : that )
    ) ;
  """ )
)


FUNCTION( 'ANY nom_start_object_new( ANY context, ANY scope )', """
  return $CA(FRAME__SCOPE_new( scope, context )) ;
""" )


OBJECT( 'CLOSURE_FACTORY',
  methods = [
    MS( ARG( CW( '@' ), CG( 'ANY', 'scope' ), CG( 'LIST', 'phrase' ) ), """
      JUMP__return_ANY( CONTEXT, CONTEXT, $CA(CLOSURE_new( PARAM_scope, PARAM_phrase )) ) ;
    """ ),
  ]
)

OBJECTIVE( 'CLOSURE',
  attributes = [
    A( 'ANY', 'scope' ),
    A( 'ANY', 'phrase' ),
  ],
  objective = """
    JUMP__evaluate_ANY( CONTEXT, ACTION->phrase, nom_start_object_new( CONTEXT, ACTION->scope ) ) ;
  """,
  dump = D( '%s', '$DUMP( object->phrase )' )
)



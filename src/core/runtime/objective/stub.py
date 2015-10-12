

ROOT_SCOPE_METHOD( MD( 'Stub', 'STUB_FACTORY_single()' ) )


OBJECT( 'STUB_FACTORY',
  methods = [
    MS( ARG( CW( '@' ), CG( 'ANY', 'scope' ), CG( 'LIST', 'phrase' ) ), """
      JUMP__return_ANY( CONTEXT, CONTEXT, $CA(STUB_new( PARAM_scope, PARAM_phrase )) ) ;
    """ ),
  ]
)

OBJECTIVE( 'STUB',
  attributes = [
    A( 'ANY', 'scope' ),
    A( 'ANY', 'phrase' ),
  ],
  objective = """
    JUMP__evaluate_ANY( CONTEXT, ACTION->phrase, ACTION->scope ) ;
  """
)


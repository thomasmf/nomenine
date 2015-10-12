

ROOT_SCOPE_METHOD( MD( 'Objective', 'OBJECTIVE_FACTORY_single()' ) )


OBJECT( 'OBJECTIVE_FACTORY',
  methods = [
    MS( ARG( CW( '@' ), CG( 'LIST', 'phrase' ) ), """
      JUMP__return_ANY( CONTEXT, CONTEXT, $CA(OBJECTIVE_new( PARAM_phrase )) ) ;
    """ ),
  ]
)

OBJECTIVE( 'OBJECTIVE',
  attributes = [
    A( 'ANY', 'phrase' ),
  ],
  objective = """
    JUMP__evaluate_ANY( CONTEXT, ACTION->phrase, CONTEXT ) ;
  """
)




FRAME( 'REPLACER',
  attributes = [
    A( 'ANY', 'value' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      JUMP__return_ANY( ACTION->parent, ACTION->parent, ACTION->value ) ;
    """ ),
  ]
)

OBJECTIVE( 'RETURNER',
  attributes = [
    A( 'ANY', 'object' ),
  ],
  objective = """
    JUMP__return_ANY( CONTEXT, CONTEXT, ACTION->object ) ;
  """
)

OBJECTIVE( 'RETURN_THIS',
  objective = """
    JUMP__this( CONTEXT, CONTEXT ) ;
  """
)

OBJECTIVE( 'FORWARDER',
  objective = """
    JUMP__return_ANY( CONTEXT, CONTEXT, THAT ) ;
  """
)

OBJECTIVE( 'IGNORER' ) ;

OBJECTIVE( 'FAILURE',
  objective = """
    nom_fail( CONTEXT, "Failure because object does nothing", $NONE ) ;
  """
)

FRAME( 'INVERTER',
  attributes = [
    A( 'ANY', 'value' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      nom_fail( ACTION->parent, "Inverter failure", $NONE ) ;
    """ ),
    MS( ARG( CW( 'fail' ), CG( 'ANY', 'error' ) ), """
      JUMP__return_ANY( ACTION->parent, ACTION->parent, ACTION->value ) ;
    """ ),
  ]
)


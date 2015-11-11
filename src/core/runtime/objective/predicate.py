

ROOT_SCOPE_METHOD(
  MD( 'Predicate', 'PREDICATE_FACTORY_single()' ),
)


OBJECT( 'PREDICATE_FACTORY',
  methods = [
    MS( ARG( CW( '@' ), CG( 'ANY', 'scope' ), CG( 'LIST', 'phrase' ) ), """
      JUMP__return_ANY( CONTEXT, CONTEXT, $CA(PREDICATE_new( PARAM_scope, PARAM_phrase )) ) ;
    """ ),
  ]
)

OBJECTIVE( 'PREDICATE',
  attributes = [
    A( 'ANY', 'scope' ),
    A( 'ANY', 'phrase' ),
  ],
  objective = """
    JUMP__evaluate_ANY( $CA(FRAME__PREDICATE_new( CONTEXT )), ACTION->phrase, nom_start_object_new( CONTEXT, ACTION->scope ) ) ;
  """,
  dump = D( '%s', '$DUMP( object->phrase )' )
)

FRAME( 'PREDICATE',
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      JUMP__that( ACTION->parent, ACTION->parent ) ;
    """ ),
  ]
)



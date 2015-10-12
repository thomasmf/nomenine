

ROOT_SCOPE_METHOD( MD( 'Composition', 'COMPOSITION_FACTORY_single()' ) )


TEST( """ Map @ ( list 234 5 34 ) ( Composition @ ( list ( closure [ : that * 10 ] ) ( closure [ : that + 1 ] ) ) ) next value == 51 """ )


OBJECT( 'COMPOSITION_FACTORY',
  methods = [
    MS( ARG( CW( '@' ), CG( 'LIST', 'objectives' ) ), """
      JUMP__return_ANY( CONTEXT, CONTEXT, $CA(COMPOSITION_new( PARAM_objectives )) ) ;
    """ ),
  ]
)

OBJECTIVE( 'COMPOSITION',
  attributes = [
    A( 'ANY', 'objectives' ),
  ],
  objective = """
    JUMP__value( $CA(FRAME__COMPOSITION_1_new( CONTEXT, ACTION->objectives, THAT )), ACTION->objectives ) ;
  """
)


FRAME( 'COMPOSITION_1',
  attributes = [
    A( 'ANY', 'objectives' ),
    A( 'ANY', 'that' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      nom_do_sync( FRAME__TASK_new( $CA(FRAME__COMPOSITION_2_new( ACTION->parent, ACTION->objectives )), PARAM_value, ACTION->that ) ) ;
    """ ),
    MS( ARG( CW( 'fail' ), CG( 'ANY', 'error' ) ), """
      JUMP__return_ANY( ACTION->parent, ACTION->parent, ACTION->that ) ;
    """ ),
  ]
)

FRAME( 'COMPOSITION_2',
  attributes = [
    A( 'ANY', 'objectives' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      JUMP__next( $CA(FRAME__COMPOSITION_3_new( ACTION->parent, PARAM_value )), ACTION->objectives ) ;
    """ ),
  ]
)

FRAME( 'COMPOSITION_3',
  attributes = [
    A( 'ANY', 'that' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      JUMP__value( $CA(FRAME__COMPOSITION_1_new( ACTION->parent, PARAM_value, ACTION->that )), PARAM_value ) ;
    """ ),
  ]
)


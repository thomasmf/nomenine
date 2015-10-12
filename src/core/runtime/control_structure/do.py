

ROOT_SCOPE_METHOD( MC( ARG( CW( 'do' ), CG( 'LIST', 'phrase' ) ), """
  JUMP__this( $CA(FRAME__DO_new( CONTEXT, PARAM_phrase )), CONTEXT ) ;
""" ) )


TEST( """ do [ . 1 ] do [ . 2 ] """ )


FRAME( 'DO',
  attributes = [
    A( 'ANY', 'phrase' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      JUMP__evaluate_ANY( $CA(FRAME__REPLACER_new( ACTION->parent, PARAM_value )), ACTION->phrase, PARAM_value ) ;
    """ ),
  ]
)


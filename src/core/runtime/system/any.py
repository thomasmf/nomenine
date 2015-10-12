

ROOT_SCOPE_METHOD( MD( 'Any', 'ANY_FACTORY_single()' ) )
ROOT_SCOPE_METHOD( MD( 'none', '$NONE' ) )


NONE = 'ANY_single()'


OBJECT( 'ANY' )

OBJECT( 'ANY_FACTORY',
  inherit = [ 'TYPE' ],
  methods = [
    MS( ARG( CW( 'test' ), CG( 'ANY', 'object' ) ), """
      JUMP__return_ANY( CONTEXT, CONTEXT, PARAM_object ) ;
    """ ),
    MS( ARG( CW( 'consume' ), CG( 'LIST', 'phrase' ) ), """
      JUMP__value( $CA(FRAME__ANY_CONSUME_new( CONTEXT, PARAM_phrase )), PARAM_phrase ) ;
    """ ),
    MS( ARG( CW( '@' ) ), """
      JUMP__return_ANY( CONTEXT, CONTEXT, ANY_single() ) ;
    """ ),
  ]
)

FRAME( 'ANY_CONSUME',
  attributes = [
    A( 'ANY', 'phrase' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      JUMP__return_ANY( ACTION->parent, ACTION->parent, ACTION->phrase ) ;
    """ ),
  ]
)


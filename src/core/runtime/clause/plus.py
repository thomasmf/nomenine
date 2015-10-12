

ROOT_SCOPE_METHOD( MD( 'Plus', 'PLUS_FACTORY_single()' ) )


TEST( """ Or @ ( . [ ( Plus @ y ) ( Plus @ x ) ] flatten () ) consume [ x x y y y x y y ] value value == x """ )


OBJECT( 'PLUS_FACTORY',
  methods = [
    MS( ARG( CW( '@' ), CG( 'CLAUSE', 'clause' ) ), """
      JUMP__return_ANY( CONTEXT, CONTEXT, $CA(PLUS_new( PARAM_clause )) ) ;
    """ ),
  ]
)

OBJECT( 'PLUS',
  inherit = [ 'CLAUSE' ],
  attributes = [
    A( 'ANY', 'type' ),
  ],
  methods = [
    MS( ARG( CW( 'consume' ), CG( 'LIST', 'phrase' ) ), """
      JUMP__consume_LIST( $CA(FRAME__PLUS_0_new( CONTEXT )), $CA(STAR_new( ACTION->type )), PARAM_phrase ) ;
    """ ),
  ],
  dump = D( '%s', '$DUMP( object->type )' )
)

FRAME( 'PLUS_0',
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      JUMP__value( $CA(FRAME__PLUS_1_new( ACTION->parent, PARAM_value )), PARAM_value ) ;
    """ ),
  ]
)

FRAME( 'PLUS_1',
  attributes = [
    A( 'ANY', 'element' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      JUMP__value( $CA(FRAME__REPLACER_new( ACTION->parent, ACTION->element )), PARAM_value ) ;
    """ ),
  ]
)


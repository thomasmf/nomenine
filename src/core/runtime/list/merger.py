

ROOT_SCOPE_METHOD( MD( 'Merger', 'MERGER_FACTORY_single()' ) )


OBJECT( 'MERGER_FACTORY',
  methods = [
    MS( ARG( CW( '@' ), CG( 'LIST', 'beginning' ), CG( 'LIST', 'end' ) ), """
      JUMP__return_ANY( CONTEXT, CONTEXT, $CA(MERGER_new( PARAM_beginning, PARAM_end )) ) ;
    """ ),
  ]
)

OBJECT( 'MERGER',
  inherit = [ 'LIST' ],
  attributes = [
    A( 'ANY', 'beginning' ),
    A( 'ANY', 'end' ),
  ],
  methods = [
    MS( ARG( CW( 'value' ) ), """
      JUMP__value( $CA(FRAME__MERGER_VALUE_new( CONTEXT, ACTION->end )), ACTION->beginning ) ;
    """ ),
    MS( ARG( CW( 'next' ) ), """
      JUMP__value( $CA(FRAME__MERGER_NEXT_1_new( CONTEXT, ACTION )), ACTION->beginning ) ;
    """ ),
  ]
)

FRAME( 'MERGER_VALUE',
  attributes = [
    A( 'ANY', 'end' ),
  ],
  methods = [
    MS( ARG( CW( 'fail' ), CG( 'ANY', 'error' ) ), """
      JUMP__value( ACTION->parent, ACTION->end ) ;
    """ ),
  ]
)

FRAME( 'MERGER_NEXT_1',
  attributes = [
    A( 'MERGER', 'merger' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      JUMP__next( $CA(FRAME__MERGER_NEXT_2_new( ACTION->parent, ACTION->merger->end )), ACTION->merger->beginning ) ;
    """ ),
    MS( ARG( CW( 'fail' ), CG( 'ANY', 'error' ) ), """
      JUMP__next( ACTION->parent, ACTION->merger->end ) ;
    """ ),
  ]
)

FRAME( 'MERGER_NEXT_2',
  attributes = [
    A( 'ANY', 'end' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      JUMP__return_ANY( ACTION->parent, ACTION->parent, $CA(MERGER_new( PARAM_value, ACTION->end )) ) ;
    """ ),
  ]
)


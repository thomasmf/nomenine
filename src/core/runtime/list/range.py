

ROOT_SCOPE_METHOD( MD( 'Range', 'RANGE_FACTORY_single()' ) )


TEST( """ Range @ 0 4 produce ( StringExtract ) == "[ 0 1 2 3 4 ]" """ )


OBJECT( 'RANGE_FACTORY',
  methods = [
    MS( ARG( CW( '@' ), CG( 'ANY', 'first' ), CG( 'ANY', 'last' ) ), """
      JUMP__return_ANY( CONTEXT, CONTEXT, $CA(RANGE_new( PARAM_first, PARAM_last )) ) ;
    """ ),
  ]
)

OBJECT( 'RANGE',
  inherit = [ 'LIST' ],
  attributes = [
    A( 'ANY', 'first' ),
    A( 'ANY', 'last' ),
  ],
  methods = [
    MS( ARG( CW( 'next' ) ), """
      nom_send_nonempty_flat_phrase_message( $CA(FRAME__RANGE_NEXT_1_new( CONTEXT, ACTION )), ACTION->first, $LISTNEW( WORD_new( "++" ) ) ) ;
    """ ),
    MS( ARG( CW( 'value' ) ), """
      JUMP__return_ANY( CONTEXT, CONTEXT, $CA(ACTION->first) ) ;
    """ ),
  ],
  dump = D( '<%s> %s', '$DUMP( object->first ), $DUMP( object->last )' )
)


FRAME( 'RANGE_NEXT_1',
  attributes = [
    A( 'RANGE', 'range' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      nom_send_nonempty_flat_phrase_message( $CA(FRAME__RANGE_NEXT_2_new( ACTION->parent, PARAM_value, ACTION->range->last )), PARAM_value, $LISTNEW( WORD_new( "=<" ), ACTION->range->last ) ) ;
    """ ),
  ]
)

FRAME( 'RANGE_NEXT_2',
  attributes = [
    A( 'ANY', 'first' ),
    A( 'ANY', 'last' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      JUMP__return_ANY( ACTION->parent, ACTION->parent, $CA(RANGE_new( ACTION->first, ACTION->last )) ) ;
    """ ),
    MS( ARG( CW( 'fail' ), CG( 'ANY', 'error' ) ), """
      JUMP__return_ANY( ACTION->parent, ACTION->parent, $LISTNEW() ) ;
    """ ),
  ]
)


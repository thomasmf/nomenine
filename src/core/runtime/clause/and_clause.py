

ROOT_SCOPE_METHOD( MD( 'And', 'AND_CLAUSE_FACTORY_single()' ) )


TEST( """ And @ ( list ( Word ) ( Word ) ) consume [ x 1 2 3 ] next value == x """ )
TEST( """ if [ And @ ( list ( Word ) ( Word ) ) consume [ 1 2 3 ] ] then [ . 1 ] else [ . 2 ] == 2 """ )
TEST( """ And @ ( list ( Integer ) ( Not @ ( . 1 ) ) ) consume [ 2 3 ] next value == 2 """ )


OBJECT( 'AND_CLAUSE_FACTORY',
  methods = [
    MS( ARG( CW( '@' ), CG( 'LIST', 'components' ) ), """
      JUMP__return_ANY( CONTEXT, CONTEXT, $CA(AND_CLAUSE_new( PARAM_components )) ) ;
    """ ),
  ]
)


OBJECT( 'AND_CLAUSE',
  inherit = [ 'CLAUSE' ],
  attributes = [
    A( 'ANY', 'components' ),
  ],
  methods = [
    MS( ARG( CW( 'consume' ), CG( 'LIST', 'phrase' ) ), """
      JUMP__value( $CA(FRAME__AND_CLAUSE_3_new( CONTEXT, PARAM_phrase, ACTION->components )), ACTION->components ) ;
    """ ),
  ],
  dump = D( '%s', '$DUMP( object->components )' )
)

FRAME( 'AND_CLAUSE_3',
  attributes = [
    A( 'ANY', 'phrase' ),
    A( 'ANY', 'components' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      JUMP__consume_LIST( $CA(FRAME__AND_CLAUSE_4_new( ACTION->parent, ACTION->phrase, ACTION->components )), PARAM_value, ACTION->phrase ) ;
    """ ),
    MS( ARG( CW( 'fail' ), CG( 'ANY', 'error' ) ), """
      JUMP__return_ANY( ACTION->parent, ACTION->parent, $CA(ELEMENT_new( $NONE, ACTION->phrase )) ) ;
    """ ),
  ]
)

FRAME( 'AND_CLAUSE_4',
  attributes = [
    A( 'ANY', 'phrase' ),
    A( 'ANY', 'components' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      JUMP__next( $CA(FRAME__AND_CLAUSE_5_new( ACTION->parent, ACTION->phrase )), ACTION->components ) ;
    """ ),
  ]
)

FRAME( 'AND_CLAUSE_5',
  attributes = [
    A( 'ANY', 'phrase' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      JUMP__value( $CA(FRAME__AND_CLAUSE_3_new( ACTION->parent, ACTION->phrase, PARAM_value )), PARAM_value ) ;
    """ ),
  ]
)


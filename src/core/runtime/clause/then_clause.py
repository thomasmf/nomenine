

ROOT_SCOPE_METHOD( MD( 'Then', 'THEN_CLAUSE_FACTORY_single()' ) )


TEST( """ Then @ ( Not @ ( . 1 ) ) ( Integer ) consume [ 2 3 ] value == 2 """ )
TEST( """ Then @ ( Not @ ( Or @ ( list 1 2 ) ) ) ( Integer ) consume [ 3 ] value == 3 """ )
TEST( """ if [ Then @ ( Not @ ( Or @ ( list 1 2 ) ) ) ( Integer ) consume [ 2 3 4 ] ] then [ . 1 ] else [ . 2 ] == 2 """ )


OBJECT( 'THEN_CLAUSE_FACTORY',
  methods = [
    MS( ARG( CW( '@' ), CG( 'CLAUSE', 'if_clause' ), CG( 'CLAUSE', 'then_clause' ) ), """
      JUMP__return_ANY( CONTEXT, CONTEXT, $CA(THEN_CLAUSE_new( PARAM_if_clause, PARAM_then_clause )) ) ;
    """ ),
  ]
)

OBJECT( 'THEN_CLAUSE',
  inherit = [ 'CLAUSE' ],
  attributes = [
    A( 'ANY', 'if_clause' ),
    A( 'ANY', 'then_clause' ),
  ],
  methods = [
    MS( ARG( CW( 'consume' ), CG( 'LIST', 'phrase' ) ), """
      JUMP__consume_LIST( $CA(FRAME__THEN_CLAUSE_1_new( CONTEXT, ACTION->then_clause, PARAM_phrase )), ACTION->if_clause, PARAM_phrase ) ;
    """ ),
  ]
)

FRAME( 'THEN_CLAUSE_1',
  attributes = [
    A( 'ANY', 'then_clause' ),
    A( 'ANY', 'phrase' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      JUMP__consume_LIST( ACTION->parent, ACTION->then_clause, ACTION->phrase ) ;
    """ ),
  ]
)




ROOT_SCOPE_METHOD( MD( 'ConsumeMap', 'CONSUME_MAP_FACTORY_single()' ) )


TEST( """ ConsumeMap @ ( Integer ) [ 1 2 3 ] next value == 2 """ )
TEST( """ ConsumeMap @ ( Grouping @ ( . [ ( Word ) ( Integer ) ] flatten () ) ) [ a 1 b 2 c 3 ] next value next value == 2 """ )
TEST( """ ConsumeMap @ ( Or @ ( . [ ( Plus @ ( RangeType @ 0 9 ) ) ( Plus @ b ) ] flatten () ) ) [ b b 1 2 3 b b 4 5 b b b ] next value next value == 2 """ )


FUNCTION( 'ANY nom_consume_map_new( ANY clause, ANY phrase )', """
  return $CA(nom_lazy_new( $CA(CONSUME_MAP_OBJECTIVE_new( clause, phrase )) )) ;
""" )


OBJECT( 'CONSUME_MAP_FACTORY',
  methods = [
    MS( ARG( CW( '@' ), CG( 'CLAUSE', 'clause' ), CG( 'LIST', 'phrase' ) ), """
      JUMP__return_ANY( CONTEXT, CONTEXT, $CA(nom_consume_map_new( PARAM_clause, PARAM_phrase )) ) ;
    """ ),
  ]
)

OBJECTIVE( 'CONSUME_MAP_OBJECTIVE',
  attributes = [
    A( 'ANY', 'clause' ),
    A( 'ANY', 'phrase' ),
  ],
  objective = """
    JUMP__consume_LIST( $CA(FRAME__CONSUME_MAP_0_new( CONTEXT, ACTION )), ACTION->clause, ACTION->phrase ) ;
  """
)

FRAME( 'CONSUME_MAP_0',
  attributes = [
    A( 'CONSUME_MAP_OBJECTIVE', 'consume_map_objective' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      REFERENCE reference = nom_reference_new( $NONE ) ;
      JUMP__value( $CA(FRAME__SPLIT_new( $CA(FRAME__CONSUME_MAP_1_new( ACTION->parent, ACTION->consume_map_objective, reference )), PARAM_value, reference )), PARAM_value ) ;
    """ ),
  ]
)

FRAME( 'CONSUME_MAP_1',
  attributes = [
    A( 'CONSUME_MAP_OBJECTIVE', 'consume_map_objective' ),
    A( 'REFERENCE', 'value' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      JUMP__return_ANY( ACTION->parent, ACTION->parent, $CA(ELEMENT_new( ACTION->value->value, nom_consume_map_new( ACTION->consume_map_objective->clause, PARAM_value ) )) ) ;
    """ ),
  ]
)


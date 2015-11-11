

OBJECT( 'PARSE_TOKEN_INTEGER',
  methods = [
    MTID_IS( 'TYPE' ),
    MS( ARG( CW( 'consume' ), CG( 'LIST', 'phrase' ) ), """
      JUMP__consume_LIST( $CA(FRAME__PARSE_TOKEN_INTEGER_0_new( CONTEXT )), $CA(PLUS_new( $CA(RANGE_TYPE_new( $CA(CHARACTER_new( '0' )), $CA(CHARACTER_new( '9' )) )) )), PARAM_phrase ) ;
    """ ),
  ]
)

FRAME( 'PARSE_TOKEN_INTEGER_0',
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      REFERENCE reference = nom_reference_new( $NONE ) ;
      JUMP__value( $CA(FRAME__SPLIT_new( $CA(FRAME__PARSE_TOKEN_INTEGER_1_new( ACTION->parent, reference )), PARAM_value, reference )), PARAM_value ) ;
    """ ),
  ]
)

FRAME( 'PARSE_TOKEN_INTEGER_1',
  attributes = [
    A( 'REFERENCE', 'value' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      JUMP__join_STRING( $CA(FRAME__PARSE_TOKEN_INTEGER_2_new( ACTION->parent, PARAM_value )), ACTION->value->value, STRING_new( "" ) ) ;
    """ ),
  ]
)

FRAME( 'PARSE_TOKEN_INTEGER_2',
  attributes = [
    A( 'ANY', 'next' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      JUMP__produce_TID__INTEGER_FACTORY_single( $CA(FRAME__PARSE_TOKEN_INTEGER_3_new( ACTION->parent, ACTION->next )), PARAM_value, $CA(INTEGER_FACTORY_single()) ) ;
    """ ),
  ]
)

FRAME( 'PARSE_TOKEN_INTEGER_3',
  attributes = [
    A( 'ANY', 'next' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      JUMP__return_ANY( ACTION->parent, ACTION->parent, $CA(ELEMENT_new( PARAM_value, ACTION->next )) ) ;
    """ ),
  ]
)



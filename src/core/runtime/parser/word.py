

OBJECT( 'PARSE_TOKEN_WORD',
  methods = [
    MTID_IS( 'TYPE' ),
    MS( ARG( CW( 'consume' ), CG( 'LIST', 'phrase' ) ), """
      JUMP__consume_LIST( $CA(FRAME__PARSE_TOKEN_WORD_0_new( CONTEXT )), $CA(PLUS_new( $CA(OR_CLAUSE_new( $LISTNEW(
        $CA(RANGE_TYPE_new( $CA(CHARACTER_new( 0x21 )), $CA(CHARACTER_new( 0x27 )) )),
        $CA(RANGE_TYPE_new( $CA(CHARACTER_new( 0x2A )), $CA(CHARACTER_new( 0x5A )) )),
        $CA(CHARACTER_new( 0x5C )),
        $CA(RANGE_TYPE_new( $CA(CHARACTER_new( 0x5E )), $CA(CHARACTER_new( 0x7E )) ))
      ) )) )), PARAM_phrase ) ;
    """ ),
  ]
)

FRAME( 'PARSE_TOKEN_WORD_0',
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      REFERENCE reference = nom_reference_new( $NONE ) ;
      JUMP__value( $CA(FRAME__SPLIT_new( $CA(FRAME__PARSE_TOKEN_WORD_1_new( ACTION->parent, reference )), PARAM_value, reference )), PARAM_value ) ;
    """ ),
  ]
)

FRAME( 'PARSE_TOKEN_WORD_1',
  attributes = [
    A( 'REFERENCE', 'value' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      JUMP__join_STRING( $CA(FRAME__PARSE_TOKEN_WORD_2_new( ACTION->parent, PARAM_value )), ACTION->value->value, STRING_new( "" ) ) ;
    """ ),
  ]
)

FRAME( 'PARSE_TOKEN_WORD_2',
  attributes = [
    A( 'ANY', 'next' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      JUMP__return_ANY( ACTION->parent, ACTION->parent, $CA(ELEMENT_new( $CA(WORD_new( $C(STRING,PARAM_value)->data )), ACTION->next )) ) ;
    """ ),
  ]
)



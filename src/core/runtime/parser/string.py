

OBJECT( 'PARSE_TOKEN_STRING',
  methods = [
    MTID_IS( 'TYPE' ),
    MS( ARG( CW( 'consume' ), CG( 'LIST', 'phrase' ) ), """
      JUMP__consume_LIST( $CA(FRAME__PARSE_TOKEN_STRING_0_new( CONTEXT )),
        $CA(PATTERN_new( $LISTNEW(
          CHARACTER_new( 0x22 ),
          SHAPE_new( $CA(WORD_new( "content" )), $CA(STAR_new( $CA(OR_CLAUSE_new( $LISTNEW(
            CHARACTER_new( 0x09 ),
            CHARACTER_new( 0x0A ),
            CHARACTER_new( 0x0D ),
            CHARACTER_new( 0x20 ),
            CHARACTER_new( 0x21 ),
            $CA(RANGE_TYPE_new( $CA(CHARACTER_new( 0x23 )), $CA(CHARACTER_new( 0x7E )) ))
          ) )) )) ),
          CHARACTER_new( 0x22 )
        ) )),
        PARAM_phrase
      ) ;
    """ ),
  ]
)

FRAME( 'PARSE_TOKEN_STRING_0',
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      REFERENCE reference = nom_reference_new( $NONE ) ;
      JUMP__value( $CA(FRAME__SPLIT_new( $CA(FRAME__PARSE_TOKEN_STRING_1_new( ACTION->parent, reference )), PARAM_value, reference )), PARAM_value ) ;
    """ ),
  ]
)

FRAME( 'PARSE_TOKEN_STRING_1',
  attributes = [
    A( 'REFERENCE', 'value' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      nom_send_nonempty_flat_phrase_message( $CA(FRAME__PARSE_TOKEN_STRING_2_new( ACTION->parent, PARAM_value )), ACTION->value->value, $LISTNEW( WORD_new( "content" ) ) ) ;
    """ ),
  ]
)

FRAME( 'PARSE_TOKEN_STRING_2',
  attributes = [
    A( 'ANY', 'next' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      JUMP__join_STRING( $CA(FRAME__PARSE_TOKEN_STRING_3_new( ACTION->parent, ACTION->next )), PARAM_value, STRING_new( "" ) ) ;
    """ ),
  ]
)

FRAME( 'PARSE_TOKEN_STRING_3',
  attributes = [
    A( 'ANY', 'next' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      JUMP__return_ANY( ACTION->parent, ACTION->parent, $CA(ELEMENT_new( PARAM_value, ACTION->next )) ) ;
    """ ),
  ]
)



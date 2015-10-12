

OBJECT( 'PARSE_TOKEN_EXPRESSION',
  methods = [
    MTID_IS( 'TYPE' ),
    MS( ARG( CW( 'consume' ), CG( 'LIST', 'phrase' ) ), """
      JUMP__consume_LIST( $CA(FRAME__PARSE_TOKEN_EXPRESSION_0_new( CONTEXT )),
        $CA(PATTERN_new( $LISTNEW( CHARACTER_new( '(' ), SHAPE_new( $CA(WORD_new( "content" )), nom_parse_phrase_clause_lazy() ), CHARACTER_new( ')' ) ) )),
        PARAM_phrase
      ) ;
    """ ),
  ]
)

FRAME( 'PARSE_TOKEN_EXPRESSION_0',
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      REFERENCE reference = nom_reference_new( $NONE ) ;
      JUMP__value( $CA(FRAME__SPLIT_new( $CA(FRAME__PARSE_TOKEN_EXPRESSION_1_new( ACTION->parent, reference )), PARAM_value, reference )), PARAM_value ) ;
    """ ),
  ]
)

FRAME( 'PARSE_TOKEN_EXPRESSION_1',
  attributes = [
    A( 'REFERENCE', 'value' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      nom_send_nonempty_flat_phrase_message( $CA(FRAME__PARSE_TOKEN_EXPRESSION_2_new( ACTION->parent, PARAM_value )), ACTION->value->value, $LISTNEW( WORD_new( "content" ) ) ) ;
    """ ),
  ]
)


FRAME( 'PARSE_TOKEN_EXPRESSION_2',
  attributes = [
    A( 'ANY', 'next' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      nom_parse_fine( $CA(FRAME__PARSE_TOKEN_EXPRESSION_3_new( ACTION->parent, ACTION->next )), PARAM_value ) ;
    """ ),
  ]
)


FRAME( 'PARSE_TOKEN_EXPRESSION_3',
  attributes = [
    A( 'ANY', 'next' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      JUMP__return_ANY( ACTION->parent, ACTION->parent, $CA(ELEMENT_new( $CA(EXPRESSION_new( PARAM_value )), ACTION->next )) ) ;
    """ ),
  ]
)


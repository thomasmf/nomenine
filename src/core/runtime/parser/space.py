

OBJECT( 'SPACE',
  methods = [
  MTID_IS( 'SPACE' ),
] )

TYPE( 'SPACE_FACTORY' )

OBJECTIVE( 'SPACE_TEST_OBJECTIVE',
  objective = """
    $OPT(
      $IFLET( o, SPACE, THAT ) ;
      nom_fail( CONTEXT, "Space test objective informing that a space was encountered", $NONE ) ;
    )
    $OPT(
      $IFLET( o, WORD, THAT ) ;
      JUMP__return_ANY( CONTEXT, CONTEXT, THAT ) ;
    )
    $OPT(
      $IFLET( o, EXPRESSION, THAT ) ;
      JUMP__return_ANY( CONTEXT, CONTEXT, THAT ) ;
    )
    $OPT(
      $IFLET( o, INTEGER, THAT ) ;
      JUMP__return_ANY( CONTEXT, CONTEXT, THAT ) ;
    )
    $OPT(
      $IFLET( o, ARRAY_MUTABLE_NOLOCK, THAT ) ;
      JUMP__return_ANY( CONTEXT, CONTEXT, THAT ) ;
    )
    $OPT(
      $IFLET( o, STRING, THAT ) ;
      JUMP__return_ANY( CONTEXT, CONTEXT, THAT ) ;
    )
    JUMP__produce_TID__SPACE_FACTORY_single( $CA(FRAME__INVERTER_new( CONTEXT, THAT )), THAT, $CA(SPACE_FACTORY_single()) ) ;
  """
)

OBJECT( 'PARSE_TOKEN_SPACE',
  methods = [
    MTID_IS( 'TYPE' ),
    MS( ARG( CW( 'consume' ), CG( 'LIST', 'phrase' ) ), """
      JUMP__consume_LIST( $CA(FRAME__PARSE_TOKEN_SPACE_0_new( CONTEXT )), $CA(PLUS_new( $CA(OR_CLAUSE_new( $LISTNEW(
        $CA(CHARACTER_new( 0x09 )),
        $CA(CHARACTER_new( 0x0A )),
        $CA(CHARACTER_new( 0x0D )),
        $CA(CHARACTER_new( 0x20 ))
      ) )) )), PARAM_phrase ) ;
    """ ),
  ]
)

FRAME( 'PARSE_TOKEN_SPACE_0',
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      JUMP__next( $CA(FRAME__PARSE_TOKEN_SPACE_1_new( ACTION->parent )), PARAM_value ) ;
    """ ),
  ]
)

FRAME( 'PARSE_TOKEN_SPACE_1',
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      JUMP__return_ANY( ACTION->parent, ACTION->parent, $CA(ELEMENT_new( $CA(SPACE_single()), PARAM_value )) ) ;
    """ ),
  ]
)


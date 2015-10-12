

REGISTER_FLAG( 'map_parsing', 'do not eagerly process parsed data' )


TEST( """ . ". 1234 * 10" parse evaluate () == 12340 """ )
TEST( """ . ". 1234 * 10" evaluate () == 12340 """ )


FUNCTION( 'ANY nom_parse_filter_wrapper( ANY elements )', """
   return nom_mill_new( elements, $CA(SPACE_TEST_OBJECTIVE_single()) ) ;
""" )


FUNCTION( 'void nom_parse_fine( ANY context, ANY elements )', """

  $ENABLED( map_parsing,
    JUMP__return_ANY( context, context, nom_parse_filter_wrapper( elements ) ) ;
  )

   $DISABLED( map_parsing,
    nom_list_eager_copy( context, nom_parse_filter_wrapper( elements ) ) ;
  )

""" )


FUNCTION( 'void nom_parse_phrase( ANY context, ANY characters )', """
  JUMP__consume_LIST( $CA(FRAME__PARSE_1_new( context )), nom_parse_phrase_clause_lazy(), characters ) ;
""" )

FUNCTION( 'ANY nom_parse_phrase_clause_lazy()', """
  return $LAZY( ANY,
    $CA(STAR_new( $CA(OR_CLAUSE_new( $LISTNEW(
      PARSE_TOKEN_SPACE_single(),
      PARSE_TOKEN_INTEGER_single(),
      PARSE_TOKEN_STRING_single(),
      PARSE_TOKEN_QUOTE_single(),
      PARSE_TOKEN_EXPRESSION_single(),
      PARSE_TOKEN_WORD_single()
    ) )) ))
  ) ;
""" )


FRAME( 'PARSE_1',
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      JUMP__value( $CA(FRAME__PARSE_2_new( ACTION->parent )), PARAM_value ) ;					// dropping possible additional unrecognized tokens
    """ ),
  ]
)

FRAME( 'PARSE_2',
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """

      nom_parse_fine( ACTION->parent, PARAM_value ) ;

    """ ),
  ]
)




TEST( """ . [ . 2 * 3 * 4 ] evaluate ( ) == 24 """ )
TEST( """ . [ ( . 11 * 2 ) 12 ] flatten ( ) value == 22 """ )

TEST( """ . [ f ] evaluate ( Function @ f ( Closure @ () [ . 1313 ] ) ) == 1313 """ )
TEST( """ . [ f ] evaluate ( Union @ ( . [ ( Function @ f ( Closure @ () [ . 1414 ] ) ) ] flatten () ) ) == 1414 """ )
TEST( """ . [ f + ( . 2828 ) ] evaluate ( Union @ ( . [ ( Function @ f ( Closure @ () [ . 1414 ] ) ) () ] flatten () ) ) == 4242 """ )


FUNCTION( 'void nom_phrase_evaluate( ANY context, ANY phrase, ANY scope )', """
  nom_phrase_flatten( $CA(FRAME__EVALUATE_READABLE_2_new( context, scope )), phrase, scope ) ;
""" )

FRAME( 'EVALUATE_READABLE_2',
  attributes = [
    A( 'ANY', 'scope' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      nom_send_flat_phrase_message( ACTION->parent, ACTION->scope, PARAM_value ) ;
    """ ),
  ]
)


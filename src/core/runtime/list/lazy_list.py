

ROOT_SCOPE_METHOD( MD( 'LazyList', 'LAZY_LIST_FACTORY_single()' ) )


TEST( """ LazyList @ ( Closure @ () [ do [ : yield 123 ] do [ : yield 234 ] do [ : yield 345 ] ] ) joinToString "," == "123,234,345" """ )
TEST( """ LazyList @ ( Closure @ () [ do [ : yield 123 ] do [ Range @ 1 3 reduce 0 ( closure [ : yield ( : that ) ] ) ] do [ : yield 345 ] ] ) joinToString "," == "123,1,2,3,345" """ )


FUNCTION( 'ANY nom_lazy_list_new( ANY action )', """
  return nom_mill_new( $CA(LAZY_LIST_new( nom_generator_new( action ) )), $CA(FORWARDER_new()) ) ;
""" )


OBJECT( 'LAZY_LIST_FACTORY',
  methods = [
    MS( ARG( CW( '@' ), CG( 'ANY', 'action' ) ), """
      JUMP__return_ANY( CONTEXT, CONTEXT, nom_lazy_list_new( PARAM_action ) ) ;
    """ ),
  ]
)

OBJECT( 'LAZY_LIST',
  inherit = [ 'LIST' ],
  attributes = [
    A( 'GENERATOR', 'generator' ),
  ],
  methods = [
    MS( ARG( CW( 'value' ) ), """
      JUMP__generate( CONTEXT, $CA(ACTION->generator) ) ;
    """ ),
    MS( ARG( CW( 'next' ) ), """
      JUMP__return_ANY( CONTEXT, CONTEXT, $CA(ACTION) ) ;
    """ ),
  ]
)



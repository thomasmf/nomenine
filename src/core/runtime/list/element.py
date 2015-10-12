

ROOT_SCOPE_METHOD( MD( 'Element', 'ELEMENT_FACTORY_single()' ) )


TEST( """ Element @ 123 ( empty ) value == 123 """ )
TEST( """ Element @ 123 ( Element @ 234 ( empty ) ) next value == 234 """ )

TEST( """ . [ 1 2 3 ] next value == 2 """ )


OBJECT( 'ELEMENT_FACTORY',
  methods = [
    MS( ARG( CW( '@' ), CG( 'ANY', 'value' ), CG( 'ANY', 'next' ) ), """
      JUMP__return_ANY( CONTEXT, CONTEXT, $CA(ELEMENT_new( PARAM_value, PARAM_next )) ) ;
    """ ),
  ]
)

OBJECT( 'ELEMENT',
  inherit = [ 'VALUE', 'LIST' ],
  attributes = [
    A( 'ANY', 'next' ),
  ],
  methods = [
    MS( ARG( CW( 'value' ) ), """
      JUMP__return_ANY( CONTEXT, CONTEXT, ACTION->value ) ;
    """ ),
    MS( ARG( CW( 'next' ) ), """
      JUMP__return_ANY( CONTEXT, CONTEXT, ACTION->next ) ;
    """ ),
  ],
  dump = D( '<%s> %s', '$DUMP( object->value ), $DUMP( object->next )' )
)




FUNCTION( 'ELEMENT_CHARACTERS nom_element_characters_new( n_string data )', """
  return ELEMENT_CHARACTERS_new( data ) ;
""" )

FUNCTION( 'CHARACTER nom_element_characters_value( ELEMENT_CHARACTERS element_characters )', """
  return CHARACTER_new( element_characters->data[ 0 ] ) ;
""" )

FUNCTION( 'ANY nom_element_characters_next( ELEMENT_CHARACTERS element_characters )', """
  n_string data = element_characters->data + 1 ;
  if ( element_characters->data[ 0 ] == '\\0' ) {
    return $LISTNEW() ;
  } else {
    return $CA(nom_element_characters_new( data )) ;
  }
""" )

FUNCTION( 'n_boolean nom_element_characters_has_elements( ELEMENT_CHARACTERS element_characters )', """
  return element_characters->data[ 0 ] == 0 ;
""" )


OBJECT( 'ELEMENT_CHARACTERS',
  inherit = [ 'LIST' ],
  attributes = [
    A( 'n_string', 'data' ),
  ],
  methods = [
    MS( ARG( CW( 'next' ) ), """
      JUMP__return_ANY( CONTEXT, CONTEXT, nom_element_characters_next( ACTION ) ) ;
    """ ),
    MS( ARG( CW( 'value' ) ), """
      JUMP__return_ANY( CONTEXT, CONTEXT, $CA(nom_element_characters_value( ACTION )) ) ;
    """ ),

  ],
  dump = D( '<%s> ', 'object->data' )
)


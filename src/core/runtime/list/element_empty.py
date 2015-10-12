

OBJECT( 'ELEMENT_EMPTY',
  inherit = [ 'LIST' ],
  methods = [
    MS( ARG( CW( 'value' ) ), """
      nom_fail( CONTEXT, "Empty sequence has no value", $NONE ) ;
    """ ),
    MS( ARG( CW( 'next' ) ), """
      JUMP__return_ANY( CONTEXT, CONTEXT, $CA(ACTION) ) ;
    """ ),
  ]
)


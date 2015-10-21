

OBJECT( 'BOX',
  inherit = [ 'VALUE' ],
  methods = [
    MC( ARG( CW( 'set' ), CG( 'ANY', 'value' ) ), """
      $NOT_IMPLEMENTED() ;
    """ ),
    MS( ARG( CW( 'get' ) ), """
      JUMP__return_ANY( CONTEXT, CONTEXT, ACTION->value ) ;
    """ ),
  ],
  dump = D( '%s', '$DUMP( object->value )' )
)


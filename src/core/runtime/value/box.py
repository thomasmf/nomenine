

OBJECT( 'BOX',
  inherit = [ 'VALUE' ],
  methods = [
    MC( ARG( CW( 'set' ), CG( 'ANY', 'value' ) ), """
      $NOT_IMPLEMENTED() ;
    """ ),
    MS( ARG( CW( 'get' ) ), """
      $NOT_IMPLEMENTED() ;
    """ ),
  ],
  dump = D( '%s', '$DUMP( object->value )' )
)


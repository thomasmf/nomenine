

FRAME( 'SCOPE',
  attributes = [
    A( 'ANY', 'context' ),
  ],
  methods = [
    MS( ARG( CW( ':' ) ), """
      JUMP__return_ANY( CONTEXT, CONTEXT, ACTION->context ) ;
    """ ),
  ],
  dump = D( '%s', '$DUMP( object->context )' )
)


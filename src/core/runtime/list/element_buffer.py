

ROOT_SCOPE_METHOD( MD( 'Buffer', 'ELEMENT_BUFFER_FACTORY_single()' ) )


FUNCTION( 'ANY nom_buffer_new( ANY list )', """
  return $CA(ELEMENT_BUFFER_new( list, nom_promise_new(), nom_promise_new() )) ;
""" )


OBJECT( 'ELEMENT_BUFFER_FACTORY',
  methods =  [
    MS( ARG( CW( '@' ), CG( 'LIST', 'source' ) ), """
      JUMP__return_ANY( CONTEXT, CONTEXT, nom_buffer_new( PARAM_source ) ) ;
    """ ),
  ]
)

OBJECT( 'ELEMENT_BUFFER',
  inherit = [ 'LIST' ],
  attributes = [
    A( 'ANY', 'source' ),
    A( 'PROMISE', 'value' ),
    A( 'PROMISE', 'next' ),
  ],
  methods = [
    MS( ARG( CW( 'value' ) ), """

      $PROMISE_START( ACTION->value,
        JUMP__value( $CA(FRAME__ELEMENT_BUFFER_AQUIRE_new( CONTEXT, ACTION->value )), ACTION->source ) ;
        return ;
      )

      nom_promise_return( CONTEXT, ACTION->value ) ;

    """ ),
    MS( ARG( CW( 'next' ) ), """

      $PROMISE_START( ACTION->next,
        JUMP__next( $CA(FRAME__ELEMENT_BUFFER_AQUIRE_new( CONTEXT, ACTION->next )), ACTION->source ) ;
        return ;
      )

      nom_promise_return( CONTEXT, ACTION->next ) ;

    """ ),
  ],
  dump = D( 'source: %s <%s> %s', '$DUMP( object->source ),$DUMP( object->value->value ), $DUMP( object->next->value )' )
)

FRAME( 'ELEMENT_BUFFER_AQUIRE',
  attributes = [
    A( 'PROMISE', 'value' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      nom_promise_set_fine( ACTION->value, PARAM_value ) ;
      nom_promise_return( ACTION->parent, ACTION->value ) ;
    """ ),
    MS( ARG( CW( 'fail' ), CG( 'ANY', 'error' ) ), """
      nom_promise_set_fail( ACTION->value, nom_error_new( ACTION->parent, "Buffer failed to aquire input", PARAM_error ) ) ;
      nom_promise_return( ACTION->parent, ACTION->value ) ;
    """ ),
  ],
)



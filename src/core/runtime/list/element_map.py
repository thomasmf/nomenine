

ROOT_SCOPE_METHOD( MD( 'Map', 'ELEMENT_MAP_FACTORY_single()' ) )


TEST( """ Map @ ( Element @ 123 ( empty ) ) ( Closure @ () [ : that * 2 ] ) value == 246 """ )
TEST( """ Map @ ( Element @ 123 ( Element @ 234 ( empty ) ) ) ( Closure @ () [ : that * 2 ] ) next value == 468 """ )


FUNCTION( 'ANY nom_buffer_map( ANY objective, ANY elements )', """
  return nom_buffer_new( $CA(ELEMENT_MAP_new( elements, objective )) ) ;
""" )


OBJECT( 'ELEMENT_MAP_FACTORY',
  methods = [
    MS( ARG( CW( '@' ), CG( 'LIST', 'source' ), CG( 'ANY', 'action' ) ), """
      JUMP__return_ANY( CONTEXT, CONTEXT, $CA(ELEMENT_MAP_new( PARAM_source, PARAM_action )) ) ;
    """ ),
  ]
)

OBJECT( 'ELEMENT_MAP',
  inherit = [ 'LIST' ],
  attributes = [
    A( 'ANY', 'source' ),
    A( 'ANY', 'action' ),
  ],
  methods = [
    MS( ARG( CW( 'value' ) ), """

      $OPT(
        $IFLET( source, ARRAY_MUTABLE_NOLOCK, ACTION->source ) ;

        if ( nom_array_mutable_nolock_size( source ) == 0 ) {
          nom_fail( CONTEXT, "Element map source depleted", $NONE ) ;
        } else {
          nom_do_sync( FRAME__TASK_new( CONTEXT, ACTION->action, nom_array_mutable_nolock_value( source ) ) ) ;
        }
      )

      JUMP__value( $CA(FRAME__ELEMENT_MAP_VALUE_new( CONTEXT, ACTION )), ACTION->source ) ;
    """ ),
    MS( ARG( CW( 'next' ) ), """
      $OPT(
        $IFLET( source, ARRAY_MUTABLE_NOLOCK, ACTION->source ) ;
        JUMP__return_ANY( CONTEXT, CONTEXT, $CA(ELEMENT_MAP_new( $CA(nom_array_mutable_nolock_next( source )), ACTION->action )) ) ;
      )
      JUMP__next( $CA(FRAME__ELEMENT_MAP_NEXT_new( CONTEXT, ACTION )), ACTION->source ) ;
    """ ),
  ]
)

FRAME( 'ELEMENT_MAP_VALUE',
  attributes = [
    A( 'ELEMENT_MAP', 'element_map' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      nom_do_sync( FRAME__TASK_new( ACTION->parent, ACTION->element_map->action, PARAM_value ) ) ;
    """ ),
  ]
)

FRAME( 'ELEMENT_MAP_NEXT',
  attributes = [
    A( 'ELEMENT_MAP', 'element_map' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      JUMP__return_ANY( ACTION->parent, ACTION->parent, $CA(ELEMENT_MAP_new( PARAM_value, ACTION->element_map->action )) ) ;
    """ ),
  ]
)


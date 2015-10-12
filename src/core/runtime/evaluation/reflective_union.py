

ROOT_SCOPE_METHOD( MD( 'ReflectiveUnion', 'REFLECTIVE_UNION_FACTORY_single()' ) )


FUNCTION( 'ANY nom_reflective_union_new( ANY context, ANY scope, ANY components )', """
  FLATMAP_OBJECTIVE flatmap_objective = FLATMAP_OBJECTIVE_new( $NONE ) ;
  ANY target = $CA(UNION_new( nom_buffer_map( $CA(flatmap_objective), components ) )) ;
  flatmap_objective->scope = $CA(UNION_new( $LISTNEW( scope, target ) )) ;
  return target ;
""" )


OBJECT( 'REFLECTIVE_UNION_FACTORY',
  methods = [
    MS( ARG( CW( '@' ), CG( 'ANY', 'scope' ), CG( 'LIST', 'components' ) ), """
      JUMP__return_ANY( CONTEXT, CONTEXT, nom_reflective_union_new( CONTEXT, PARAM_scope, PARAM_components ) ) ;
    """ ),
    ]
 )


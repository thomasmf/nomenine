

ROOT_SCOPE_METHOD( MD( 'AvidMap', 'AVID_MAP_FACTORY_single()' ) )


TEST( """ AvidMap @ ( list 1 2 3 ) ( closure [ : that * 3 ] ) join ":" == "3:6:9" """ )


FUNCTION( 'ANY nom_avid_map_new( ANY context, ANY action, ANY source )', """
  ANY target = nom_buffer_map( action, source ) ;
  nom_list_scan( context, target ) ;
  return target ;
""" )


OBJECT( 'AVID_MAP_FACTORY',
  methods = [
    MS( ARG( CW( '@' ), CG( 'LIST', 'source' ), CG( 'ANY', 'action' ) ), """
      JUMP__return_ANY( CONTEXT, CONTEXT, nom_avid_map_new( CONTEXT, PARAM_action, PARAM_source ) ) ;
    """ ),
  ]
)



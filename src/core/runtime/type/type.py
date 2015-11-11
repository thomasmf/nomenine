

ROOT_SCOPE_METHOD( MD( 'Type', 'TYPE_FACTORY_single()' ) )


TEST( """ . 12345 produce ( Integer ) == 12345 """ )


CLASS( 'TYPE',
  inherit = [ 'CLAUSE' ],
  methods = [
    MS( ARG( CW( 'test' ), CG( 'ANY', 'value' ) ), """
      nom_fail( CONTEXT, "Type test method missing", $NONE ) ;
    """ ),
    MS( ARG( CW( '===' ), CG( 'TYPE', 'value' ) ), """
      if ( $CA(PARAM_value) == $CA(ACTION) ) {
        JUMP__this( CONTEXT, CONTEXT ) ;
      } else {
        nom_fail( CONTEXT, "Identity comparison === failed", $NONE ) ;
      }
    """ ),
    MS( ARG( CW( 'tid' ) ), """
      nom_fail( CONTEXT, "Type tid method missing", $NONE ) ;
    """ ),
  ]
)


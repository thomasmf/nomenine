

ROOT_SCOPE_METHOD( MD( 'Generator', 'GENERATOR_FACTORY_single()' ) )


TEST( """ let g ( Generator @ ( Closure @ () [ do [ : yield 123 ] do [ : yield 234 ] do [ : yield 345 ] do [ : yield 456 ] ] ) ) [ do [ g generate ]  g generate + ( g generate ) ] == 468 """ )
TEST( """ let g ( Generator @ ( Closure @ () [ ] ) ) [ if [ g generate ] then [ . 1 ] else [ . 2 ] ] == 2 """ )
TEST( """ let g ( Generator @ ( Closure @ () [ asdf ] ) ) [ if [ g generate ] then [ . 1 ] else [ . 2 ] ] == 2 """ )


FUNCTION( 'GENERATOR nom_generator_new( ANY action )', """
  return GENERATOR_new( nom_lock_new(), nom_reference_new( $NONE ), nom_reference_new( $NONE ), action ) ;
""" )


OBJECT( 'GENERATOR_FACTORY',
  methods = [
    MS( ARG( CW( '@' ), CG( 'ANY', 'action' ) ), """
      JUMP__return_ANY( CONTEXT, CONTEXT, $CA(nom_generator_new( PARAM_action )) ) ;
    """ ),
  ]
)

OBJECT( 'GENERATOR',
  inherit = [ 'LOCKABLE' ],
  attributes = [
    A( 'REFERENCE', 'frame' ) ,
    A( 'REFERENCE', 'context' ),
    A( 'ANY', 'action' ),
  ],
  methods = [
    MS( ARG( CW( 'generate' ) ), """
      nom_lock_lock( ACTION->lock ) ;

      ANY context = nom_reference_get( ACTION->context ) ;
      nom_reference_set( ACTION->frame, CONTEXT ) ;

      if ( context == $NONE ) {
        nom_do_sync( FRAME__TASK_new( $CA(FRAME__GENERATOR_new( $CA(ACTION->frame), ACTION )), ACTION->action, $NONE ) ) ;
      } else {
        JUMP__return_ANY( context, context, $NONE ) ;
      }
    """ ),
  ]
)

FRAME( 'GENERATOR',
  attributes = [
    A( 'GENERATOR', 'generator' ),
  ],
  methods = [
    MS( ARG( CW( 'yield' ), CG( 'ANY', 'value' ) ), """
      nom_reference_set( ACTION->generator->context, CONTEXT ) ;
      nom_lock_unlock( ACTION->generator->lock ) ;
      JUMP__return_ANY( ACTION->parent, ACTION->parent, PARAM_value ) ;
    """ ),

    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      nom_lock_unlock( ACTION->generator->lock ) ;
      nom_fail( ACTION->parent, "Generator is depleted", $NONE ) ;
    """ ),

    MS( ARG( CW( 'fail' ), CG( 'ANY', 'error' ) ), """
      nom_lock_unlock( ACTION->generator->lock ) ;
      nom_fail( ACTION->parent, "Generator failed", $NONE ) ;
    """ ),

  ]
)



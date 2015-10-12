

ROOT_SCOPE_METHOD( MD( 'Generator', 'GENERATOR_FACTORY_single()' ) )


FUNCTION( 'ANY nom_generator_new( ANY action )', """
  return $CA(GENERATOR_new( nom_reference_new( $NONE ), action )) ;
""" )


OBJECT( 'GENERATOR_FACTORY',
  methods = [
    MS( ARG( CW( '@' ), CG( 'ANY', 'action' ) ), """
      JUMP__return_ANY( CONTEXT, CONTEXT, nom_generator_new( PARAM_action ) ) ;
    """ ),
  ]
)

OBJECT( 'GENERATOR',
  inherit = [ 'LIST' ],
  attributes = [
    A( 'REFERENCE', 'context' ),
    A( 'ANY', 'action' ),
  ],
  methods = [
    MS( ARG( CW( 'value' ) ), """
      $OUT( generator value ) ;
      if ( nom_reference_get( ACTION->context ) == $NONE ) {

        $OUT( generator first value ) ;

        nom_send_message( $CA(FRAME__GENERATOR_new( CONTEXT, ACTION )), ACTION->action, ACTION->action, $NONE ) ;

      } else {

        $OUT( generator new value ) ;

        JUMP__return_ANY( $CA(FRAME__GENERATOR_new( CONTEXT, ACTION )), nom_reference_get( ACTION->context ), $NONE ) ;

      }
    """ ),
    MS( ARG( CW( 'next' ) ), """
      JUMP__return_ANY( CONTEXT, CONTEXT, $CA(ACTION) ) ;
    """ ),
  ]
)

FRAME( 'GENERATOR',
  attributes = [
    A( 'GENERATOR', 'generator' ),
  ],
  methods = [
    MS( ARG( CW( 'yield' ), CG( 'ANY', 'value' ) ), """

      $OUT( generator got value ) ;
      $LOG( PARAM_value ) ;

      nom_reference_set( ACTION->generator->context, CONTEXT ) ;
      JUMP__return_ANY( ACTION->parent, ACTION->parent, PARAM_value ) ;

    """ ),


  ]
)


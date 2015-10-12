

FUNCTION( 'void nom_send_initial_message( ANY context, ANY this, ANY that )', """
  nom_send_message( context, this, this, that ) ;
""" )

FUNCTION( 'void nom_send_message( ANY context, ANY action, ANY this, ANY that )', """
  nom_do_sync( FRAME__TASK_new( $CA(FRAME__APPLICATION_new( context, this )), action, that ) ) ;
""" )


FRAME( 'APPLICATION',
  attributes = [
    A( 'ANY', 'this' ),
  ],
  methods = [
    MS( ARG( CW( 'this' ) ), """
      JUMP__return_ANY( CONTEXT, CONTEXT, ACTION->this ) ;
    """ ),
    MS( ARG( CW( 'callerContext' ) ), """
      JUMP__return_ANY( CONTEXT, CONTEXT, $CA(ACTION->parent) ) ;
    """ ),
  ],
  dump = D( '%s %s', '$DUMP( object->this ), $DUMP( object->parent )' )
)


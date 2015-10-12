

FUNCTION( 'void nom_tid_test( ANY context, ANY t1, ANY t2 )', """
  if ( t1 == t2 ) {
    JUMP__return_ANY( context, context, t1 ) ;
  } else {
    nom_fail( context, "Test failed", $NONE ) ;
  }
""" )


OBJECT( 'TID',
  inherit = [ 'TYPE' ],
  attributes = [
    A( 'ANY', 'type' ),
  ],
  methods = [
    MS( ARG( CW( 'test' ), CG( 'ANY', 'value' ) ), """
      JUMP__EQEQEQ_TYPE( CONTEXT, PARAM_value, ACTION->type ) ;
    """ ),
    MS( ARG( CW( 'consume' ), CG( 'LIST', 'phrase' ) ), """
      nom_clause_consume( CONTEXT, $CA(ACTION), PARAM_phrase ) ;
    """ ),
  ]
)




TEST( """ if [ Integer consume [ asd 1 2 ] ] then [ . 1 ] else [ . 2 ] == 2 """ )


FUNCTION( 'void nom_clause_consume( ANY context, ANY clause, ANY phrase )', """

  $OPT(
    $IFLET( array, ARRAY_MUTABLE_NOLOCK, phrase ) ;
    $ARRAY_MUTABLE_NOLOCK__NONEMPTY( context, array ) ;
    JUMP__test_ANY( $CA(FRAME__CONSUME_2_new( context, phrase )), clause, nom_array_mutable_nolock_value( array ) ) ;
  )

  JUMP__value( $CA(FRAME__CONSUME_1_new( context, phrase, clause )), phrase ) ;

""" )


FRAME( 'CONSUME_1',
  attributes = [
    A( 'ANY', 'phrase' ),
    A( 'ANY', 'this' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      JUMP__test_ANY( $CA(FRAME__CONSUME_2_new( ACTION->parent, ACTION->phrase )), ACTION->this, PARAM_value ) ;
    """ ),
  ]
)

FRAME( 'CONSUME_2',
  attributes = [
    A( 'ANY', 'phrase' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """

      $OPT(
        $IFLET( phrase, ARRAY_MUTABLE_NOLOCK, ACTION->phrase ) ;
        JUMP__return_ANY( ACTION->parent, ACTION->parent, $CA(ELEMENT_new( PARAM_value, $CA(nom_array_mutable_nolock_next( phrase )) )) ) ;
      )

      JUMP__next( $CA(FRAME__CONSUME_3_new( ACTION->parent, PARAM_value )), ACTION->phrase ) ;
    """ ),
  ]
)

FRAME( 'CONSUME_3',
  attributes = [
    A( 'ANY', 'value' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      JUMP__return_ANY( ACTION->parent, ACTION->parent, $CA(ELEMENT_new( ACTION->value, PARAM_value )) ) ;
    """ ),
  ]
)



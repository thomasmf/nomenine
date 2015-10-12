

ROOT_SCOPE_METHOD( MD( 'RangeType', 'RANGE_TYPE_FACTORY_single()' ) )


TEST( """ Star @ ( RangeType @ 5 10 ) consume [ 5 8 9 12 1 ] value next value == 8 """ )


OBJECT( 'RANGE_TYPE_FACTORY',
  methods = [
    MS( ARG( CW( '@' ), CG( 'ANY', 'start' ), CG( 'ANY', 'stop' ) ), """
      JUMP__return_ANY( CONTEXT, CONTEXT, $CA(RANGE_TYPE_new( PARAM_start, PARAM_stop )) ) ;
    """ ),
  ]
)

OBJECT( 'RANGE_TYPE',
  inherit = [ 'TYPE' ],
  attributes = [
    A( 'ANY', 'start' ),
    A( 'ANY', 'stop' ),
  ],
  methods = [
    MS( ARG( CW( 'test' ), CG( 'ANY', 'value' ) ), """
      nom_send_nonempty_flat_phrase_message( $CA(FRAME__RANGE_TYPE_TEST_new( CONTEXT, ACTION, PARAM_value )), PARAM_value, $LISTNEW( WORD_new( ">=" ), ACTION->start ) ) ;
    """ ),

    MS( ARG( CW( 'consume' ), CG( 'LIST', 'phrase' ) ), """

      $OPT(
        $IFLET( o, ELEMENT_EMPTY, PARAM_phrase ) ;
        nom_fail( CONTEXT, "Character consume failed", $NONE ) ;
      )

      $OPT(
        $IFLET( array, ELEMENT_CHARACTERS, PARAM_phrase ) ;
        $IFLET( start, CHARACTER, ACTION->start ) ;
        $IFLET( stop, CHARACTER, ACTION->stop ) ;
        n_character param = array->data[ 0 ] ;
        if ( ( param >= start->data ) && ( param <= stop->data ) ) {
          JUMP__return_ANY( CONTEXT, CONTEXT, PARAM_phrase ) ;
        } else {
          nom_fail( CONTEXT, "Character consume failed", $NONE ) ;
        }
      )

      $OPT(
        $IFLET( array, ARRAY_MUTABLE_NOLOCK, PARAM_phrase ) ;
        $IFLET( start, INTEGER, ACTION->start ) ;
        $IFLET( stop, INTEGER, ACTION->stop ) ;
        ANY value = nom_array_mutable_nolock_value( array ) ;
        $IFLET( param, INTEGER, value ) ;
        if ( ( mpz_cmp( *start->data, *param->data ) <= 0 ) && ( mpz_cmp( *stop->data, *param->data ) >= 0 ) ) {
          JUMP__return_ANY( CONTEXT, CONTEXT, PARAM_phrase ) ;
        } else {
          nom_fail( CONTEXT, "RangeType Integer not within range", $NONE ) ;
        }
      )

      nom_clause_consume( CONTEXT, $CA(ACTION), PARAM_phrase ) ;
    """ ),

  ]
)

FRAME( 'RANGE_TYPE_TEST',
  attributes = [
    A( 'RANGE_TYPE', 'range_type' ),
    A( 'ANY', 'object' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      nom_send_nonempty_flat_phrase_message( $CA(FRAME__REPLACER_new( ACTION->parent, ACTION->object )), ACTION->range_type->stop, $LISTNEW( WORD_new( ">=" ), ACTION->object ) ) ;
    """ ),
  ]
)


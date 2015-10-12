

ROOT_SCOPE_METHOD( MD( 'Mill', 'ELEMENT_MILL_FACTORY_single()' ) )


TEST( """ Mill @ [ 1 2 1 1 3 1 1 6 7 4 ] ( Closure @ () [ if [ : that > 2 ] then [ : that * 10 ] else [ fail omg! ] ] ) next next value == 70 """ )


FUNCTION( 'ANY nom_mill_new( ANY list, ANY action )', """
  return $CA(ELEMENT_MILL_new( list, action, nom_promise_new() )) ;
""" )


OBJECT( 'ELEMENT_MILL_FACTORY',
  methods = [
    MS( ARG( CW( '@' ), CG( 'LIST', 'source' ), CG( 'ANY', 'action' ) ), """
      JUMP__return_ANY( CONTEXT, CONTEXT, $CA(ELEMENT_MILL_new( PARAM_source, PARAM_action, nom_promise_new() )) ) ;
    """ ),
  ]
)


OBJECT( 'ELEMENT_MILL',
  inherit = [ 'LIST' ],
  attributes = [
    A( 'ANY', 'source' ),
    A( 'ANY', 'action' ),
    A( 'PROMISE', 'element' ),
  ],
  methods = [
    MS( ARG( CW( 'value' ) ), """

      $PROMISE_START( ACTION->element,

        $OPT(
          $IFLET( source, ARRAY_MUTABLE_NOLOCK, ACTION->source ) ;

          if ( nom_array_mutable_nolock_size( source ) == 0 ) {
            nom_promise_set_fine( ACTION->element, ELEMENT_EMPTY_single() ) ;
            nom_fail( CONTEXT, "End of Mill source", $NONE ) ;
          } else {
            nom_do_sync( FRAME__TASK_new( $CA(FRAME__ELEMENT_MILL_GET_2_new( $CA(FRAME__ELEMENT_MILL_VALUE_new( CONTEXT, ACTION->element )), ACTION, ACTION->source )), ACTION->action, nom_array_mutable_nolock_value( source ) ) ) ;
          }
        )

        JUMP__value( $CA(FRAME__ELEMENT_MILL_GET_1_new( $CA(FRAME__ELEMENT_MILL_VALUE_new( CONTEXT, ACTION->element )), ACTION, ACTION->source )), ACTION->source ) ;
        return ;
      )

      $PROMISE_USE( ACTION->element,
        JUMP__value( CONTEXT, ACTION->element->value ) ;
      ,
        nom_fail( CONTEXT, "Error in Mill", ACTION->element->value ) ;
      )

    """ ),
    MS( ARG( CW( 'next' ) ), """

      $PROMISE_START( ACTION->element,

        $OPT(
          $IFLET( source, ARRAY_MUTABLE_NOLOCK, ACTION->source ) ;

          if ( nom_array_mutable_nolock_size( source ) == 0 ) {
            nom_promise_set_fine( ACTION->element, ELEMENT_EMPTY_single() ) ;
            JUMP__return_ANY( CONTEXT, CONTEXT, ACTION->element->value ) ;
          } else {
            nom_do_sync( FRAME__TASK_new( $CA(FRAME__ELEMENT_MILL_GET_2_new( $CA(FRAME__ELEMENT_MILL_NEXT_new( CONTEXT, ACTION->element )), ACTION, ACTION->source )), ACTION->action, nom_array_mutable_nolock_value( source ) ) ) ;
          }
        )

        JUMP__value( $CA(FRAME__ELEMENT_MILL_GET_1_new( $CA(FRAME__ELEMENT_MILL_NEXT_new( CONTEXT, ACTION->element )), ACTION, ACTION->source )), ACTION->source ) ;
        return ;
      )

      $PROMISE_USE( ACTION->element,
        JUMP__next( CONTEXT, ACTION->element->value ) ;
      ,
        nom_fail( CONTEXT, "Error in Mill", ACTION->element->value ) ;
      )

    """ ),
  ]
)


FRAME( 'ELEMENT_MILL_GET_1',
  attributes = [
    A( 'ELEMENT_MILL', 'mill' ),
    A( 'ANY', 'next' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      nom_do_sync( FRAME__TASK_new( $CA(FRAME__ELEMENT_MILL_GET_2_new( ACTION->parent, ACTION->mill, ACTION->next )), ACTION->mill->action, PARAM_value ) ) ;
    """ ),
    MS( ARG( CW( 'fail' ), CG( 'ANY', 'error' ) ), """
      nom_promise_set_fine( ACTION->mill->element, ELEMENT_EMPTY_single() ) ;
      JUMP__return_ANY( ACTION->parent, ACTION->parent, $NONE ) ;
    """ ),
  ]
)

FRAME( 'ELEMENT_MILL_GET_2',
  attributes = [
    A( 'ELEMENT_MILL', 'mill' ),
    A( 'ANY', 'next' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      $OPT(
        $IFLET( source, ARRAY_MUTABLE_NOLOCK, ACTION->next ) ;
        nom_promise_set_fine( ACTION->mill->element, $CA(ELEMENT_new( PARAM_value, nom_mill_new( $CA(nom_array_mutable_nolock_next( source )), ACTION->mill->action ) )) ) ;
        JUMP__return_ANY( ACTION->parent, ACTION->parent, $NONE ) ;
      )
      JUMP__next( $CA(FRAME__ELEMENT_MILL_RETURN_new( ACTION->parent, ACTION->mill, PARAM_value )), ACTION->next ) ;
    """ ),
    MS( ARG( CW( 'fail' ), CG( 'ANY', 'error' ) ), """
      $OPT(
        $IFLET( source, ARRAY_MUTABLE_NOLOCK, ACTION->next ) ;
        ARRAY_MUTABLE_NOLOCK next = nom_array_mutable_nolock_next( source ) ;
        if ( nom_array_mutable_nolock_size( next ) == 0 ) {
          nom_promise_set_fine( ACTION->mill->element, ELEMENT_EMPTY_single() ) ;
          JUMP__return_ANY( ACTION->parent, ACTION->parent, $NONE ) ;
        } else {
          nom_do_sync( FRAME__TASK_new(
            $CA(FRAME__ELEMENT_MILL_GET_2_new( $CA(FRAME__ELEMENT_MILL_VALUE_new( ACTION->parent, ACTION->mill->element )), ACTION->mill, $CA(next) )),
            ACTION->mill->action, nom_array_mutable_nolock_value( next )
          ) ) ;
        }
      )
      JUMP__next( $CA(FRAME__ELEMENT_MILL_SKIP_new( ACTION->parent, ACTION->mill )), ACTION->next ) ;
    """ ),
  ]
)


FRAME( 'ELEMENT_MILL_RETURN',
  attributes = [
    A( 'ELEMENT_MILL', 'mill' ),
    A( 'ANY', 'value' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      nom_promise_set_fine( ACTION->mill->element, $CA(ELEMENT_new( ACTION->value, nom_mill_new( PARAM_value, ACTION->mill->action ) )) ) ;
      JUMP__return_ANY( ACTION->parent, ACTION->parent, $NONE ) ;
    """ ),
    MS( ARG( CW( 'fail' ), CG( 'ANY', 'error' ) ), """
      nom_promise_set_fail( ACTION->mill->element, nom_error_new( ACTION->parent, "Mill failed to get next from source", PARAM_error ) ) ;
      nom_fail( ACTION->parent, "Error in Mill", ACTION->mill->element->value ) ;
    """ ),
  ]
)


FRAME( 'ELEMENT_MILL_SKIP',
  attributes = [
    A( 'ELEMENT_MILL', 'mill' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      JUMP__value( $CA(FRAME__ELEMENT_MILL_GET_1_new( ACTION->parent, ACTION->mill, PARAM_value )), PARAM_value ) ;
    """ ),
    MS( ARG( CW( 'fail' ), CG( 'ANY', 'error' ) ), """
      $OUT( skip fail ) ;
      nom_promise_set_fail( ACTION->mill->element, nom_error_new( ACTION->parent, "Mill failed to get next from source", PARAM_error ) ) ;
      nom_fail( ACTION->parent, "Error in Mill", ACTION->mill->element->value ) ;
    """ ),
  ]
)



FRAME( 'ELEMENT_MILL_VALUE',
  attributes = [
    A( 'PROMISE', 'promise' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      $PROMISE_USE( ACTION->promise,
        JUMP__value( ACTION->parent, ACTION->promise->value ) ;
      ,
        nom_fail( ACTION->parent, "Error in Mill", ACTION->promise->value ) ;
      )
    """ ),
  ]
)

FRAME( 'ELEMENT_MILL_NEXT',
  attributes = [
    A( 'PROMISE', 'promise' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      $PROMISE_USE( ACTION->promise,
        JUMP__next( ACTION->parent, ACTION->promise->value ) ;
      ,
        nom_fail( ACTION->parent, "Error in Mill", ACTION->promise->value ) ;
      )
    """ ),
  ]
)





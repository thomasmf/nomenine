

ROOT_SCOPE_METHOD( MD( 'Grouping', 'GROUPING_FACTORY_single()' ) )


# Notice that the type of object produced by Grouping clause, ArrayMutableNolock, is expected in action objectives.


OBJECT( 'GROUPING_FACTORY',
  methods = [
    MS( ARG( CW( '@' ), CG( 'LIST', 'clauses' ) ), """
      JUMP__return_ANY( CONTEXT, CONTEXT, $CA(GROUPING_new( PARAM_clauses )) ) ;
    """ ),
  ]
)

OBJECT( 'GROUPING',
  inherit = [ 'CLAUSE' ],
  attributes = [
    A( 'ANY', 'clauses' ),
  ],
  methods = [
    MS( ARG( CW( 'consume' ), CG( 'LIST', 'phrase' ) ), """

      $OPT(
        $IFLET( clauses, ARRAY_MUTABLE_NOLOCK, ACTION->clauses ) ;
        if ( nom_array_mutable_nolock_size( clauses ) == 0 ) {
          JUMP__return_ANY( CONTEXT, CONTEXT, $CA(ELEMENT_new( $CA(nom_array_mutable_nolock_new()), PARAM_phrase )) ) ;
        } else {
          JUMP__consume_LIST( $CA(FRAME__GROUPING_3_new( CONTEXT, nom_array_mutable_nolock_new(), ACTION->clauses )), nom_array_mutable_nolock_value( clauses ), PARAM_phrase ) ;
        }
      )

      JUMP__value( $CA(FRAME__GROUPING_2_new( CONTEXT, nom_array_mutable_nolock_new(), PARAM_phrase, ACTION->clauses )), ACTION->clauses ) ;
    """ ),
  ],
  dump = D( '%s', '$DUMP( object->clauses )' )
)

FRAME( 'GROUPING_2',
  attributes = [
    A( 'ARRAY_MUTABLE_NOLOCK', 'array' ),
    A( 'ANY', 'phrase' ),
    A( 'ANY', 'clauses' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      JUMP__consume_LIST( $CA(FRAME__GROUPING_3_new( ACTION->parent, ACTION->array, ACTION->clauses )), PARAM_value, ACTION->phrase ) ;
    """ ),
    MS( ARG( CW( 'fail' ), CG( 'ANY', 'error' ) ), """
      JUMP__return_ANY( ACTION->parent, ACTION->parent, $CA(ELEMENT_new( $CA(ACTION->array), ACTION->phrase )) ) ;
    """ ),
  ]
)

FRAME( 'GROUPING_3',
  attributes = [
    A( 'ARRAY_MUTABLE_NOLOCK', 'array' ),
    A( 'ANY', 'clauses' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """

      $OPT(
        $IFLET( element, ARRAY_MUTABLE_NOLOCK, PARAM_value ) ;
        $IFLET( clauses, ARRAY_MUTABLE_NOLOCK, ACTION->clauses ) ;
        nom_array_mutable_nolock_push( ACTION->array, nom_array_mutable_nolock_value( element ) ) ;

        ARRAY_MUTABLE_NOLOCK next = nom_array_mutable_nolock_next( clauses ) ;

        if ( nom_array_mutable_nolock_size( next ) == 0 ) {
          JUMP__return_ANY( ACTION->parent, ACTION->parent, $CA(ELEMENT_new( $CA(ACTION->array), $CA(nom_array_mutable_nolock_next( element )) )) ) ;
        } else {
          JUMP__consume_LIST( $CA(FRAME__GROUPING_3_new( ACTION->parent, ACTION->array, $CA(next) )), nom_array_mutable_nolock_value( next ), $CA(nom_array_mutable_nolock_next( element )) ) ;
        }

      )

      $OPT(
        $IFLET( element, ELEMENT_CHARACTERS, PARAM_value ) ;
        $IFLET( clauses, ARRAY_MUTABLE_NOLOCK, ACTION->clauses ) ;
        nom_array_mutable_nolock_push( ACTION->array, $CA(nom_element_characters_value( element )) ) ;

        ARRAY_MUTABLE_NOLOCK next = nom_array_mutable_nolock_next( clauses ) ;

        if ( nom_array_mutable_nolock_size( next ) == 0 ) {
          JUMP__return_ANY( ACTION->parent, ACTION->parent, $CA(ELEMENT_new( $CA(ACTION->array), nom_element_characters_next( element ) )) ) ;
        } else {
          JUMP__consume_LIST( $CA(FRAME__GROUPING_3_new( ACTION->parent, ACTION->array, $CA(next) )), nom_array_mutable_nolock_value( next ), nom_element_characters_next( element ) ) ;
        }

      )

      $OPT(
        $IFLET( element, ELEMENT, PARAM_value ) ;
        $IFLET( clauses, ARRAY_MUTABLE_NOLOCK, ACTION->clauses ) ;
        nom_array_mutable_nolock_push( ACTION->array, element->value ) ;

        ARRAY_MUTABLE_NOLOCK next = nom_array_mutable_nolock_next( clauses ) ;

        if ( nom_array_mutable_nolock_size( next ) == 0 ) {
          JUMP__return_ANY( ACTION->parent, ACTION->parent, $CA(ELEMENT_new( $CA(ACTION->array), element->next )) ) ;
        } else {
          JUMP__consume_LIST( $CA(FRAME__GROUPING_3_new( ACTION->parent, ACTION->array, $CA(next) )), nom_array_mutable_nolock_value( next ), element->next ) ;
        }

      )

      REFERENCE reference = nom_reference_new( $NONE ) ;
      JUMP__value( $CA(FRAME__SPLIT_new( $CA(FRAME__GROUPING_4_new( ACTION->parent, ACTION->array, ACTION->clauses, reference )), PARAM_value, reference )), PARAM_value ) ;

    """ ),
  ]
)

FRAME( 'GROUPING_4',
  attributes = [
    A( 'ARRAY_MUTABLE_NOLOCK', 'array' ),
    A( 'ANY', 'clauses' ),
    A( 'REFERENCE', 'value' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """

      nom_array_mutable_nolock_push( ACTION->array, nom_reference_get( ACTION->value ) ) ;

      JUMP__next( $CA(FRAME__GROUPING_5_new( ACTION->parent, ACTION->array, PARAM_value )), ACTION->clauses ) ;
    """ ),
  ]
)

FRAME( 'GROUPING_5',
  attributes = [
    A( 'ARRAY_MUTABLE_NOLOCK', 'array' ),
    A( 'ANY', 'phrase' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      JUMP__value( $CA(FRAME__GROUPING_2_new( ACTION->parent, ACTION->array, ACTION->phrase, PARAM_value )), PARAM_value ) ;
    """ ),
  ]
)



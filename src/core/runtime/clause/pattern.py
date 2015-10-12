

ROOT_SCOPE_METHOD( MD( 'Pattern', 'PATTERN_FACTORY_single()' ) )


OBJECT( 'PATTERN_FACTORY',
  methods = [
    MS( ARG( CW( '@' ), CG( 'LIST', 'clauses' ) ), """
      JUMP__return_ANY( CONTEXT, CONTEXT, $CA(PATTERN_new( PARAM_clauses )) ) ;
    """ ),
  ]
)

OBJECT( 'PATTERN',
  inherit = [ 'CLAUSE' ],
  attributes = [
    A( 'ANY', 'elements' ),
  ],
  methods = [
    MS( ARG( CW( 'consume' ), CG( 'LIST', 'phrase' ) ), """
//      $OUT( pattern consume ) ;
      JUMP__consume_LIST( $CA(FRAME__PATTERN_0_new( CONTEXT )), $CA(GROUPING_new( ACTION->elements )), PARAM_phrase ) ;
    """ )
  ],
  dump = D( '%s', '$DUMP( object->elements )' )
)

FRAME( 'PATTERN_0',
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """

      $OPT(
        $IFLET( element, ELEMENT, PARAM_value ) ;
        JUMP__return_ANY( ACTION->parent, ACTION->parent, $CA(ELEMENT_new( $CA(UNION_new( element->value )), element->next )) ) ;
      )

      REFERENCE reference = nom_reference_new( $NONE ) ;
      JUMP__value( $CA(FRAME__SPLIT_new( $CA(FRAME__PATTERN_1_new( ACTION->parent, reference )), PARAM_value, reference )), PARAM_value ) ;
    """ ),
  ]
)

FRAME( 'PATTERN_1',
  attributes = [
    A( 'REFERENCE', 'value' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      JUMP__return_ANY( ACTION->parent, ACTION->parent, $CA(ELEMENT_new( $CA(UNION_new( ACTION->value->value )), PARAM_value )) ) ;
    """ ),
  ]
)


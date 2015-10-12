

ROOT_SCOPE_METHOD( MD( 'Or', 'OR_CLAUSE_FACTORY_single()' ) )


OBJECT( 'OR_CLAUSE_FACTORY',
  methods = [
    MS( ARG( CW( '@' ), CG( 'LIST', 'components' ) ), """
      JUMP__return_ANY( CONTEXT, CONTEXT, $CA(OR_CLAUSE_new( PARAM_components )) ) ;
    """ ),
  ]
)


OBJECT( 'OR_CLAUSE',
  inherit = [ 'CLAUSE' ],
  attributes = [
    A( 'ANY', 'components' ),
  ],
  methods = [
    MS( ARG( CW( 'consume' ), CG( 'LIST', 'phrase' ) ), """

      $OPT(
        $IFLET( array, ARRAY_MUTABLE_NOLOCK, ACTION->components ) ;

        if ( nom_array_mutable_nolock_size( array ) == 0 ) {
          nom_fail( CONTEXT, "OrClause consume failed", $NONE ) ;
        } else {
          JUMP__consume_LIST( $CA(FRAME__OR_CLAUSE_4_new( CONTEXT, PARAM_phrase, ACTION->components )), nom_array_mutable_nolock_value( array ), PARAM_phrase ) ;
        }
      )

      JUMP__value( $CA(FRAME__OR_CLAUSE_3_new( CONTEXT, PARAM_phrase, ACTION->components )), ACTION->components ) ;
    """ ),
  ],
  dump = D( '%s', '$DUMP( object->components )' )
)

FRAME( 'OR_CLAUSE_3',
  attributes = [
    A( 'ANY', 'phrase' ),
    A( 'ANY', 'components' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      JUMP__consume_LIST( $CA(FRAME__OR_CLAUSE_4_new( ACTION->parent, ACTION->phrase, ACTION->components )), PARAM_value, ACTION->phrase ) ;
    """ ),
  ]
)

FRAME( 'OR_CLAUSE_4',
  attributes = [
    A( 'ANY', 'phrase' ),
    A( 'ANY', 'components' ),
  ],
  methods = [
    MS( ARG( CW( 'fail' ), CG( 'ANY', 'error' ) ), """

      $OPT(
        $IFLET( array, ARRAY_MUTABLE_NOLOCK, ACTION->components ) ;

        ARRAY_MUTABLE_NOLOCK next = nom_array_mutable_nolock_next( array ) ;

        if ( nom_array_mutable_nolock_size( next ) == 0 ) {
          nom_fail( ACTION->parent, "OrClause consume failed", $NONE ) ;
        } else {
          JUMP__consume_LIST( $CA(FRAME__OR_CLAUSE_4_new( ACTION->parent, ACTION->phrase, $CA(next) )), nom_array_mutable_nolock_value( next ), ACTION->phrase ) ;
        }
      )

      JUMP__next( $CA(FRAME__OR_CLAUSE_5_new( ACTION->parent, ACTION->phrase )), ACTION->components ) ;
    """ ),
  ]
)

FRAME( 'OR_CLAUSE_5',
  attributes = [
    A( 'ANY', 'phrase' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      JUMP__value( $CA(FRAME__OR_CLAUSE_3_new( ACTION->parent, ACTION->phrase, PARAM_value )), PARAM_value ) ;
    """ ),
  ]
)


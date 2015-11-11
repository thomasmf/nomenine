

ROOT_SCOPE_METHOD( MD( 'Star', 'STAR_FACTORY_single()' ) )


TEST( """ Star @ ( Integer ) consume [ 11 22 33 a b c ] value next value == 22 """ )
TEST( """ Star @ ( Integer ) consume [] """ )

TEST( """ Pattern @ ( . [ ( Word ) ( Star @ ( Integer ) ) ] flatten () ) consume [ asdf 1 2 3 asdf 111 a b c ] next next value == 111 """ )


OBJECT( 'STAR_FACTORY',
  methods = [
    MS( ARG( CW( '@' ), CG( 'CLAUSE', 'clause' ) ), """
      JUMP__return_ANY( CONTEXT, CONTEXT, $CA(STAR_new( PARAM_clause )) ) ;
    """ ),
  ]
)

OBJECT( 'STAR',
  inherit = [ 'CLAUSE' ],
  attributes = [
    A( 'ANY', 'clause' ),
  ],
  methods = [
    MS( ARG( CW( 'consume' ), CG( 'LIST', 'phrase' ) ), """
      JUMP__consume_LIST( $CA(FRAME__STAR_0_new( CONTEXT, nom_array_mutable_nolock_new(), ACTION->clause, PARAM_phrase )), ACTION->clause, PARAM_phrase ) ;
    """ ),
  ],
  dump = D( '%s', '$DUMP( object->clause )' )
)

FRAME( 'STAR_0',
  attributes = [
    A( 'ARRAY_MUTABLE_NOLOCK', 'array' ),
    A( 'ANY', 'clause' ),
    A( 'ANY', 'phrase' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """

      $OPT(
        $IFLET( characters, ELEMENT_CHARACTERS, PARAM_value ) ;
        nom_array_mutable_nolock_push( ACTION->array, $CA(nom_element_characters_value( characters )) ) ;
        ANY next = nom_element_characters_next( characters ) ;
        JUMP__consume_LIST( $CA(FRAME__STAR_0_new( ACTION->parent, ACTION->array, ACTION->clause, next )), ACTION->clause, next ) ;
      )

      $OPT(
        $IFLET( element, ELEMENT, PARAM_value ) ;
        nom_array_mutable_nolock_push( ACTION->array, element->value ) ;
        JUMP__consume_LIST( $CA(FRAME__STAR_0_new( ACTION->parent, ACTION->array, ACTION->clause, element->next )), ACTION->clause, element->next ) ;
      )

      REFERENCE reference = nom_reference_new( $NONE ) ;
      JUMP__value( $CA(FRAME__SPLIT_new( $CA(FRAME__STAR_1_new( ACTION->parent, ACTION->array, ACTION->clause, ACTION->phrase, reference )), PARAM_value, reference )), PARAM_value ) ;
    """ ),
    MS( ARG( CW( 'fail' ), CG( 'ANY', 'error' ) ), """
      JUMP__return_ANY( ACTION->parent, ACTION->parent, $CA(ELEMENT_new( $CA(ACTION->array), ACTION->phrase )) ) ;
    """ ),
  ]
)

FRAME( 'STAR_1',
  attributes = [
    A( 'ARRAY_MUTABLE_NOLOCK', 'array' ),
    A( 'ANY', 'clause' ),
    A( 'ANY', 'phrase' ),
    A( 'REFERENCE', 'value' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      nom_array_mutable_nolock_push( ACTION->array, nom_reference_get( ACTION->value ) ) ;
      JUMP__consume_LIST( $CA(FRAME__STAR_0_new( ACTION->parent, ACTION->array, ACTION->clause, PARAM_value )), ACTION->clause, PARAM_value ) ;
    """ ),
  ]
)



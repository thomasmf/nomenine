

ROOT_SCOPE_METHOD( MD( 'Character', 'CHARACTER_FACTORY_single()' ) )


TEST( """ . "abc" produce ( List ) value consume ( . [ ( . "abc" produce ( List ) value ) ] flatten () ) value """ )
TEST( """ . "a" produce ( List ) value == ( . "a" produce ( List ) value ) """ )
TEST( """ . "a" produce ( List ) value =< ( . "b" produce ( List ) value ) """ )


PRIMITIVE( 'CHARACTER',
  inherit = [ 'TOKEN', 'TYPE' ],
  attributes = [
    A( 'n_character', 'data' )
  ],
  methods = [
    MS( ARG( CW( 'test' ), CG( 'ANY', 'character' ) ), """
      JUMP__produce_TID__CHARACTER_EXTRACT_TYPE_single( $CA(FRAME__CHARACTER_TEST_new( CONTEXT, ACTION )), PARAM_character, $CA(CHARACTER_EXTRACT_TYPE_single()) ) ;
    """ ),
    MS( ARG( CW( 'consume' ), CG( 'LIST', 'phrase' ) ), """
      $OPT(
        $IFLET( array, ELEMENT_CHARACTERS, PARAM_phrase ) ;
        if ( ACTION->data == array->data[ 0 ] ) {
          JUMP__return_ANY( CONTEXT, CONTEXT, PARAM_phrase ) ;
        } else {
          nom_fail( CONTEXT, "Character consume failed", $NONE ) ;
        }
      )
      $OPT(
        $IFLET( o, ELEMENT_EMPTY, PARAM_phrase ) ;
        nom_fail( CONTEXT, "Character consume failed", $NONE ) ;
      )
      nom_clause_consume( CONTEXT, $CA(ACTION), PARAM_phrase ) ;
    """ ),

    MTID( 'STRING_EXTRACT_TYPE_single', """
      JUMP__return_ANY( CONTEXT, CONTEXT, $CA(STRING_new( nom_format_string( "%c", ACTION->data ) )) ) ;
    """ ),

    MS( ARG( CW( '==' ), CT( 'CHARACTER', 'character' ) ), """
      if ( ACTION->data == PARAM_character->data ) {
        JUMP__return_ANY( CONTEXT, CONTEXT, $CA(PARAM_character) );
      } else {
        nom_fail( CONTEXT, "Character comparison == failed", $NONE ) ;
      }
    """ ),
    MS( ARG( CW( '>=' ), CT( 'CHARACTER', 'character' ) ), """
      if ( ACTION->data >= PARAM_character->data ) {
        JUMP__return_ANY( CONTEXT, CONTEXT, $CA(PARAM_character) );
      } else {
        nom_fail( CONTEXT, "Character comparison >= failed", $NONE ) ;
      }
    """ ),
    MS( ARG( CW( '=<' ), CT( 'CHARACTER', 'character' ) ), """
      if ( ACTION->data <= PARAM_character->data ) {
        JUMP__return_ANY( CONTEXT, CONTEXT, $CA(PARAM_character) );
      } else {
        nom_fail( CONTEXT, "Character comparison =< failed", $NONE ) ;
      }
    """ ),
    MS( ARG( CW( '>' ), CT( 'CHARACTER', 'character' ) ), """
      if ( ACTION->data > PARAM_character->data ) {
        JUMP__return_ANY( CONTEXT, CONTEXT, $CA(PARAM_character) );
      } else {
        nom_fail( CONTEXT, "Character comparison > failed", $NONE ) ;
      }
    """ ),
    MS( ARG( CW( '<' ), CT( 'CHARACTER', 'character' ) ), """
      if ( ACTION->data < PARAM_character->data ) {
        JUMP__return_ANY( CONTEXT, CONTEXT, $CA(PARAM_character) );
      } else {
        nom_fail( CONTEXT, "Character comparison < failed", $NONE ) ;
      }
    """ ),
  ],
  dump = D( '\'%c\'', 'object->data' )
)

FRAME( 'CHARACTER_TEST',
  attributes = [
    A( 'CHARACTER', 'character' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'character' ) ), """
      JUMP__EQEQ_CHARACTER( ACTION->parent, $CA(ACTION->character), $C(CHARACTER,PARAM_character) ) ;
    """ ),
  ]
)


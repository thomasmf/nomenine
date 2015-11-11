

ROOT_SCOPE_METHOD( MD( 'Word', 'WORD_FACTORY_single()' ) )


PRIMITIVE( 'WORD',
  inherit = [ 'TOKEN', 'TYPE' ],
  attributes = [
    A( 'n_string', 'data' )
  ],
  methods = [
    MS( ARG( CW( 'test' ), CG( 'ANY', 'value' ) ), """
      JUMP__produce_TID__WORD_EXTRACT_TYPE_single( $CA(FRAME__WORD_TEST_new( CONTEXT, ACTION )), PARAM_value, $CA(WORD_EXTRACT_TYPE_single()) ) ;
    """ ),
    MS( ARG( CW( 'consume' ), CG( 'LIST', 'phrase' ) ), """
      $OPT(
        $IFLET( array, ARRAY_MUTABLE_NOLOCK, PARAM_phrase ) ;
        $ARRAY_MUTABLE_NOLOCK__NONEMPTY( CONTEXT, array ) ;
        ANY value = nom_array_mutable_nolock_value( array ) ;
        $IFLET( word, WORD, value ) ;
        if ( strcmp( ACTION->data, word->data ) == 0 ) {
          JUMP__return_ANY( CONTEXT, CONTEXT, PARAM_phrase );
        } else {
          nom_fail( CONTEXT, "Word consume failed", $NONE ) ;
        }
      )
      nom_clause_consume( CONTEXT, $CA(ACTION), PARAM_phrase ) ;
    """ ),
    MS( ARG( CW( '==' ), CT( 'WORD', 'word' ) ), """
      if ( strcmp( ACTION->data, PARAM_word->data ) == 0 ) {
        JUMP__return_ANY( CONTEXT, CONTEXT, $CA(PARAM_word) );
      } else {
        nom_fail( CONTEXT, "Word comparison == failed", $NONE ) ;
      }
    """ ),

    MTID_IS( 'STRING' ),
    MTID( 'STRING_EXTRACT_TYPE_single', """
      JUMP__return_ANY( CONTEXT, CONTEXT, $CA(STRING_new( ACTION->data )) ) ;
    """ ),

    MS( ARG( CW( 'serialize' ) ), """
      JUMP__return_ANY( CONTEXT, CONTEXT, $CA(STRING_new( ACTION->data )) ) ;
    """ ),
  ],
  dump = D( '\033[0;32m%s\033[0m ', 'object->data' )
)

FRAME( 'WORD_TEST',
  attributes = [
    A( 'WORD', 'word' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      JUMP__EQEQ_WORD( ACTION->parent, $CA(ACTION->word), $C(WORD,PARAM_value) ) ;
    """ ),
  ]
)


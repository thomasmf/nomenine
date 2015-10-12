

FUNCTION( 'void nom_send_flat_phrase_message( ANY context, ANY scope, ANY phrase )', """
  $OPT(
    $IFLET( array, ARRAY_MUTABLE_NOLOCK, phrase ) ;

    if ( nom_array_mutable_nolock_size( array ) == 0 ) {
      JUMP__return_ANY( context, context, scope ) ;
    } else {
      nom_send_nonempty_flat_phrase_message( context, scope, phrase ) ;
    }
  )

  JUMP__value( $CA(FRAME__SEND_PHRASE_MESSAGE_2_new( context, scope, phrase )), phrase ) ;
""" )

FUNCTION( 'void nom_send_nonempty_flat_phrase_message( ANY context, ANY scope, ANY phrase )', """
  nom_send_initial_message( $CA(FRAME__SEND_PHRASE_MESSAGE_0_new( context )), scope, phrase ) ;
""" )


FRAME( 'SEND_PHRASE_MESSAGE_0',
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """

      $OPT(
        $IFLET( element, ELEMENT, PARAM_value ) ;
        $IFLET( phrase, ARRAY_MUTABLE_NOLOCK, element->next ) ;

        if ( nom_array_mutable_nolock_size( phrase ) == 0 ) {
          JUMP__return_ANY( ACTION->parent, ACTION->parent, element->value ) ;
        } else {
          nom_send_nonempty_flat_phrase_message( ACTION->parent, element->value, element->next ) ;
        }
      )

      REFERENCE reference = nom_reference_new( $NONE ) ;
      JUMP__value( $CA(FRAME__SPLIT_new( $CA(FRAME__SEND_PHRASE_MESSAGE_1_new( ACTION->parent, reference )), PARAM_value, reference )), PARAM_value ) ;
    """ ),
  ]
)

FRAME( 'SEND_PHRASE_MESSAGE_1',
  attributes = [
    A( 'REFERENCE', 'value' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      nom_send_flat_phrase_message( ACTION->parent, ACTION->value->value, PARAM_value ) ;
    """ ),
  ],
  dump = D( '%s', '$DUMP( object->parent )' )
)

FRAME( 'SEND_PHRASE_MESSAGE_2',
  attributes = [
    A( 'ANY', 'value' ),
    A( 'ANY', 'next' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      nom_send_nonempty_flat_phrase_message( ACTION->parent, ACTION->value, ACTION->next ) ;
    """ ),
    MS( ARG( CW( 'fail' ), CG( 'ANY', 'error' ) ), """
      JUMP__return_ANY( ACTION->parent, ACTION->parent, ACTION->value ) ;
    """ ),
  ]
)


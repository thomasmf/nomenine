

FUNCTION( 'void nom_this_list_join( ANY context, STRING separator )', """
  JUMP__this( $CA(FRAME__LIST_JOIN_0_new( context, separator )), context ) ;
""" )

FUNCTION( 'void nom_list_join( ANY context, ANY list, STRING separator, STRING string  )', """
  JUMP__value( $CA(FRAME__LIST_JOIN_1_new( context, list, separator, string )), list ) ;
""" )


FRAME( 'LIST_JOIN_0',
  attributes = [
    A( 'STRING', 'separator' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      nom_list_join( ACTION->parent, PARAM_value, ACTION->separator, STRING_new( "" ) ) ;
    """ ),
  ]
)

FRAME( 'LIST_JOIN_1',
  attributes = [
    A( 'ANY', 'list' ),
    A( 'STRING', 'separator' ),
    A( 'STRING', 'string' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      JUMP__produce_TID__STRING_EXTRACT_TYPE_single( $CA(FRAME__LIST_JOIN_2_new( ACTION->parent, ACTION->list, ACTION->separator, ACTION->string )), PARAM_value, $CA(STRING_EXTRACT_TYPE_single()) ) ;
    """ ),
    MS( ARG( CW( 'fail' ), CG( 'ANY', 'error' ) ), """
      JUMP__return_ANY( ACTION->parent, ACTION->parent, $CA(ACTION->string) ) ;
    """ ),
  ]
)

FRAME( 'LIST_JOIN_2',
  attributes = [
    A( 'ANY', 'list' ),
    A( 'STRING', 'separator' ),
    A( 'STRING', 'string' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      if ( nom_string_is_empty( ACTION->string ) ) {
        JUMP__next( $CA(FRAME__LIST_JOIN_5_new( ACTION->parent, ACTION->separator, $C(STRING,PARAM_value) )), ACTION->list ) ;
      } else {
        nom_send_nonempty_flat_phrase_message( $CA(FRAME__LIST_JOIN_3_new( ACTION->parent, ACTION->list, ACTION->separator, PARAM_value )), $CA(ACTION->string), $LISTNEW( WORD_new( "+" ), ACTION->separator ) ) ;
      }
    """ ),
  ]
)

FRAME( 'LIST_JOIN_3',
  attributes = [
    A( 'ANY', 'list' ),
    A( 'STRING', 'separator' ),
    A( 'ANY', 'item' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      nom_send_nonempty_flat_phrase_message( $CA(FRAME__LIST_JOIN_4_new( ACTION->parent, ACTION->list, ACTION->separator )), PARAM_value, $LISTNEW( WORD_new( "+" ), ACTION->item ) ) ;
    """ ),
  ]
)

FRAME( 'LIST_JOIN_4',
  attributes = [
    A( 'ANY', 'list' ),
    A( 'STRING', 'separator' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      JUMP__next( $CA(FRAME__LIST_JOIN_5_new( ACTION->parent, ACTION->separator, $C(STRING,PARAM_value) )), ACTION->list ) ;
    """ ),
  ]
)

FRAME( 'LIST_JOIN_5',
  attributes = [
    A( 'STRING', 'separator' ),
    A( 'STRING', 'string' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      nom_list_join( ACTION->parent, PARAM_value, ACTION->separator, ACTION->string ) ;
    """ ),
  ]
)





FUNCTION( 'void nom_this_list_produce_string( ANY context )', """
  JUMP__this( $CA(FRAME__LIST_EXTRACT_STRING_1_new( context, STRING_new("") )), context ) ;
""" )


FRAME( 'LIST_EXTRACT_STRING_1',
  attributes = [
    A( 'STRING', 'string' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      JUMP__value( $CA(FRAME__LIST_EXTRACT_STRING_2_new( ACTION->parent, ACTION->string, PARAM_value )), PARAM_value ) ;
    """ ),
  ]
)

FRAME( 'LIST_EXTRACT_STRING_2',
  attributes = [
    A( 'STRING', 'string' ),
    A( 'ANY', 'sequence' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      JUMP__produce_TID__STRING_EXTRACT_TYPE_single( $CA(FRAME__LIST_EXTRACT_STRING_3_new( ACTION->parent, ACTION->string, ACTION->sequence )), PARAM_value, $CA(STRING_EXTRACT_TYPE_single()) ) ;
    """ ),
    MS( ARG( CW( 'fail' ), CG( 'ANY', 'error' ) ), """
      JUMP__return_ANY( ACTION->parent, ACTION->parent, $CA(ACTION->string) ) ;
    """ ),
  ]
)

FRAME( 'LIST_EXTRACT_STRING_3',
  attributes = [
    A( 'STRING', 'string' ),
    A( 'ANY', 'sequence' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      JUMP__next( $CA(FRAME__LIST_EXTRACT_STRING_1_new( ACTION->parent, STRING_new( nom_format_string( "%s%s", ACTION->string->data, $C(STRING,PARAM_value)->data ) ) )), ACTION->sequence ) ;
    """ ),
  ]
)


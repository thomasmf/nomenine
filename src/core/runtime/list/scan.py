


FUNCTION( 'void* nom_list_scan_start_routine( void* arg )', """
  FRAME__LIST_SCAN_1 frame = $C(FRAME__LIST_SCAN_1,arg) ;
  JUMP__value( $CA(frame), frame->source ) ;
  return NULL ;
""" )

FUNCTION( 'void nom_list_scan_async( FRAME__LIST_SCAN_1 frame )', """
  nom_call_async( nom_list_scan_start_routine, $CAST(void*,frame) ) ;
""" )

FUNCTION( 'void nom_list_scan( ANY context, ANY source )', """
  nom_list_scan_async( FRAME__LIST_SCAN_1_new( context, source ) ) ;
""" )



FRAME( 'LIST_SCAN_1',
  attributes = [
    A( 'ANY', 'source' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      JUMP__next( $CA(FRAME__LIST_SCAN_2_new( ACTION->parent, ACTION->source )), ACTION->source ) ;
    """ ),
    MS( ARG( CW( 'fail' ), CG( 'ANY', 'error' ) ), """
    """ ),
  ]
)

FRAME( 'LIST_SCAN_2',
  attributes = [
    A( 'ANY', 'source' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      JUMP__value( $CA(FRAME__LIST_SCAN_1_new( ACTION->parent, PARAM_value )), PARAM_value ) ;
    """ ),
  ]
)



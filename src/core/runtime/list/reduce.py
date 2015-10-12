

TEST( """ Range @ 1 10 reduce 0 ( closure [ : this + ( : that ) ] ) == 55 """ )


FUNCTION( 'void nom_list_reduce( ANY context, ANY list, ANY action, ANY sum )', """
  JUMP__value( $CA(FRAME__LIST_REDUCE_2_new( context, action, sum, list )), list ) ;
""" )


FRAME( 'LIST_REDUCE_1',
  attributes = [
    A( 'ANY', 'action' ),
    A( 'ANY', 'sum' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      nom_list_reduce( ACTION->parent, PARAM_value, ACTION->action, ACTION->sum ) ;
    """ ),
  ]
)

FRAME( 'LIST_REDUCE_2',
  attributes = [
    A( 'ANY', 'action' ),
    A( 'ANY', 'sum' ),
    A( 'ANY', 'list' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      nom_send_message( $CA(FRAME__LIST_REDUCE_3_new( ACTION->parent, ACTION->action, ACTION->list )), ACTION->action, ACTION->sum, PARAM_value ) ;
    """ ),
    MS( ARG( CW( 'fail' ), CG( 'ANY', 'error' ) ), """
      JUMP__return_ANY( ACTION->parent, ACTION->parent, ACTION->sum ) ;
    """ ),
  ]
)

FRAME( 'LIST_REDUCE_3',
  attributes = [
    A( 'ANY', 'action' ),
    A( 'ANY', 'list' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      JUMP__next( $CA(FRAME__LIST_REDUCE_1_new( ACTION->parent, ACTION->action, PARAM_value )), ACTION->list ) ;
    """ ),
  ]
)


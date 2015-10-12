

FUNCTION( 'void nom_list_eager_copy( ANY context, ANY source )', """
  JUMP__value( $CA(FRAME__LIST_EAGER_COPY_1_new( context, nom_array_mutable_nolock_new(), source )), source ) ;
""" )


FRAME( 'LIST_EAGER_COPY_1',
  attributes = [
    A( 'ARRAY_MUTABLE_NOLOCK', 'array' ),
    A( 'ANY', 'source' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      nom_array_mutable_nolock_push( ACTION->array, PARAM_value ) ;
      JUMP__next( $CA(FRAME__LIST_EAGER_COPY_2_new( ACTION->parent, ACTION->array, ACTION->source )), ACTION->source ) ;
    """ ),
    MS( ARG( CW( 'fail' ), CG( 'ANY', 'error' ) ), """
      JUMP__return_ANY( ACTION->parent, ACTION->parent, $CA(ACTION->array) ) ;
    """ ),
  ]
)

FRAME( 'LIST_EAGER_COPY_2',
  attributes = [
    A( 'ARRAY_MUTABLE_NOLOCK', 'array' ),
    A( 'ANY', 'source' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      JUMP__value( $CA(FRAME__LIST_EAGER_COPY_1_new( ACTION->parent, ACTION->array, PARAM_value )), PARAM_value ) ;
    """ ),
  ]
)



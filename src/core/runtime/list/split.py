

FRAME( 'SPLIT',
  attributes = [
    A( 'ANY', 'list' ),
    A( 'REFERENCE', 'value' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      nom_reference_set( ACTION->value, PARAM_value ) ;
      JUMP__next( ACTION->parent, ACTION->list ) ;
    """ ),
  ]
)


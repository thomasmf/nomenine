

ROOT_SCOPE_METHOD( MD( 'FlatmapObjective', 'FLATMAP_FACTORY_single()' ) )


REGISTER_FLAG( 'map_evaluation', 'evaluation uses something similar to a buffered map' )


FUNCTION( 'void nom_phrase_flatten( ANY context, ANY phrase, ANY scope )', """

  $ENABLED( map_evaluation,
    JUMP__return_ANY( context, context, nom_mill_new( phrase, $CA(FLATMAP_OBJECTIVE_new( scope )) ) ) ;
  )

  $DISABLED( map_evaluation,
    nom_list_eager_copy( context, $CA(ELEMENT_MAP_new( phrase, $CA(FLATMAP_OBJECTIVE_new( scope )) )) ) ;
  )
""" )


OBJECT( 'FLATMAP_FACTORY',
  methods = [
    MS( ARG( CW( '@' ), CG( 'ANY', 'value' ) ), """
      JUMP__return_ANY( CONTEXT, CONTEXT, $CA(FLATMAP_OBJECTIVE_new( PARAM_value )) ) ;
    """ ),
  ]
)

OBJECTIVE( 'FLATMAP_OBJECTIVE',
  attributes = [
    A( 'ANY', 'scope' ),
  ],
  objective = """
    $OPT(
      $IFLET( o, WORD, THAT ) ;
      JUMP__return_ANY( CONTEXT, CONTEXT, THAT ) ;
    )
    $OPT(
      $IFLET( expression, EXPRESSION, THAT ) ;
      nom_expression_produce_for_evaluation( CONTEXT, expression->phrase, ACTION->scope ) ;
    )
    $OPT(
      $IFLET( o, INTEGER, THAT ) ;
      JUMP__return_ANY( CONTEXT, CONTEXT, THAT ) ;
    )
    $OPT(
      $IFLET( o, STRING, THAT ) ;
      JUMP__return_ANY( CONTEXT, CONTEXT, THAT ) ;
    )
    $OPT(
      $IFLET_SUBSTRUCT( o, LIST, THAT ) ;
      JUMP__return_ANY( CONTEXT, CONTEXT, THAT ) ;
    )
    JUMP__produceForEvaluation_ANY( CONTEXT, THAT, ACTION->scope ) ;
  """
)


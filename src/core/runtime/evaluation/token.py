

OBJECT( 'TOKEN',
  methods = [
    MS( ARG( CW( 'produceForEvaluation' ), CG( 'ANY', 'scope' ) ), """
      JUMP__return_ANY( CONTEXT, CONTEXT, $CA(ACTION) ) ;
    """ ),
  ]
)


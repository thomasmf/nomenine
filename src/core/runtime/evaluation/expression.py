

REGISTER_FLAG( 'call_by_future', 'expressions are evaluated concurrently' )


FUNCTION( 'void nom_expression_produce_for_evaluation( ANY context, ANY phrase, ANY scope )', """
    $DISABLED( call_by_future,
      nom_phrase_evaluate( context, phrase, scope ) ;
    )
    $ENABLED( call_by_future,
      JUMP__return_ANY( context, context, nom_avid_new( context, $CA(STUB_new( scope, phrase )) ) ) ;
    )
""" )


PRIMITIVE( 'EXPRESSION',
  inherit = [ 'TOKEN' ],
  attributes = [
    A( 'ANY', 'phrase' )
  ],
  methods = [

    MS( ARG( CW( 'produceForEvaluation' ), CG( 'ANY', 'scope' ) ), """
      nom_expression_produce_for_evaluation( CONTEXT, ACTION->phrase, PARAM_scope ) ;
    """ ),

    MTID_IS( 'STRING' ),
    MTID( 'STRING_EXTRACT_TYPE_single', """
      $NOM( CONTEXT, ACTION->phrase,

        if [ : that value ] then [. "( " + ( Map @ ( : that ) ( Closure @ () [ : that serialize ] ) join " " ) + " )" ] else [ . "()" ]

      ) ;
    """ ),

    MS( ARG( CW( 'serialize' ) ), """
      $NOM( CONTEXT, ACTION->phrase,

        if [ : that value ] then [. "( " + ( Map @ ( : that ) ( Closure @ () [ : that serialize ] ) join " " ) + " )" ] else [ . "()" ]

      ) ;
    """ ),

  ],
  dump = D( '%s', '$DUMP( object->phrase )' )
)



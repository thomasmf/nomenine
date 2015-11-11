

ROOT_SCOPE_METHOD( MD( 'Clause', 'CLAUSE_FACTORY_single()' ) )


CLASS( 'CLAUSE',
  methods = [
    MS( ARG( CW( 'consume' ), CG( 'LIST', 'phrase' ) ), """
      nom_fail( CONTEXT, "Clause consume method missing", $NONE ) ;
    """ ),
  ]
)





ROOT_SCOPE_METHOD( MS( ARG( CW( '.' ), CG( 'ANY', 'object' ) ), """
      JUMP__return_ANY( CONTEXT, CONTEXT, PARAM_object ) ;
""" ) )


TEST( """ . 10 == 10 """ )


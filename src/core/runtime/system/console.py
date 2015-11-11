

ROOT_SCOPE_METHOD( MD( 'console', 'CONSOLE_single()' ) )


FUNCTION( 'STRING nom_read_line()', """
  char* line = NULL ;
  size_t len = 0 ;
  ssize_t read ;

  $ERROR( "Out of memory!", $CAST(n_boolean, read = ( getline( &line, &len, stdin ) != -1 ) ) ) ;

  return STRING_new( line ) ;
""" )


OBJECT( 'CONSOLE',
  methods = [
    MS( ARG( CW( 'writeLine' ), CT( 'STRING', 'string' ) ), """

      printf( "%s\\n", PARAM_string->data ) ;

      JUMP__return_ANY( CONTEXT, CONTEXT, $NONE ) ;

    """ ),

    MS( ARG( CW( 'write' ), CT( 'STRING', 'string' ) ), """

      printf( "%s", PARAM_string->data ) ;

      JUMP__return_ANY( CONTEXT, CONTEXT, $NONE ) ;

    """ ),

    MS( ARG( CW( 'readLine' ) ), """


      JUMP__return_ANY( CONTEXT, CONTEXT, $CA(nom_read_line()) ) ;

    """ ),


  ]
)



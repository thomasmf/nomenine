

ROOT_SCOPE_METHOD( MD( 'String', 'STRING_FACTORY_single()' ) )
ROOT_SCOPE_METHOD( MD( 'StringExtract', 'STRING_EXTRACT_TYPE_single()' ) )


TEST( """ . "12345" produce ( Integer ) * 2 == 24690 """ )
TEST( """ if [ . "12asd34" produce ( Integer ) ] then [ . 1 ] else [ . 2 ] == 2 """ )
TEST( """ . "Hello" + [ " to " "world" "!!!" ] == "Hello to world!!!" """ )
TEST( """ . "this = " + ( Star @ ( RangeType @ ( . "a" produce ( List ) value ) ( . "z" produce ( List ) value ) ) consume ( . "this is a test" produce ( List ) )value ) == "this = this" """ )


FUNCTION( 'n_string nom_format_string_va_list( const n_string fmt, va_list argp )', """
  n_string s ;
  if ( vasprintf( &s, fmt, argp ) == -1 ) {
    $ERROR( "Failed to produce string!" ) ;
  }
  n_string r = (n_string)nom_gcstring( s ) ;
  return r ;
""" )

FUNCTION( 'n_string nom_format_string( const n_string fmt, ... )', """
  va_list argp ;
  va_start( argp, fmt ) ;
  n_string r = nom_format_string_va_list( fmt, argp ) ;
  va_end( argp ) ;
  return r ;
""" )

FUNCTION( 'void nom_string_evaluate( ANY context, STRING string, ANY scope )', """
  nom_parse_phrase( $CA(FRAME__STRING_EVALUATE_2_new( context, scope )), $CA(nom_element_characters_new( string->data )) ) ;
""" )


PRIMITIVE( 'STRING',
  inherit = [ 'TOKEN', 'TYPE' ],
  attributes = [
    A( 'n_string', 'data' )
  ],
  methods = [
    MS( ARG( CW( 'parse' ) ), """
      nom_parse_phrase( CONTEXT, $CA(nom_element_characters_new( ACTION->data )) ) ;
    """ ),
    MS( ARG( CW( 'evaluate' ), CG( 'ANY', 'scope' ) ), """
      nom_string_evaluate( CONTEXT, ACTION, PARAM_scope ) ;
    """ ),
    MTID( 'LIST_FACTORY_single', """
      JUMP__return_ANY( CONTEXT, CONTEXT, $CA(nom_element_characters_new( ACTION->data )) ) ;
    """ ),
    MTID( 'INTEGER_FACTORY_single', """
      mpz_t* v = (mpz_t*)nom_malloc( sizeof( mpz_t ) ) ;

      if ( !mpz_init_set_str( *v, ACTION->data, 10 ) ) {
        JUMP__return_ANY( CONTEXT, CONTEXT, $CA(INTEGER_new( v )) ) ;
      } else {
        nom_fail( CONTEXT, "String to iteger failed", $NONE ) ;
      }
    """ ),

    MS( ARG( CW( '+' ), CT( 'STRING', 'value' ) ), """
        JUMP__return_ANY( CONTEXT, CONTEXT, $CA(STRING_new( nom_format_string( "%s%s", ACTION->data, PARAM_value->data ) )) ) ;
    """ ),

    MS( ARG( CW( '==' ), CT( 'STRING', 'string' ) ), """
      if ( 0 == strcmp( ACTION->data, PARAM_string->data ) ) {
        JUMP__return_ANY( CONTEXT, CONTEXT, $CA(PARAM_string) );
      } else {
        nom_fail( CONTEXT, "Strings are not equal", $NONE ) ;
      }
    """ ),
  ],
  dump = D( '\\"%s\\"', 'object->data' )
)

FRAME( 'STRING_EVALUATE_2',
  attributes = [
    A( 'ANY', 'scope' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      nom_phrase_evaluate( ACTION->parent, PARAM_value, ACTION->scope ) ;
    """ ),
  ]
)




ROOT_SCOPE_METHOD( MD( 'Integer', 'INTEGER_FACTORY_single()' ) )


TEST( """ . 10 == 10 """ )
TEST( """ . 2 + 2 == 4 """ )
TEST( """ . 2 * ( . 2 + 1 ) == 6 """ )
TEST( """ . ( . 7 + 3 ) * 3 == 30 """ )
TEST( """ . 7 + 3 * 3 == 30 """ )

TEST( """ Integer consume [ 12 13 14 ] next value == 13 """ )
TEST( """ Integer test 88 """ )

TEST( """ . 123 consume [ 123 12 1 ] value == 123 """ )


FUNCTION( 'INTEGER nom_integer_new( n_string value )', """
  mpz_t* some_integer_value = (mpz_t*)nom_malloc( sizeof( mpz_t ) ) ;
  mpz_init_set_str( *some_integer_value, value, 10 ) ;
  return INTEGER_new( some_integer_value ) ;
""" )


PRIMITIVE( 'INTEGER',
  inherit = [ 'TOKEN', 'TYPE' ],
  attributes = [
    A( 'mpz_t*', 'data' ),
  ],
  methods = [
    MS( ARG( CW( 'test' ), CG( 'ANY', 'value' ) ), """
      JUMP__produce_TID__INTEGER_EXTRACT_TYPE_single( $CA(FRAME__INTEGER_TEST_new( CONTEXT, ACTION )), PARAM_value, $CA(INTEGER_EXTRACT_TYPE_single()) ) ;
    """ ),
    MS( ARG( CW( 'consume' ), CG( 'LIST', 'phrase' ) ), """
      nom_clause_consume( CONTEXT, $CA(ACTION), PARAM_phrase ) ;
    """ ),
    MS( ARG( CW( '==' ), CT( 'INTEGER', 'integer' ) ), """
      if ( mpz_cmp( *ACTION->data, *PARAM_integer->data ) == 0 ) {
        JUMP__return_ANY( CONTEXT, CONTEXT, $CA(PARAM_integer) ) ;
      } else {
        nom_fail( CONTEXT, "Integer comparison == failed", $NONE ) ;
      }
    """ ),
    MS( ARG( CW( '!=' ), CT( 'INTEGER', 'integer' ) ), """
      if ( mpz_cmp( *ACTION->data, *PARAM_integer->data ) != 0 ) {
        JUMP__return_ANY( CONTEXT, CONTEXT, $CA(PARAM_integer) ) ;
      } else {
        nom_fail( CONTEXT, "Integer comparison != failed", $NONE ) ;
      }
    """ ),
    MS( ARG( CW( '<' ), CT( 'INTEGER', 'integer' ) ), """
      if ( mpz_cmp( *ACTION->data, *PARAM_integer->data ) < 0 ) {
        JUMP__return_ANY( CONTEXT, CONTEXT, $CA(PARAM_integer) ) ;
      } else {
        nom_fail( CONTEXT, "Integer comparison < failed", $NONE ) ;
      }
    """ ),
    MS( ARG( CW( '=<' ), CT( 'INTEGER', 'integer' ) ), """
      if ( mpz_cmp( *ACTION->data, *PARAM_integer->data ) <= 0 ) {
        JUMP__return_ANY( CONTEXT, CONTEXT, $CA(PARAM_integer) ) ;
      } else {
        nom_fail( CONTEXT, "Integer comparison =< failed", $NONE ) ;
      }
    """ ),
    MS( ARG( CW( '>' ), CT( 'INTEGER', 'integer' ) ), """
      if ( mpz_cmp( *ACTION->data, *PARAM_integer->data ) > 0 ) {
        JUMP__return_ANY( CONTEXT, CONTEXT, $CA(PARAM_integer) ) ;
      } else {
        nom_fail( CONTEXT, "Integer comparison > failed", $NONE ) ;
      }
    """ ),
    MS( ARG( CW( '>=' ), CT( 'INTEGER', 'integer' ) ), """
      if ( mpz_cmp( *ACTION->data, *PARAM_integer->data ) >= 0 ) {
        JUMP__return_ANY( CONTEXT, CONTEXT, $CA(PARAM_integer) ) ;
      } else {
        nom_fail( CONTEXT, "Integer comparison >= failed", $NONE ) ;
      }
    """ ),

    MS( ARG( CW( '+' ), CT( 'INTEGER', 'integer' ) ), """
      INTEGER v = nom_integer_new( "0" ) ;
      mpz_add( *v->data, *ACTION->data, *PARAM_integer->data ) ;
      JUMP__return_ANY( CONTEXT, CONTEXT, $CA(v) ) ;
    """ ),
    MS( ARG( CW( '++' ) ), """
      INTEGER v = nom_integer_new( "1" ) ;
      mpz_add( *v->data, *ACTION->data, *v->data ) ;
      JUMP__return_ANY( CONTEXT, CONTEXT, $CA(v) ) ;
    """ ),
    MS( ARG( CW( '-' ), CT( 'INTEGER', 'integer' ) ), """
      INTEGER v = nom_integer_new( "0" ) ;
      mpz_sub( *v->data, *ACTION->data, *PARAM_integer->data ) ;
      JUMP__return_ANY( CONTEXT, CONTEXT, $CA(v) ) ;
    """ ),
    MS( ARG( CW( '*' ), CT( 'INTEGER', 'integer' ) ), """
      INTEGER v = nom_integer_new( "0" ) ;
      mpz_mul( *v->data, *ACTION->data, *PARAM_integer->data ) ;
      JUMP__return_ANY( CONTEXT, CONTEXT, $CA(v) ) ;
    """ ),
    MS( ARG( CW( '/' ), CT( 'INTEGER', 'integer' ) ), """
      INTEGER v = nom_integer_new( "0" ) ;
      mpz_div( *v->data, *ACTION->data, *PARAM_integer->data ) ;
      JUMP__return_ANY( CONTEXT, CONTEXT, $CA(v) ) ;
    """ ),
    MTID( 'STRING_EXTRACT_TYPE_single', """
      JUMP__return_ANY( CONTEXT, CONTEXT, $CA(STRING_new( mpz_get_str( NULL, 10, *ACTION->data ) )) ) ;
    """ ),
    MTID_IS( 'STRING' ),
  ],
  dump = D( '%s', 'mpz_get_str( NULL, 10, *object->data )' )
)

FRAME( 'INTEGER_TEST',
  attributes = [
    A( 'INTEGER', 'integer' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      JUMP__EQEQ_INTEGER( ACTION->parent, $CA(ACTION->integer), $C(INTEGER,PARAM_value) ) ;
    """ ),
  ]
)


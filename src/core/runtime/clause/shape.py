

ROOT_SCOPE_METHOD(

  MD( 'Shape', 'SHAPE_FACTORY_single()' ),

  MS( ARG( CW( '::' ), CG( 'WORD', 'name' ), CG( 'CLAUSE', 'clause' ) ), """
    $NOM( CONTEXT,
      $CA(UNION_new( $LISTNEW(
        nom_definition( $CA(WORD_new( "name" )), PARAM_name ),
        nom_definition( $CA(WORD_new( "clause" )), PARAM_clause )
      ) )),
      Shape @ ( : that name ) ( : that clause )
    ) ;
  """ )

)


FUNCTION( 'ANY nom_definition( ANY clause, ANY object )', """
  return $CA(FUNCTION_new( clause, $CA(RETURNER_new( object )) )) ;
""" )


TEST( """ Shape @ x ( Any ) consume [ 1234 ] value x == 1234 """ )
TEST( """ Shape @ x ( Integer ) consume [ 1234 ] value x == 1234 """ )
TEST( """ Shape @ a ( Integer ) consume [ 1 2 ] next value == 2 """ )
TEST( """ :: a ( Integer ) consume [ 123 ] value a == 123 """ )


OBJECT( 'SHAPE_FACTORY',
  methods = [
    MS( ARG( CW( '@' ), CT( 'WORD', 'word' ), CG( 'CLAUSE', 'clause' ) ), """
      JUMP__return_ANY( CONTEXT, CONTEXT, $CA(SHAPE_new( $CA(PARAM_word), PARAM_clause )) ) ;
    """ ),
  ]
)

OBJECT( 'SHAPE',
  inherit = [ 'CLAUSE' ],
  attributes = [
    A( 'ANY', 'word' ),
    A( 'ANY', 'type' ),
  ],
  methods = [
    MS( ARG( CW( 'consume' ), CG( 'LIST', 'phrase' ) ), """
      JUMP__consume_LIST( $CA(FRAME__SHAPE_0_new( CONTEXT, ACTION->word, PARAM_phrase )), ACTION->type, PARAM_phrase ) ;
    """ ),
  ]
)

FRAME( 'SHAPE_0',
  attributes = [
    A( 'ANY', 'word' ),
    A( 'ANY', 'phrase' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      REFERENCE reference = nom_reference_new( $NONE ) ;
      JUMP__value( $CA(FRAME__SPLIT_new( $CA(FRAME__SHAPE_1_new( ACTION->parent, ACTION->word, ACTION->phrase, reference )), PARAM_value, reference )), PARAM_value ) ;
    """ ),
  ]
)

FRAME( 'SHAPE_1',
  attributes = [
    A( 'ANY', 'word' ),
    A( 'ANY', 'phrase' ),
    A( 'REFERENCE', 'value' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      JUMP__return_ANY( ACTION->parent, ACTION->parent, $CA(ELEMENT_new( nom_definition( ACTION->word, ACTION->value->value ), PARAM_value )) ) ;
    """ ),
  ]
)



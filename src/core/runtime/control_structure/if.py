

DOC_CHAPTER(
  header = 'If statements',
  topic = 'Reference',
  text = """

There are two main forms of if-statements in Nomenine.

1. Regular if-then with optional else-clause

	if [ condition ] then [ value ]

	if [ condition ] then [ value ] else [ alternative-value ]

2. The if-let statement where the result of the condition can be uses in the then-clause

	if x [ condition ] then [ do something with x ] else [ fallback ]

Notice that Nomenine does not use booleans.
Instead, the then-clause is evaluated if the condition-clause does not fail,
and if it does fail, the optional else-clause is evaluated.
For example, this means that if-statements can be use similarly to try-clauses.


  """
)


ROOT_SCOPE_METHOD(
  MC( ARG( CW( 'if' ), CT( 'WORD', 'word' ), CG( 'LIST', 'if_phrase' ), CW( 'then' ), CG( 'LIST', 'then_phrase' ), CW( 'else' ), CG( 'LIST', 'else_phrase' ) ), """
    JUMP__this( $CA(FRAME__CONDITIONALS_IF_0_new( CONTEXT, $CA(PARAM_word), PARAM_if_phrase, PARAM_then_phrase, PARAM_else_phrase )), CONTEXT ) ;
  """ ),
  MC( ARG( CW( 'if' ), CT( 'WORD', 'word' ), CG( 'LIST', 'if_phrase' ), CW( 'then' ), CG( 'LIST', 'then_phrase' ) ), """
    JUMP__this( $CA(FRAME__CONDITIONALS_IF_0_new( CONTEXT, $CA(PARAM_word), PARAM_if_phrase, PARAM_then_phrase, $NONE )), CONTEXT ) ;
  """ ),
  MC( ARG( CW( 'if' ), CG( 'LIST', 'if_phrase' ), CW( 'then' ), CG( 'LIST', 'then_phrase' ), CW( 'else' ), CG( 'LIST', 'else_phrase' ) ), """
    JUMP__this( $CA(FRAME__CONDITIONALS_IF_0_new( CONTEXT, $NONE, PARAM_if_phrase, PARAM_then_phrase, PARAM_else_phrase )), CONTEXT ) ;
  """ ),
  MC( ARG( CW( 'if' ), CG( 'LIST', 'if_phrase' ), CW( 'then' ), CG( 'LIST', 'then_phrase' ) ), """
    JUMP__this( $CA(FRAME__CONDITIONALS_IF_0_new( CONTEXT, $NONE, PARAM_if_phrase, PARAM_then_phrase, $NONE )), CONTEXT ) ;
  """ ),
  MC( ARG( CW( 'if' ), CG( 'LIST', 'if_phrase' ) ), """
    JUMP__this( $CA(FRAME__CONDITIONALS_IF_0_new( CONTEXT, $NONE, PARAM_if_phrase, $NONE, $NONE )), CONTEXT ) ;
  """ )
)


TEST( """ if [ . 1 == 2 ] """ )
TEST( """ if [ . 2 == 2 ] """ )

TEST( """ if [ . 1 == 2 ] then [ . 3 ] """ )
TEST( """ if [ . 2 == 2 ] then [ . 3 ] == 3 """ )

TEST( """ if it [ . 7 == 7 ] then [ . 3 * ( it ) ] == 21 """ )

TEST( """ if [ . 1 == 2 ] then [ . 3 ] else [ . 4 ] == 4 """ )
TEST( """ if [ . 2 == 2 ] then [ . 3 ] else [ . 4 ] == 3 """ )

TEST( """ if x [ . 2 == 2 ] then [ x + 3 ] else [ . 4 ] == 5 """ )
TEST( """ if x [ . 1 == 2 ] then [ x + 2 ] else [ . 7 ] == 7 """ )

TEST( """ if [ asdf asdf asdf ] then [ it ] else [ . 123 ] == 123 """ )


FRAME( 'CONDITIONALS_IF_0',
  attributes = [
    A( 'ANY', 'word' ),
    A( 'ANY', 'if_phrase' ),
    A( 'ANY', 'then_phrase' ),
    A( 'ANY', 'else_phrase' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      JUMP__evaluate_ANY( $CA(FRAME__CONDITIONALS_IF_1_new( ACTION->parent, PARAM_value, ACTION->word, ACTION->then_phrase, ACTION->else_phrase )), ACTION->if_phrase, PARAM_value ) ;
    """ ),
  ]
)

FRAME( 'CONDITIONALS_IF_1',
  attributes = [
    A( 'ANY', 'scope' ),
    A( 'ANY', 'word' ),
    A( 'ANY', 'then_phrase' ),
    A( 'ANY', 'else_phrase' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      if ( ACTION->then_phrase != $NONE ) {
        if ( ACTION->word != $NONE ) {
          JUMP__evaluate_ANY( ACTION->parent, ACTION->then_phrase, $CA(UNION_new( $LISTNEW( nom_definition( ACTION->word, PARAM_value ), ACTION->scope ) )) ) ;
        } else {
          JUMP__evaluate_ANY( ACTION->parent, ACTION->then_phrase, ACTION->scope ) ;
        }
      } else {
        JUMP__return_ANY( ACTION->parent, ACTION->parent, $NONE ) ;
      }
    """ ),
    MS( ARG( CW( 'fail' ), CG( 'ANY', 'error' ) ), """
      if ( ACTION->else_phrase != $NONE ) {
        JUMP__evaluate_ANY( ACTION->parent, ACTION->else_phrase, ACTION->scope ) ;
      } else {
        JUMP__return_ANY( ACTION->parent, ACTION->parent, $NONE ) ;
      }
    """ ),
  ]
)


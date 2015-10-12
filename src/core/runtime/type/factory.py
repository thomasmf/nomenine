

ROOT_SCOPE_METHOD(
  MD( 'Factory', 'FACTORY_FACTORY_single()' ),
  MO( """
    function factory ( Shape @ parameters ( Plus @ ( Clause ) ) ) ( Shape @ definition ( List ) ) [
      Factory @ ( Function @ ( Pattern @ ( : that parameters ) ) ( Closure @ ( : this ) ( : that definition ) ) )
    ]
  """ )
)


TEST( """ Factory @ ( function ( Integer ) [ : that + 10000 ] ) 100 + 1 == 10101 """ )
TEST( """ use [ ( definition TestFactory ( Factory @ ( function ( Integer ) [ : that + 10000 ] ) ) ) ] [ TestFactory consume ( list ( TestFactory 100 ) 0 0 ) value + 1 ] == 10101 """ )
TEST( """ use [ ( definition TestFactory ( Factory @ ( function ( Integer ) [ : that + 10000 ] ) ) ) ( function f ( TestFactory ) [ : that ] ) ] [ f ( TestFactory 100 ) + 1 ] == 10101 """ )



OBJECT( 'FACTORY_FACTORY',
  methods = [
    MS( ARG( CW( '@' ), CG( 'ANY', 'constructor' ) ), """
      ANY factory = $CA(FACTORY_new()) ;
      JUMP__return_ANY( CONTEXT, CONTEXT, $CA(UNION_new( $LISTNEW( factory, FACTORY_WRAPPER_new( PARAM_constructor, factory ) ) )) ) ;
    """ ),
  ]
)

OBJECT( 'FACTORY',
  inherit = [ 'TYPE' ],
  methods = [
    MS( ARG( CW( 'test' ), CG( 'ANY', 'object' ) ), """
      nom_send_nonempty_flat_phrase_message( CONTEXT, PARAM_object, $LISTNEW( WORD_new( "produce" ), $CA(ACTION) ) ) ;
    """ ),
    MS( ARG( CW( 'consume' ), CG( 'LIST', 'phrase' ) ), """
      nom_clause_consume( CONTEXT, $CA(ACTION), PARAM_phrase ) ;
    """ ),
  ]
)

OBJECTIVE( 'FACTORY_WRAPPER',
  inherit = [ 'VALUE' ],
  attributes = [
    A( 'ANY', 'factory' ),
  ],
  objective =  """
    nom_do_sync( FRAME__TASK_new( $CA(FRAME__FACTORY_SIGNER_0_new( CONTEXT, ACTION->factory )), ACTION->value, THAT ) ) ;
  """
)

FRAME( 'FACTORY_SIGNER_0',
  attributes = [
    A( 'ANY', 'factory' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      REFERENCE reference = nom_reference_new( $NONE ) ;
      JUMP__value( $CA(FRAME__SPLIT_new( $CA(FRAME__FACTORY_SIGNER_1_new( ACTION->parent, ACTION->factory, reference )), PARAM_value, reference )), PARAM_value ) ;
    """ ),
  ]
)

FRAME( 'FACTORY_SIGNER_1',
  attributes = [
    A( 'ANY', 'factory' ),
    A( 'REFERENCE', 'value' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      FUNCTION f = FUNCTION_new( $CA(PATTERN_new( $LISTNEW( WORD_new( "produce" ), TID_new( ACTION->factory ) ) )), $CA(RETURN_THIS_new()) ) ;
      ANY u = $CA(UNION_new( $LISTNEW( f, ACTION->value->value ) )) ;
      JUMP__return_ANY( ACTION->parent, ACTION->parent, $CA(ELEMENT_new( u, PARAM_value )) ) ;
    """ ),
  ]
)


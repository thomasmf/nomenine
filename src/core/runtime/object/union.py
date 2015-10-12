

ROOT_SCOPE_METHOD(
  MD( 'Union', 'UNION_FACTORY_single()' ),
  MO( """
    function union ( :: elements ( Star @ ( Any ) ) ) [
      Union @ ( : that elements )
    ]
  """ )
)


TEST( """ Union @ [ asdf 1 2 3 ] + 1 == 2 """ )
TEST( """ . 123 + ( Union @ [ 1000 ] ) == 1123 """ )
TEST( """ . ( union ( function a [ . 1 ] ) ( function b [ . 2 ] ) ( function c [ . 3 ] ) ) b == 2 """ )


OBJECT( 'UNION_FACTORY',
  methods = [
    MS( ARG( CW( '@' ), CG( 'LIST', 'components' ) ), """
      JUMP__return_ANY( CONTEXT, CONTEXT, $CA(UNION_new( PARAM_components )) ) ;
    """ ),
    ]
 )

OBJECTIVE( 'UNION',
  attributes = [
    A( 'ANY', 'components' ),
  ],
  objective = """

    $OPT(
      $IFLET( components, ARRAY_MUTABLE_NOLOCK, ACTION->components ) ;
      if ( nom_array_mutable_nolock_size( components ) == 0 ) {
        nom_fail( CONTEXT, "Empty union", $NONE ) ;
      } else {
        nom_do_sync( FRAME__TASK_new( $CA(FRAME__UNION_4_new( CONTEXT, THAT, ACTION->components )), nom_array_mutable_nolock_value( components ), THAT ) ) ;
      }
    )

    JUMP__value( $CA(FRAME__UNION_3_new( CONTEXT, THAT, ACTION->components )), ACTION->components ) ;
  """,
  dump = D( 'components:%s', '$DUMP( object->components )' )
)

FRAME( 'UNION_3',
  attributes = [
    A( 'ANY', 'phrase' ),
    A( 'ANY', 'components' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      nom_do_sync( FRAME__TASK_new( $CA(FRAME__UNION_4_new( ACTION->parent, ACTION->phrase, ACTION->components )), PARAM_value, ACTION->phrase ) ) ;
    """ ),

  ],
  dump = D( '%s', '$DUMP( object->parent )' )
)

FRAME( 'UNION_4',
  attributes = [
    A( 'ANY', 'phrase' ),
    A( 'ANY', 'components' ),
  ],
  methods = [
    MS( ARG( CW( 'fail' ), CG( 'ANY', 'error' ) ), """

      $OPT(
        $IFLET( components, ARRAY_MUTABLE_NOLOCK, ACTION->components ) ;

        ARRAY_MUTABLE_NOLOCK next = nom_array_mutable_nolock_next( components ) ;

        if ( nom_array_mutable_nolock_size( next ) == 0 ) {
          nom_fail( ACTION->parent, "Depleted union", $NONE ) ;
        } else {
          nom_do_sync( FRAME__TASK_new( $CA(FRAME__UNION_4_new( ACTION->parent, ACTION->phrase, $CA(next) )), nom_array_mutable_nolock_value( next ), ACTION->phrase ) ) ;
        }
      )

      JUMP__next( $CA(FRAME__UNION_5_new( ACTION->parent, ACTION->phrase )), ACTION->components ) ;
    """ ),
  ],
  dump = D( '%s', '$DUMP( object->parent )' )
)

FRAME( 'UNION_5',
  attributes = [
    A( 'ANY', 'phrase' ),
  ],
  methods = [
    MS( ARG( CW( 'return' ), CG( 'ANY', 'value' ) ), """
      JUMP__value( $CA(FRAME__UNION_3_new( ACTION->parent, ACTION->phrase, PARAM_value )), PARAM_value ) ;
    """ ),
  ]
)


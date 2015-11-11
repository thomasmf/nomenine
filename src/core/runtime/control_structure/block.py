

TEST( """ with ( function x1 [ . 40 ] ) [ x1 ] == 40 """ )

TEST( """ let x1 30 [ x1 * 10 ] == 300 """ )

TEST( """ use [ [ definition x 387 ] [ definition y 4123 ] [ function f [ x + 1000 ] ] ] [ f * ( y ) ] == 5718601 """ )

TEST( """ use [ [ definition TestFactory ( factory ( Integer ) [ : that + 10000 ] ) ] [ function f ( TestFactory ) [ : that ] ] ] [ f ( TestFactory 100 ) + 1 ] == 10101 """ )


ROOT_SCOPE_METHOD(


  MC( ARG( CW( 'with' ), CG( 'ANY', 'scope' ), CG( 'LIST', 'phrase' ) ), """

    $NOM( CONTEXT,

      $CA(UNION_new( $LISTNEW(
        nom_definition( $CA(WORD_new( "scope" )), PARAM_scope ),
        nom_definition( $CA(WORD_new( "phrase" )), PARAM_phrase )
      ) )),

      : that phrase evaluate ( union
        ( : that scope )
        ( : this )
      )

    ) ;

  """ ),


  MC( ARG( CW( 'let' ), CG( 'WORD', 'name' ), CG( 'ANY', 'value' ), CG( 'LIST', 'phrase' ) ), """

    $NOM( CONTEXT,

      $CA(UNION_new( $LISTNEW(
        nom_definition( $CA(WORD_new( "name" )), PARAM_name ),
        nom_definition( $CA(WORD_new( "value" )), PARAM_value ),
        nom_definition( $CA(WORD_new( "phrase" )), PARAM_phrase )
      ) )),

      : this with ( definition ( : that name ) ( : that value ) ) ( : that phrase )

    ) ;

  """ ),


  MC( ARG( CW( 'block' ), CG( 'ANY', 'scope' ), CG( 'LIST', 'components' ) ), """

    $NOM( CONTEXT,

      $CA(UNION_new( $LISTNEW(
        nom_definition( $CA(WORD_new( "scope" )), PARAM_scope ),
        nom_definition( $CA(WORD_new( "components" )), PARAM_components )
      ) )),


      if value [ : that components value ]

      then [

        let scope ( union ( : that scope ) ( value evaluate ( : that scope ) ) ) [

          : this block ( scope ) ( : that components next )

        ]

      ]

      else [

        : that scope

      ]

    ) ;

  """ ),


  MC( ARG( CW( 'use' ), CG( 'LIST', 'components' ), CG( 'LIST', 'phrase' ) ), """

    $NOM( CONTEXT,

      $CA(UNION_new( $LISTNEW(
        nom_definition( $CA(WORD_new( "components" )), PARAM_components ),
        nom_definition( $CA(WORD_new( "phrase" )), PARAM_phrase )
      ) )),

      : this with ( : this block ( : this ) ( : that components ) ) ( : that phrase )

    ) ;

  """ )


)



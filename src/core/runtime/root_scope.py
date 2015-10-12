

TEST( """ function b [ . 100 ] b == 100 """ )


ROOT_SCOPE_METHOD( MO( """
  Function @
    ( Pattern @ ( . [
      function
      ( Shape @ parameters ( Plus @ ( Clause ) ) )
      ( Shape @ definition ( List ) )
    ] flatten () ) )
    ( Closure @ () [ Function @ ( Pattern @ ( : that parameters ) ) ( Closure @ ( : this ) ( : that definition ) ) ] )
""" ) )

ROOT_SCOPE_METHOD( MO( """
  function :: ( Shape @ name ( Word ) ) ( Shape @ clause ( Clause ) ) [
    Shape @ ( : that name ) ( : that clause )
  ]
""" ) )

ROOT_SCOPE_METHOD( MO( """
  function definition ( :: name ( Word ) ) ( :: value ( Any ) ) [
    Function @ ( : that name ) ( Stub @ ( : that value ) [] )
  ]
""" ) )



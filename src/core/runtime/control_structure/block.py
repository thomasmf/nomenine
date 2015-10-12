

TEST( """ with ( function x1 [ . 40 ] ) [ x1 ] == 40 """ )
TEST( """ let x1 30 [ x1 * 10 ] == 300 """ )
TEST( """ use [ ( definition x 387 ) ( definition y 4123 ) ( function f [ x + 1000 ] ) ] [ f * ( y ) ] == 5718601 """ )
TEST( """ use [ ( definition TestFactory ( factory ( Integer ) [ : that + 10000 ] ) ) ( function f ( TestFactory ) [ : that ] ) ] [ f ( TestFactory 100 ) + 1 ] == 10101 """ )


ROOT_SCOPE_METHOD(
  MO( """
    function with ( :: object ( Any ) ) ( :: block ( List ) ) [
      : that block evaluate ( union
        ( : that object )
        ( : this )
      )
    ]
  """ ),
  MO( """
    function let ( :: name ( Word ) ) ( :: value ( Any ) ) ( :: block ( List ) ) [
      : this with ( definition ( : that name ) ( : that value ) ) ( : that block )
    ]
  """ ),
  MO( """
    function use ( :: components ( List ) ) ( :: block ( List ) ) [
      : this with ( ReflectiveUnion @ ( : this ) ( : that components ) ) ( : that block )
    ]
  """ )
)


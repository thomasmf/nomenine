

DOC_CHAPTER(
  header = 'Overview',
  text = """

$DOC_PURPOSE(
This chapter gives an overview of syntax and semantics without going into any details.
)


$DOC_HEADER( Expressions )

Nomenine syntax does not look very different from most languages:

$DOC_CODE(
someNumber + 1
)

Expressions uses parenthesis:

$DOC_CODE(
someNumber + ( someOtherNumber * 10 )
)

Object attributes are not accessed using dot-notation.
Instead the components of a path is simply separated by spaces:

$DOC_CODE(
someObject someAttribute someAttributeOfThatAttribute
)

Expressions are paths.
However a component of a path may be a pattern that spans many components of an expression.

Since expressions are paths,
there must be an object at the beginning of that path.
This object is the scope.

$DOC_CODE(
x + ( y )
)

Notice the use of parenthesis around $DOC_WORD( y ).
This parenthesis is not optional.
The reason is that $DOC_WORD( y ) is acquired from scope.
Parenthesis are not optional, they either must be included or must be omitted.
The important point here is that expressions are paths that originates from the scope object.


$DOC_HEADER( Quoting )

Nomenine is very focused on consistency.
So much in fact that integer literals have no special meaning in scope.
To get a number, use the identity function $DOC_WORD( . ):

$DOC_CODE(
. 2 + 2
)

Will return $DOC_WORD( 4 ).

Similarly, words and quoted expressions can be quoted.
Expressions can not be quoted because they are evaluated implicitly:

$DOC_CODE(
. ( a + 1 )
)

Will return the result of $DOC_PHRASE( a + 1 ) and not the expression object itself.
It is equivalent to:

$DOC_CODE(
a + 1
)

$DOC_HEADER( Functions )

Functions can be created using $DOC_WORD( function ):

$DOC_CODE(
function ( Integer ) [ : that * 2 ]
)

Notice the use of $DOC_WORD( [ ] ).
The brackets are used to quote code.
The quoted code becomes the body of the function.
Quoted code is an ordinary list object.

Notice in the last example the use of $DOC_WORD( : ).
$DOC_WORD( : ) refers to the context.

The word $DOC_WORD( that ) refers to the message object in the context.
Similarly there is a word $DOC_WORD( this ) which is used as expected.


$DOC_HEADER( Clauses )

$DOC_WORD( Integer ) in the previous example is a $DOC_WORD( Clause ) object.
It says that the function takes an integer as an argument.
The role of clause objects in Nomenine is similar to types or classes in many other languages.

However clause objects are more about the pattern matching then types.
Clause objects can $DOC_QUOTE( consume ) more than one object in the phrase,
and use the consumed objects to produce a result in any way.

The main types of clause objects are:

$DOC_LIST_ITEMS(
  $DOC_ITEM( Star,
    This is Kleene Star. It will consume all objects of a given type, and return them as a list.
  )
  $DOC_ITEM( Plus,
    $DOC_WORD( Plus ) is similar to $DOC_WORD( Star ) only that it requires the list of matched objects to be non-empty.
  )
  $DOC_ITEM( Grouping,
    This consumes a objects matching a particular pattern of $DOC_WORD( Clause ) objects.
    A list of matches is returned.
  )
  $DOC_ITEM( Pattern,
    This is similar to $DOC_WORD( Grouping ) except that it returns a $DOC_WORD( Union ) of the matches.
  )
  $DOC_ITEM( Shape,
    This is used with $DOC_WORD( Pattern ) to name matches.
    Using $DOC_WORD( Shape ) one can refer to specific matches in a pattern by name.
    This is how multiple parameters to functions are handled.
  )
  $DOC_ITEM( any word,
    A word object will consume/match itself.
    This way words can be used in patterns.
  )
)

When building a function, the objects between $DOC_WORD( function ) and the quoted expression are used to form a pattern.
In the following function, the pattern consists of the word $DOC_WORD( f ) followed by the $DOC_WORD( Integer ) clause object:

$DOC_CODE(
  function f ( Integer ) [ : that + 4 ]
)

$DOC_HEADER( Methods )

Objects are functions and objects that understand more than one type of message are polymorphic functions.
Polymorphic functions are just unions of functions.
Using words as clauses makes it possible to use the components of a polymorphic function as a method.

The following object is a union of two functions:

$DOC_CODE(
union
  ( function f1 ( Integer ) [ : that + 2 ] )
  ( function f2 ( Integer ) [ : that + 4 ] )
)

To use the first function, one sends a message like $DOC_PHRASE( f1 123 ) to the object.
To use the other function, one sends a message like $DOC_PHRASE( f2 123 ) to the object.
The fact that the words $DOC_WORD( f1 ) and $DOC_WORD( f2 ) are part of the patterns of each function makes it possible to distinguish between them.


$DOC_HEADER( Let and with )

Most objects are immutable.
It is therefore natural to use $DOC_WORD( let ) or similar:

$DOC_CODE(
let someInteger ( 123 ) [
  someInteger + 2
]
)

Notice that the type of $DOC_WORD( someInteger ) is not specified.

The object oriented version of $DOC_WORD( let ) becomes $DOC_WORD( with ).
It is similar to $DOC_QUOTE( let* ).
It is possible to have more than one definition:

$DOC_CODE(
with ( union
  ( function f ( Integer ) [ : that + 4 ] )
  ( function x [ . 100 ] )
  ()
) [
  f ( x )
]
)

$DOC_WORD( with ) takes an object and a list as its arguments.
The list is the expression.
The object is scope that will be used in the evaluation of the expression.

Notice the empty parenthesis.
Recall that the initial object in an expression is the scope.
The empty parenthesis is scope.
The reason for using it in the union, specifically at the end,
is to make the new scope inherit the parent scope.
Therefore the two functions in addition to everything in the original scope is available in the expression.



$DOC_HEADER( If )

If-statements are expressions.
Also, there is no booleans or boolean logic.
If the condition fails, the else-branch is taken,
and if the condition produces a result, the then-branch is taken.

$DOC_CODE(
if [ x < 10 ] then [ y ] else [ z ]
)

It is possible to name that result and refer to it in the then-branch:

Here $DOC_WORD( y ) is returned if $DOC_PHRASE( x < 10 ) does not fail.
Otherwise $DOC_WORD( z ) is returned.


$DOC_HEADER( Mutable objects )

There are sparse facilities for mutable objects and imperatives:

$DOC_CODE(
do [ x = 10 ]
do [ y = ( x + 2 ) ]
)

$DOC_WORD( do ) evaluates the expression given and returns its $DOC_WORD( this ),
which is usually scope.
In order for the assignments to work, the objects $DOC_WORD( x ) and $DOC_WORD( y ) must understand those messages.

$DOC_HEADER( Loops )

There are currently no loop mechanism, but it is possible to use $DOC_WORD( Range ) and $DOC_WORD( reduce )

$DOC_CODE(
Range @ 1 9 reduce 1 [ : this + ( : that ) ]
)

This calculates the factorial of $DOC_WORD( 9 ).
Notice that $DOC_PHRASE( : this ) refers to the sum while $DOC_PHRASE( : that ) refers to the current element.

Also notice that $DOC_WORD( @ ) is the equivalent of $DOC_QUOTE( new ) as used in object-oriented programming languages.

  """,

 ),



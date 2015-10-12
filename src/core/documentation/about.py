
DOC_CHAPTER(
  header = 'About',
  text = """


Nomenine is a homo-iconic, object-oriented programming language with pattern matching, multiple inheritance and polymorphism.

Most objects are immutable.
Nomenine handles similarly to functional programming languages in many respects.
There is also room for mutable objects and imperatives.

Everything in Nomenine is an object.
Objects are closures that capture their attributes.
The object as a function takes a context containing a message as its only parameter.
It deals with the message, and sends a responds message to the context.

Nomenine is a dynamically typed language.
Clauses are used to control pattern matching which is used to control polymorphism.
Clauses can be seen as the syntactic equivalent of types.

Range and Kleene star are among the available clauses.
Clauses can be defined in the language itself.
The parser is a clause.

Nomenine is not compiled, but it is not really an interpreted language either.
There is no interpretation loop with a switch in it.
The interpretation of an expression is the result of a ricochet of messages sent between objects.
The sending of a message is also the result of a ricochet of messages sent between objects.
This causes circularity,
but Nomenine handles this circularity automatically,
allowing every component of the system to behave as perfectly ordinary high-level user-space components.

Built-in components and user-space components are always interchangeable.

Other especially noteworthy features are lazy objects and maps, promises and map/reduce.
There are other significant features planned.

$DOC_RELATED( Features, Content, Overview, Tutorial )

  """
)

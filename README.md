
<html>
<head>
<link rel="stylesheet" href="github_markdown.css">
</head>
<body class="markdown-body">
<h2 id="Nomenine"> Nomenine</h2>
<h6 ><a href="src/core/documentation/root.py">src/core/documentation/root.py</a></h6>

<hr>
<h3 id="About">1 About</h3>
<h6 ><a href="src/core/documentation/about.py">src/core/documentation/about.py</a></h6>

<p>
Nomenine is a homo-iconic, object-oriented programming language with pattern matching, multiple inheritance and polymorphism.
</p>


<p>
Most objects are immutable.
Nomenine handles similarly to functional programming languages in many respects.
There is also room for mutable objects and imperatives.
</p>


<p>
Everything in Nomenine is an object.
Objects are closures that capture their attributes.
The object as a function takes a context containing a message as its only parameter.
It deals with the message, and sends a responds message to the context.
</p>


<p>
Nomenine is a dynamically typed language.
Clauses are used to control pattern matching which is used to control polymorphism.
Clauses can be seen as the syntactic equivalent of types.
</p>


<p>
Range and Kleene star are among the available clauses.
Clauses can be defined in the language itself.
The parser is a clause.
</p>


<p>
Nomenine is not compiled, but it is not really an interpreted language either.
There is no interpretation loop with a switch in it.
The interpretation of an expression is the result of a ricochet of messages sent between objects.
The sending of a message is also the result of a ricochet of messages sent between objects.
This causes circularity,
but Nomenine handles this circularity automatically,
allowing every component of the system to behave as perfectly ordinary high-level user-space components.
</p>


<p>
Built-in components and user-space components are always interchangeable.
</p>


<p>
Other especially noteworthy features are lazy objects and maps, promises and map/reduce.
There are other significant features planned.
</p>


<p>
<strong>Related:</strong> <a href="#Features">Features</a>, <a href="#Content">Content</a>, <a href="#Overview">Overview</a>, <a href="#Tutorial">Tutorial</a>
</p>

<hr>
<h3 id="Example">2 Example</h3>
<h6 ><a href="src/core/documentation/example.py">src/core/documentation/example.py</a></h6>

<p>
This is what it looks like:
</p>


<p>

<pre><code>let sort ( function ( List ) [

  let l ( : that next ) [

    if pivot [ : that value ] then [

      merge

        ( sort ( filter ( l ) [ : that =< ( pivot ) ] ) )

        ( list ( pivot ) )

        ( sort ( filter ( l ) [ : that > ( pivot ) ] ) )

    ] else [ list ]

  ]

] ) [

  sort ( list 4 2 5 7 4 2 )

]</code></pre>

</p>

<hr>
<h3 id="Content">3 Content</h3>
<h6 ><a href="src/core/documentation/root.py">src/core/documentation/root.py</a></h6>
<h4 >1 <a href="#About">About</a></h4>


<h4 >2 <a href="#Example">Example</a></h4>


<h4 >3 <a href="#Content">Content</a></h4>
<h4 >4 <a href="#Features">Features</a></h4>


<h4 >5 <a href="#Overview">Overview</a></h4>


<h4 >6 <a href="#Tutorial">Tutorial</a></h4>


<h4 >7 <a href="#Reference">Reference</a></h4>

<h5 >7.1 <a href="#If_statements">If statements</a></h5>


<hr>
<h3 id="Features">4 Features</h3>
<h6 ><a href="src/core/documentation/features.py">src/core/documentation/features.py</a></h6>

<hr>
<h3 id="Overview">5 Overview</h3>
<h6 ><a href="src/core/documentation/overview.py">src/core/documentation/overview.py</a></h6>

<p>
<em>This chapter gives an overview of syntax and semantics without going into any details.</em>
</p>


<p>
<h6 >Expressions</h6>
</p>


<p>
Nomenine syntax does not look very different from most languages:
</p>


<p>

<pre><code>someNumber + 1</code></pre>

</p>


<p>
Expressions uses parenthesis:
</p>


<p>

<pre><code>someNumber + ( someOtherNumber * 10 )</code></pre>

</p>


<p>
Object attributes are not accessed using dot-notation.
Instead the components of a path is simply separated by spaces:
</p>


<p>

<pre><code>someObject someAttribute someAttributeOfThatAttribute</code></pre>

</p>


<p>
Expressions are paths.
However a component of a path may be a pattern that spans many components of an expression.
</p>


<p>
Since expressions are paths,
there must be an object at the beginning of that path.
This object is the scope.
</p>


<p>

<pre><code>x + ( y )</code></pre>

</p>


<p>
Notice the use of parenthesis around <strong>y</strong>.
This parenthesis is not optional.
The reason is that <strong>y</strong> is acquired from scope.
Parenthesis are not optional, they either must be included or must be omitted.
The important point here is that expressions are paths that originates from the scope object.
</p>


<p>
<h6 >Quoting</h6>
</p>


<p>
Nomenine is very focused on consistency.
So much in fact that integer literals have no special meaning in scope.
To get a number, use the identity function <strong>.</strong>:
</p>


<p>

<pre><code>. 2 + 2</code></pre>

</p>


<p>
Will return <strong>4</strong>.
</p>


<p>
Similarly, words and quoted expressions can be quoted.
Expressions can not be quoted because they are evaluated implicitly:
</p>


<p>

<pre><code>. ( a + 1 )</code></pre>

</p>


<p>
Will return the result of <code>a + 1</code> and not the expression object itself.
It is equivalent to:
</p>


<p>

<pre><code>a + 1</code></pre>

</p>


<p>
<h6 >Functions</h6>
</p>


<p>
Functions can be created using <strong>function</strong>:
</p>


<p>

<pre><code>function ( Integer ) [ : that * 2 ]</code></pre>

</p>


<p>
Notice the use of <strong>[ ]</strong>.
The brackets are used to quote code.
The quoted code becomes the body of the function.
Quoted code is an ordinary list object.
</p>


<p>
Notice in the last example the use of <strong>:</strong>.
<strong>:</strong> refers to the context.
</p>


<p>
The word <strong>that</strong> refers to the message object in the context.
Similarly there is a word <strong>this</strong> which is used as expected.
</p>


<p>
<h6 >Clauses</h6>
</p>


<p>
<strong>Integer</strong> in the previous example is a <strong>Clause</strong> object.
It says that the function takes an integer as an argument.
The role of clause objects in Nomenine is similar to types or classes in many other languages.
</p>


<p>
However clause objects are more about the pattern matching then types.
Clause objects can <em>consume</em> more than one object in the phrase,
and use the consumed objects to produce a result in any way.
</p>


<p>
The main types of clause objects are:
</p>


<p>
<dl><dt>Star</dt><dd>This is Kleene Star. It will consume all objects of a given type, and return them as a list.</dd>
  <dt>Plus</dt><dd><strong>Plus</strong> is similar to <strong>Star</strong> only that it requires the list of matched objects to be non-empty.</dd>
  <dt>Grouping</dt><dd>This consumes a objects matching a particular pattern of <strong>Clause</strong> objects.
    A list of matches is returned.</dd>
  <dt>Pattern</dt><dd>This is similar to <strong>Grouping</strong> except that it returns a <strong>Union</strong> of the matches.</dd>
  <dt>Shape</dt><dd>This is used with <strong>Pattern</strong> to name matches.
    Using <strong>Shape</strong> one can refer to specific matches in a pattern by name.
    This is how multiple parameters to functions are handled.</dd>
  <dt>any word</dt><dd>A word object will consume/match itself.
    This way words can be used in patterns.</dd></dl>
</p>


<p>
When building a function, the objects between <strong>function</strong> and the quoted expression are used to form a pattern.
In the following function, the pattern consists of the word <strong>f</strong> followed by the <strong>Integer</strong> clause object:
</p>


<p>

<pre><code>function f ( Integer ) [ : that + 4 ]</code></pre>

</p>


<p>
<h6 >Methods</h6>
</p>


<p>
Objects are functions and objects that understand more than one type of message are polymorphic functions.
Polymorphic functions are just unions of functions.
Using words as clauses makes it possible to use the components of a polymorphic function as a method.
</p>


<p>
The following object is a union of two functions:
</p>


<p>

<pre><code>union
  ( function f1 ( Integer ) [ : that + 2 ] )
  ( function f2 ( Integer ) [ : that + 4 ] )</code></pre>

</p>


<p>
To use the first function, one sends a message like <code>f1 123</code> to the object.
To use the other function, one sends a message like <code>f2 123</code> to the object.
The fact that the words <strong>f1</strong> and <strong>f2</strong> are part of the patterns of each function makes it possible to distinguish between them.
</p>


<p>
<h6 >Let and with</h6>
</p>


<p>
Most objects are immutable.
It is therefore natural to use <strong>let</strong> or similar:
</p>


<p>

<pre><code>let someInteger ( 123 ) [
  someInteger + 2
]</code></pre>

</p>


<p>
Notice that the type of <strong>someInteger</strong> is not specified.
</p>


<p>
The object oriented version of <strong>let</strong> becomes <strong>with</strong>.
It is similar to <em>let*</em>.
It is possible to have more than one definition:
</p>


<p>

<pre><code>with ( union
  ( function f ( Integer ) [ : that + 4 ] )
  ( function x [ . 100 ] )
  ()
) [
  f ( x )
]</code></pre>

</p>


<p>
<strong>with</strong> takes an object and a list as its arguments.
The list is the expression.
The object is scope that will be used in the evaluation of the expression.
</p>


<p>
Notice the empty parenthesis.
Recall that the initial object in an expression is the scope.
The empty parenthesis is scope.
The reason for using it in the union, specifically at the end,
is to make the new scope inherit the parent scope.
Therefore the two functions in addition to everything in the original scope is available in the expression.
</p>


<p>
<h6 >If</h6>
</p>


<p>
If-statements are expressions.
Also, there is no booleans or boolean logic.
If the condition fails, the else-branch is taken,
and if the condition produces a result, the then-branch is taken.
</p>


<p>

<pre><code>if [ x < 10 ] then [ y ] else [ z ]</code></pre>

</p>


<p>
It is possible to name that result and refer to it in the then-branch:
</p>


<p>
Here <strong>y</strong> is returned if <code>x < 10</code> does not fail.
Otherwise <strong>z</strong> is returned.
</p>


<p>
<h6 >Mutable objects</h6>
</p>


<p>
There are sparse facilities for mutable objects and imperatives:
</p>


<p>

<pre><code>do [ x = 10 ]
do [ y = ( x + 2 ) ]</code></pre>

</p>


<p>
<strong>do</strong> evaluates the expression given and returns its <strong>this</strong>,
which is usually scope.
In order for the assignments to work, the objects <strong>x</strong> and <strong>y</strong> must understand those messages.
</p>


<p>
<h6 >Loops</h6>
</p>


<p>
There are currently no loop mechanism, but it is possible to use <strong>Range</strong> and <strong>reduce</strong>
</p>


<p>

<pre><code>Range @ 1 9 reduce 1 [ : this + ( : that ) ]</code></pre>

</p>


<p>
This calculates the factorial of <strong>9</strong>.
Notice that <code>: this</code> refers to the sum while <code>: that</code> refers to the current element.
</p>


<p>
Also notice that <strong>@</strong> is the equivalent of <em>new</em> as used in object-oriented programming languages.
</p>

<hr>
<h3 id="Tutorial">6 Tutorial</h3>
<h6 ><a href="src/core/documentation/tutorial.py">src/core/documentation/tutorial.py</a></h6>

<p>
<em>This chapter gives an in-depth explanation of the different aspects of the Nomenine programming language.</em>
</p>

<hr>
<h3 id="Reference">7 Reference</h3>
<h6 ><a href="src/core/documentation/root.py">src/core/documentation/root.py</a></h6>

<h4 id="If_statements">7.1 If statements</h4>
<h6 ><a href="src/core/runtime/control_structure/if.py">src/core/runtime/control_structure/if.py</a></h6>

<p>
There are two main forms of if-statements in Nomenine.
</p>


<p>
1. Regular if-then with optional else-clause
</p>


<p>
if [ condition ] then [ value ]
</p>


<p>
if [ condition ] then [ value ] else [ alternative-value ]
</p>


<p>
2. The if-let statement where the result of the condition can be uses in the then-clause
</p>


<p>
if x [ condition ] then [ do something with x ] else [ fallback ]
</p>


<p>
Notice that Nomenine does not use booleans.
Instead, the then-clause is evaluated if the condition-clause does not fail,
and if it does fail, the optional else-clause is evaluated.
For example, this means that if-statements can be use similarly to try-clauses.
</p>

</body>
</html>

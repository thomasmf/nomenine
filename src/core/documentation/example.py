

DOC_CHAPTER(
  header = 'Example',
  text = """

This is what it looks like:

$DOC_CODE(

let sort ( function ( List ) [

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

]
)
  """
)


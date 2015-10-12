

DOC_ROOT_NODE(
  header = 'Nomenine',

  text = """
$DOC_PURPOSE(
My name is Thomas Mork Farrelly.
Over the years I have spent a lot of time factoring code.
Nomenine is a result of this.
)

$DOC_PURPOSE(
Nomenine may, in its current state,
be of limited interest as a practical language,
but hopefully some of it will be of some interest to some people.
)

$DOC_PURPOSE(
I'm releasing this only for backup purpose. Please come back later! 
)
  """,

  nodes = [

    DOC_EMBED( 'About' ),

    DOC_EMBED( 'Example' ),

    DOC_CONTENT(),

    DOC_EMBED( 'Features' ),

    DOC_EMBED( 'Overview' ),

    DOC_EMBED( 'Tutorial' ),

    DOC_CHAPTER( 'Reference' ),

  ]
)


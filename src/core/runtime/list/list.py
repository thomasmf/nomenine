

def LISTNEW( *elements ) :
  if list( elements ) == [] :
    return PRE( '$CA(nom_array_mutable_nolock_new())' )
  else :
    return PRE( '$CA(nom_list_new( ' + ', '.join( elements ) + ', NULL ))' )


ROOT_SCOPE_METHOD(
  MD( 'List', 'LIST_FACTORY_single()' ),
  MD( 'empty', '$LISTNEW()' ),
  MO( """
    function list ( :: elements ( Star @ ( Any ) ) ) [ : that elements ]
  """ )
)


TEST( """ . ( list 2 ( . 2 * 100 ) 4 ) next value == 200 """ )
TEST( """ . ( list ) sort joinToString "/" == "" """ )
TEST( """ . ( list 1 ) sort joinToString "/" == "1" """ )
TEST( """ . ( list 4 5 3 2 ) sort joinToString "/" == "2/3/4/5" """ )


FUNCTION( 'ANY nom_list_new( void* first, ... )', """
  ARRAY_MUTABLE_NOLOCK array = nom_array_mutable_nolock_new() ;

  ANY current = first ;
  va_list ap;

  va_start( ap, first ) ;
  while ( current ) {
    nom_array_mutable_nolock_push( array, current ) ;
    current = va_arg( ap, ANY ) ;
  }
  va_end( ap ) ;

  return $CA(array) ;
""" )


CLASS( 'LIST',
  inherit = [ 'TOKEN' ],
  methods = [
    MS( ARG( CW( 'evaluate' ), CG( 'ANY', 'scope' ) ), """
      nom_phrase_evaluate( CONTEXT, $CA(ACTION), PARAM_scope ) ;
    """ ),
    MS( ARG( CW( 'flatten' ), CG( 'ANY', 'scope' ) ), """
      nom_phrase_flatten( CONTEXT, $CA(ACTION), PARAM_scope ) ;
    """ ),
    MS( ARG( CW( 'reduce' ), CG( 'ANY', 'sum' ), CG( 'ANY', 'action' ) ), """
      nom_list_reduce( CONTEXT, $CA(ACTION), PARAM_action, PARAM_sum ) ;
    """ ),

    MTID_IS( 'STRING' ),
    MTID( 'STRING_EXTRACT_TYPE_single', """
      nom_this_list_produce_string( CONTEXT ) ;
    """ ),

    MO( """
      function sort [
        if pivot [ : this value ] then [
          Merger @
            ( Mill @ ( : this next ) ( Predicate @ () [ : that =< ( pivot ) ] ) sort )
            ( Element @ ( pivot )
              ( Mill @ ( : this next ) ( Predicate @ () [ : that > ( pivot ) ] ) sort )
            )
        ] else [ empty ]
      ]
    """ ),
    MO( """
      function joinToString ( :: separator ( StringExtract ) ) [
        let separator ( : that separator ) [
          if s [ : this value produce ( StringExtract ) ] then [
            if [ : this next value ] then [
              s + ( : that separator ) + ( : this next joinToString ( : that separator ) )
            ] else [
              s
            ]
          ] else [
            . ""
          ]

        ]
      ]
    """ ),
  ]
)




def LISTNEW( *elements ) :
  if list( elements ) == [] :
    return PRE( '$CA(nom_array_mutable_nolock_new())' )
  else :
    return PRE( '$CA(nom_list_new( ' + ', '.join( elements ) + ', NULL ))' )


ROOT_SCOPE_METHOD(
  MD( 'List', 'LIST_FACTORY_single()' ),
  MD( 'empty', '$LISTNEW()' ),
  MS( ARG( CW( 'list' ), CC( 'STAR_new( ANY_FACTORY_single() )', 'elements' ) ), """
    $NOM( CONTEXT, PARAM_elements,
      : that
    ) ;
  """ )
)


TEST( """ . ( list 2 ( . 2 * 100 ) 4 ) next value == 200 """ )
TEST( """ . ( list ) sort join "/" == "" """ )
TEST( """ . ( list 1 ) sort join "/" == "1" """ )
TEST( """ . ( list 4 5 3 2 ) sort join "/" == "2/3/4/5" """ )
TEST( """ . [] serialize == "[]" """ )
TEST( """ . [ a [ 1 ] ( . 2 ) ] serialize == "[ a [ 1 ] ( . 2 ) ]" """ )


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
      $NOM( CONTEXT, $NONE,
        if [ : this value ] then [. "[ " + ( Map @ ( : this ) ( Closure @ () [ : that serialize ] ) join " " ) + " ]" ] else [ . "[]" ]
      ) ;
    """ ),

    MC( ARG( CW( 'serialize' ) ), """
      $NOM( CONTEXT, $NONE,
        if [ : this value ] then [. "[ " + ( Map @ ( : this ) ( Closure @ () [ : that serialize ] ) join " " ) + " ]" ] else [ . "[]" ]
      ) ;
    """ ),


    MC( ARG( CW( 'join' ), CT( 'STRING', 'separator' ) ), """
      nom_this_list_join( CONTEXT, PARAM_separator ) ;
    """ ),

    MC( ARG( CW( 'sort' ) ), """
      $NOM( CONTEXT, $NONE,
        if pivot [ : this value ] then [
          Merger @
            ( Mill @ ( : this next ) ( Predicate @ () [ : that =< ( pivot ) ] ) sort )
            ( Element @ ( pivot )
              ( Mill @ ( : this next ) ( Predicate @ () [ : that > ( pivot ) ] ) sort )
            )
        ] else [ empty ]
      ) ;
    """ ),

  ]
)


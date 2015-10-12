

FUNCTION( 'ARRAY_MUTABLE_NOLOCK nom_array_mutable_nolock_new()', """
  return ARRAY_MUTABLE_NOLOCK_new( NULL, 0, 8 ) ;
""" )

FUNCTION( 'void nom_array_mutable_nolock_push( ARRAY_MUTABLE_NOLOCK array, ANY value )', """
  n_integer index = array->size ;
  array->size ++ ;
  nom_array_mutable_nolock_reallocate( array ) ;
  array->data[ index ] = value ;
""" )

FUNCTION( 'void nom_array_mutable_nolock_reallocate( ARRAY_MUTABLE_NOLOCK array )', """
  if ( array->data == NULL ) {
    array->data = $CAST(ANY*,nom_malloc( array->capacity * sizeof(ANY) )) ;
  }
  if ( array->size > array->capacity ) {
    array->capacity *= 2 ;
    array->data = $CAST(ANY*,nom_realloc( array->data, array->capacity * sizeof(ANY) )) ;
  }
""" )

FUNCTION( 'ANY nom_array_mutable_nolock_get( ARRAY_MUTABLE_NOLOCK array, n_integer index )', """
  return array->data[ index ] ;
""" )

FUNCTION( 'ANY nom_array_mutable_nolock_value( ARRAY_MUTABLE_NOLOCK array )', """
  $ERROR( "Attempt to get value of empty list", array->size != 0 ) ;
  return array->data[ 0 ] ;
""" )

FUNCTION( 'n_integer nom_array_mutable_nolock_size( ARRAY_MUTABLE_NOLOCK array )', """
  return array->size ;
""" )

def ARRAY_MUTABLE_NOLOCK__NONEMPTY( context, array ) :
  return PRE( """
    if ( """ + array + """->size == 0 ) {
      ANY _context_ = """ + context + """ ;
      nom_fail( _context_, "Empty array has no more elements", $NONE ) ;
      return ;
    }
  """ )

FUNCTION( 'ARRAY_MUTABLE_NOLOCK nom_array_mutable_nolock_next( ARRAY_MUTABLE_NOLOCK array )', """
  if ( array->size == 0 ) {
    return array ;
  } else {
    return ARRAY_MUTABLE_NOLOCK_new( array->data + 1, array->size - 1, 0 ) ;
  }
""" )

FUNCTION( 'n_string nom_array_mutable_nolock_dump( ARRAY_MUTABLE_NOLOCK array )', """
  n_string s = "" ;

  for ( n_integer i = 0 ; i < array->size ; i ++ ) {
    s = nom_format_string( "%s %s", s, $DUMP( array->data[ i ] ) ) ;
  }

  return s ;
""" )


OBJECT( 'ARRAY_MUTABLE_NOLOCK',
  inherit = [ 'LIST' ],
  attributes = [
    A( 'ANY*', 'data' ),
    A( 'n_integer', 'size' ),
    A( 'n_integer', 'capacity' ),
  ],
  methods = [
    MS( ARG( CW( 'next' ) ), """
      JUMP__return_ANY( CONTEXT, CONTEXT, $CA(nom_array_mutable_nolock_next( ACTION )) ) ;
    """ ),
    MS( ARG( CW( 'value' ) ), """
      $ARRAY_MUTABLE_NOLOCK__NONEMPTY( CONTEXT, ACTION ) ;
      JUMP__return_ANY( CONTEXT, CONTEXT, nom_array_mutable_nolock_value( ACTION ) ) ;
    """ ),

  ],
  dump = D( '%s', 'nom_array_mutable_nolock_dump( object )' )
)


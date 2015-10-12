

ROOT_SCOPE_METHOD( MD( 'Reference', 'REFERENCE_FACTORY_single()' ) )


FUNCTION( 'void nom_reference_lock( REFERENCE reference )', """
  nom_mutex_lock( reference->mutex ) ;
""" )

FUNCTION( 'void nom_reference_unlock( REFERENCE reference )', """
  nom_mutex_unlock( reference->mutex ) ;
""" )

FUNCTION( 'REFERENCE nom_reference_new( ANY value )', """
  return REFERENCE_new( value, nom_mutex_new() ) ;
""" )

FUNCTION( 'REFERENCE nom_reference_locked_new()', """
  REFERENCE reference = nom_reference_new( $NONE ) ;
  nom_reference_lock( reference ) ;
  return reference ;
""" )

FUNCTION( 'void nom_reference_set_and_unlock( REFERENCE reference, ANY value )', """
  nom_reference_set_nolock( reference, value ) ;
  nom_reference_unlock( reference ) ;
""" )

FUNCTION( 'void nom_reference_set_nolock( REFERENCE reference, ANY value )', """
  reference->value = value ;
  return ;
""" )

FUNCTION( 'void nom_reference_set( REFERENCE reference, ANY value )', """
  nom_reference_lock( reference ) ;
  nom_reference_set_nolock( reference, value ) ;
  nom_reference_unlock( reference ) ;
  return ;
""" )

FUNCTION( 'ANY nom_reference_get_nolock( REFERENCE reference )', """
  return reference->value ;
""" )

FUNCTION( 'ANY nom_reference_get( REFERENCE reference )', """
  nom_reference_lock( reference ) ;
  ANY value = nom_reference_get_nolock( reference ) ;
  nom_reference_unlock( reference ) ;
  return value ;
""" )



OBJECT( 'REFERENCE_FACTORY',
  methods = [
    MS( ARG( CW( '@' ) ), """
      $OUT( new reference ) ;
      JUMP__return_ANY( CONTEXT, CONTEXT, $CA(nom_reference_new( $NONE )) ) ;
    """ ),
  ]
)

OBJECT( 'REFERENCE',
  inherit = [ 'BOX', 'MUTEXED' ],
  methods = [
    MC( ARG( CW( 'set' ), CG( 'ANY', 'value' ) ), """
      nom_reference_set( ACTION, PARAM_value ) ;
      JUMP__this( CONTEXT, CONTEXT ) ;
    """ ),
    MS( ARG( CW( 'get' ) ), """
      JUMP__return_ANY( CONTEXT, CONTEXT, nom_reference_get( ACTION ) ) ;
    """ ),
  ],
  dump = D( '%s', '$DUMP( object->value )' )
)


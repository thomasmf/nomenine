

FUNCTION( 'FLAG nom_flag_new( n_boolean value )', """
  return FLAG_new( nom_mutex_new(), value ) ;
""" )


FUNCTION( 'void nom_flag_lock( FLAG flag )', """
  nom_mutex_lock( flag->mutex ) ;
""" )

FUNCTION( 'void nom_flag_unlock( FLAG flag )', """
  nom_mutex_unlock( flag->mutex ) ;
""" )

FUNCTION( 'n_boolean nom_flag_get_nolock( FLAG flag )', """
  return flag->value ;
""" )


FUNCTION( 'n_boolean nom_flag_get( FLAG flag )', """
  nom_flag_lock( flag ) ;
  n_boolean value = nom_flag_get_nolock( flag ) ;
  nom_flag_unlock( flag ) ;
  return value ;
""" )


FUNCTION( 'void nom_flag_set_nolock( FLAG flag, n_boolean value )', """
  flag->value = value ;
""" )

FUNCTION( 'void nom_flag_set( FLAG flag, n_boolean value )', """
  nom_flag_lock( flag ) ;
  nom_flag_set_nolock( flag, value ) ;
  nom_flag_unlock( flag ) ;
""" )


OBJECT( 'FLAG',
  inherit = [ 'MUTEXED' ],
  attributes = [
    A( 'n_boolean', 'value' ),
  ]
)


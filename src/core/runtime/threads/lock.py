

FUNCTION( 'LOCK nom_lock_new()', """
  return LOCK_new( nom_mutex_new(), nom_cond_new(), $FALSE ) ;
""" )

FUNCTION( 'void nom_lock_lock( LOCK lock )', """
  nom_mutex_lock( lock->mutex ) ;
  while ( lock->locked ) {
    nom_cond_wait( lock->cond, lock->mutex ) ;
  }
  lock->locked = $TRUE ;
  nom_mutex_unlock( lock->mutex ) ;
""" )

FUNCTION( 'void nom_lock_unlock( LOCK lock )', """
  nom_mutex_lock( lock->mutex ) ;
  lock->locked = $FALSE ;
  nom_cond_broadcast( lock->cond ) ;
  nom_mutex_unlock( lock->mutex ) ;
""" )


OBJECT( 'LOCK',
  inherit = [ 'MUTEXED' ],
  attributes = [
    A( 'COND', 'cond' ),
    A( 'n_integer', 'locked' ),
  ]
)

OBJECT( 'LOCKABLE',
  attributes = [
    A( 'LOCK', 'lock' ),
  ]
)



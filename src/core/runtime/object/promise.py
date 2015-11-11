

ROOT_SCOPE_METHOD( MD( 'Promise', 'PROMISE_FACTORY_single()' ) )


PROMISE_STATE_INITIAL = 0
PROMISE_STATE_PENDING = 1
PROMISE_STATE_FINE = 2
PROMISE_STATE_FAIL = 3


def PROMISE_START( promise, code ) :
  return PRE( """do {
      nom_promise_lock( """ + promise + """ ) ;
      if ( """ + promise + """->state == $PROMISE_STATE_INITIAL ) {
        """ + promise + """->state = $PROMISE_STATE_PENDING ;
        nom_promise_unlock( """ + promise + """ ) ;
        """ + code + """
      } else {
        nom_promise_unlock( """ + promise + """ ) ;
      }
  } while ( $FALSE ) ;""" )


def PROMISE_USE( promise, fine_code, fail_code ) :
  return PRE( """
    nom_promise_wait( """ + promise + """ ) ;
    """ + PROMISE_TEST( promise, fine_code, fail_code ) + """
  """ )


def PROMISE_TEST( promise, fine_code, fail_code ) :
  return PRE( """
    if ( nom_promise_get_state( """ + promise + """ ) == $PROMISE_STATE_FINE ) {
      """ + fine_code + """
    } else {
      """ + fail_code + """
    }
  """ )



FUNCTION( 'void nom_promise_lock( PROMISE promise )', """
  nom_mutex_lock( promise->mutex ) ;
""" )

FUNCTION( 'void nom_promise_unlock( PROMISE promise )', """
  nom_mutex_unlock( promise->mutex ) ;
""" )

FUNCTION( 'PROMISE nom_promise_new()', """
  return PROMISE_new( $NONE, nom_mutex_new(), nom_cond_new(), $PROMISE_STATE_INITIAL ) ;
""" )


FUNCTION( 'void nom_promise_wait( PROMISE promise )', """
  nom_promise_lock( promise ) ;
  while ( promise->state <= $PROMISE_STATE_PENDING ) {
    nom_cond_wait( promise->cond, promise->mutex ) ;
  }
  nom_promise_unlock( promise ) ;
""" )


FUNCTION( 'ANY nom_promise_get( PROMISE promise )', """
  return promise->value ;
""" )

FUNCTION( 'n_integer nom_promise_get_state( PROMISE promise )', """
  nom_promise_lock( promise ) ;
  n_integer state = promise->state ;
  nom_promise_unlock( promise ) ;
  return state ;
""" )


FUNCTION( 'void nom_promise_set_fine( PROMISE promise, ANY value )', """
  nom_promise_lock( promise ) ;
  promise->value = value ;
  promise->state = $PROMISE_STATE_FINE ;
  nom_cond_broadcast( promise->cond ) ;
  nom_promise_unlock( promise ) ;
""" )

FUNCTION( 'void nom_promise_set_fail( PROMISE promise, ANY value )', """
  nom_promise_lock( promise ) ;
  promise->value = value ;
  promise->state = $PROMISE_STATE_FAIL ;
  nom_cond_broadcast( promise->cond ) ;
  nom_promise_unlock( promise ) ;
""" )


FUNCTION( 'void nom_promise_apply( ANY context, PROMISE promise, ANY that )', """
  $PROMISE_USE( promise,
    nom_do_sync( FRAME__TASK_new( context, promise->value, that ) ) ;
  ,
    JUMP__fail_ANY( context, context, promise->value ) ;
  )
""" )


FUNCTION( 'void nom_promise_return( ANY context, PROMISE promise )', """
  $PROMISE_USE( promise,
    JUMP__return_ANY( context, context, promise->value ) ;
  ,
    JUMP__fail_ANY( context, context, promise->value ) ;
  )
""" )


OBJECT( 'PROMISE_FACTORY',
  methods = [
    MS( ARG( CW( '@' ) ), """
      JUMP__return_ANY( CONTEXT, CONTEXT, $CA(PROMISE_BOX_new( $CA(nom_promise_new()) )) ) ;
    """ ),
  ]
)


OBJECT( 'PROMISE_BOX',
  inherit = [ 'BOX' ],
  methods = [
    MS( ARG( CW( 'fail' ), CG( 'ANY', 'error' ) ), """
      nom_promise_set_fail( $C(PROMISE,ACTION->value), PARAM_error ) ;
    """ ),
    MS( ARG( CW( 'set' ), CG( 'ANY', 'value' ) ), """
      nom_promise_set_fine( $C(PROMISE,ACTION->value), PARAM_value ) ;
    """ ),
  ]
)


OBJECTIVE( 'PROMISE',
  inherit = [ 'VALUE', 'MUTEXED' ],
  attributes = [
    A( 'COND', 'cond' ),
    A( 'n_integer', 'state' ),
  ],
  objective =  """
    nom_promise_apply( CONTEXT, ACTION, THAT ) ;
  """
)



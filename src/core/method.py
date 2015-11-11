

REGISTER_FLAG( 'no_simple_methods', 'disable simplification of many method contexts' )
REGISTER_FLAG( 'list_used_methods', 'sorted can be used to guide optimization' )


class METHOD( object ) :
  buoyancy = 0

  def __init__( self, pattern, action = '' ) :
    self.pattern = pattern
    self.action = action

  def has_signature( self, pattern ) :
    return False

  def attach( self, this ) :
    pass

  def build_primitive_dispatch( self ) :
    return 'nom_array_mutable_nolock_push( reification, $CA(' + self.build_reification_component() + ') ) ;'



class M( METHOD ) :
  buoyancy = 100

  action_objective_counter = 0

  def __init__( self, pattern, action = '', use_application_frame = True ) :
    self.use_application_frame = use_application_frame
    super( M, self ).__init__( pattern, action )

  def __eq__( self, other ) :
    if ( not isinstance( other, M ) ) :
      return False
    return self.has_signature( other.pattern )


  def build_partial_primitive_dispatch( self ) :
    if isinstance( self.pattern[ 0 ], CW ) :
      return """
        $OPT(
          if ( strcmp( word->data, \"""" + self.pattern[ 0 ].s + """\" ) != 0 ) break ;
          break ;
        )
      """
    else :
      return ''


  def has_signature( self, pattern ) :
    return self.pattern == pattern

  def create_method_action_function( self ) :
    return FUNCTION( 'void ' + self.this.name + '__' + self.pattern.build_function_name() + '( ' +  self.build_function_formal_parameters() + ' )',
      ENABLED( 'list_used_methods', 'printf( "' + self.this.name + '__' + self.pattern.build_function_name() + '\\n" ) ; \n' ) + self.action.strip()
    )

  def get_action_objective_count( self ) :
    M.action_objective_counter += 1
    return str( M.action_objective_counter )

  def attach( self, this ) :
    self.this = this
    self.oname = self.this.name + '_ACTION_' + self.get_action_objective_count()
    OBJECTIVE( self.oname,
      attributes = [
        A( self.this.name, 'this' ),
      ],
      objective = self.build_action_objective()
    )
    CORE.register_method( self )

  def build_function_invocation( self, context, action ) :
    return self.this.name + '__' + self.pattern.build_function_name() + '( ' + ', '.join( [ context, action ] + self.pattern.build_function_actual_parameter_elements() ) + ' ) ;'

  def build_action_objective( self ) :
    return '\n'.join( [
      'ARRAY_MUTABLE_NOLOCK message = $C(ARRAY_MUTABLE_NOLOCK,THAT) ; (void)message ;',
      self.pattern.build_parameter_declare(),
      self.build_function_invocation( 'CONTEXT', 'ACTION->this' ),
    ] )

  def build_function_formal_parameters( self ) :
    return self.pattern.build_formal_parameters( self.this.name )

  def create_jump_function_wrapper( self ) :
    use_application_frame = arg_get_flag( 'no_simple_methods' ) or self.use_application_frame
    return FUNCTION( 'void ' + self.this.name + '__' + self.pattern.build_function_name() + '__jump_wrapper( ' +  self.pattern.build_formal_parameters() + ' )',
      self.build_function_invocation( ( '$CA(FRAME__APPLICATION_new( CONTEXT, ACTION ))' if use_application_frame else 'CONTEXT' ), '$C(' + self.this.name + ',ACTION)' )
    )

  def build_reification_component( self ) :
    return ' '.join( [
      'FUNCTION_new( $LAZY( ANY, ' + self.pattern.build_type_objects() + ' ), $CA(' + self.oname + '_new( ACTION )) )'
    ] )

  def build_primitive_dispatch( self ) :
    return """
      do {
        n_boolean append_component = $TRUE ;
        do {
          """ + self.pattern.build_primitive_dispatch() + """
        } while ( $FALSE ) ;
        if ( append_component ) {
          nom_array_mutable_nolock_push( reification, $CA(""" + self.build_reification_component() + """) ) ;
        } else {
        }
      } while ( $FALSE ) ;
    """


class MS( M ) :
  buoyancy = 103
  def __init__( self, pattern, action = '' ) :
    super( MS, self ).__init__( pattern, action, use_application_frame = False )


class MC( M ) :
  buoyancy = 107
  def __init__( self, pattern, action = '' ) :
    super( MC, self ).__init__( pattern, action, use_application_frame = True )

class MD( M ) :
  buoyancy = 101

  def __init__( self, w, e ) :
    super( MD, self ).__init__( ARG( CW( w ) ), """
        JUMP__return_ANY( CONTEXT, CONTEXT, $LAZY( ANY, $CA(""" + e + """) ) ) ;
    """ )


class MTID( M ) :
  buoyancy = 50

  def __init__( self, v, action ) :
    super( MTID, self ).__init__( ARG( CW( 'produce' ), CTID( v ) ), action )


class MTID_EXTRACT ( MTID ) :
  buoyancy = 10

  def __init__( self, nv ) :
    super( MTID_EXTRACT, self ).__init__(
      nv + '_EXTRACT_TYPE_single',
      """
        JUMP__return_ANY( CONTEXT, CONTEXT, $CA(ACTION) ) ;
      """
    )


class MTID_IS ( MTID ) :
  buoyancy = 20

  def __init__( self, nv ) :
    super( MTID_IS, self ).__init__(
      nv + '_FACTORY_single',
      """
        JUMP__this( CONTEXT, CONTEXT ) ;
      """
    )


class MF( METHOD ) :
  buoyancy = 1000000

  def __init__( self ) :
    super( MF, self ).__init__( ARGA(), '' )

  def build_reification_component( self ) :
    return ' '.join( [
      'ACTION->parent'
    ] )



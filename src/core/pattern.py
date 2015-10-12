

class ARGA ( object ) :
  def __init__( self ) :
    pass

  def __len__( self ) :
    return 0

  def build_primitive_dispatch( self ) :
    return ''



class ARG( ARGA ) :
  def __init__( self, *pattern ) :
    self.pattern = pattern
    CORE.register_pattern( self )
  def __repr__( self ) :
    return 'ARG[ ' + ', '.join( [ str( x ) for x in self.pattern ] ) + ' ]'
  def __len__( self ) :
    return len( self.pattern )

  def __getitem__( self, key ) :
    return self.pattern[ key ]

  def __eq__( self, other ) :
    if ( len( self ) != len( other ) ) :
      return False
    for i in range( len( self ) ) :
      if ( not ( self[ i ] == other[ i ] ) ) :
        return False
    return True


  def build_actual_parameters( self, ACTION = 'ACTION' ) :
    return ', '.join( [ 'CONTEXT', ACTION ] + self.build_function_actual_parameter_elements() )

  def build_formal_parameters( self, type = 'ANY' ) :
    return ', '.join( [ 'ANY CONTEXT', type + ' ACTION' ] + self.build_function_formal_parameter_elements() )

  def build_function_name( self ) :
    return '_'.join( self.build_function_name_component_elements() )

  def build_jump_function_signature( self, suffix = '' ) :
    return 'void JUMP__' + self.build_function_name() + suffix + '( ' + ', '.join( [ 'ANY CONTEXT', 'ANY ACTION' ] + self.build_function_formal_parameter_elements() ) + ' )'

  def build_parameter_declare( self ) :
    return '\n'.join( [
      '\n'.join( [
        '\n'.join( [
          self.pattern[ i ].build_formal_parameter() + ' = ' + self.pattern[ i ].build_cast( 'nom_array_mutable_nolock_get( message, ' + str( i ) + ' )' ) + ' ;',
        ] )
        for i in range( len( self.pattern ) ) if self.pattern[ i ].build_formal_parameter() != ''
      ] ),
    ] )


  def build_type_objects( self ) :
    return  ''.join( [
      '$CA(GROUPING_new( $LISTNEW(',
      ', '.join( [
        p.build_type_object()
        for p in self.pattern
      ]),
      ') ))',
    ] )

  def build_message_objects( self ) :
    return  ''.join( [
      '$LISTNEW( ',
      ', '.join( self.build_message_object_elements() ),
      ' )',
    ] )



  def create_jump_function_forward( self ) :
    return FUNCTION( self.build_jump_function_signature( '__forward' ),
      'JUMP__' + self.build_function_name() + '( ' + self.build_actual_parameters( '$C(FRAME,ACTION)->parent' ) + ' ) ;'
    )

  def create_jump_function_fail( self ) :
    return FUNCTION( self.build_jump_function_signature( '__fail' ),
      'nom_fail( CONTEXT, "Unrecognized message.", $NONE ) ;',
    )

  def create_jump_function_fallback( self ) :
    return FUNCTION( self.build_jump_function_signature( '__fallback' ),
      'nom_send_nonempty_flat_phrase_message( CONTEXT, ACTION, ' + self.build_message_objects() + ' ) ;'
    )

  def create_jump_function( self ) :
    return FUNCTION( self.build_jump_function_signature(),
      '\n'.join( [
        'static void (* const jump_table[])( ' + self.build_formal_parameters()  + ' ) = {',
        ', '.join( [
          p.get_action_function( self )
          for p in CORE.objectives
        ] ),
        '} ;',
        '(* jump_table[ ACTION->pix ])( ' + self.build_actual_parameters() + ' ) ;',
      ] )
    )


  def build_message_object_elements( self ) :
    return filter( None, [ p.build_message_object() for p in self.pattern ] )

  def build_function_name_component_elements( self ) :
    return filter( None, [ p.build_name_component() for p in self.pattern ] )

  def build_function_formal_parameter_elements( self ) :
    return filter( None, [ p.build_formal_parameter() for p in self.pattern ] )

  def build_function_actual_parameter_elements( self ) :
    return filter( None, [ p.build_actual_parameter() for p in self.pattern ] )


  def build_primitive_dispatch( self ) :
    return '\n'.join( [
      '$IFLET( that, ARRAY_MUTABLE_NOLOCK,THAT ) ;',
      '\n'.join( [
        pv.build_primitive_dispatch( pi )
        for pi, pv in enumerate( self.pattern )
      ] )
    ] )



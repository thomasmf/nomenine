

class OBJECTIVE ( object ) :
  current_pix = 0
  def __init__( self, name, attributes = [], objective = '', dump = D(), inherit = [] ) :
    self.name = name
    self.attributes = attributes
    self.objective = objective
    self.dump = dump
    self.inherit = [ e for e in ( [ 'ANY' ] + inherit ) if e != name ]
    self.children = []
    self.updatePix()
    CORE.register_objective( self )

  def updatePix( self ) :
    self.pix = OBJECTIVE.current_pix
    OBJECTIVE.current_pix += 1

  def create_objective_function( self ) :
    return FUNCTION( 'void ' + self.name + '_objective( ANY CONTEXT )', self.build_objective() )

  def create_dump_function( self ) :
    return FUNCTION( 'n_string ' + self.name + '_dump( ANY o )', '\n'.join( [
      self.name + ' object = $CAST(' + self.name + ',o) ;',
      '(void)object ;',
      'return nom_format_string( ' + ', '.join( [ '"[\033[0;34m%04zx:\033[0m%s' + ( ' ' if ( self.dump.pattern != '' ) else '' ) + self.dump.pattern + ']"', '(n_integer)o', '"' + self.name + '"' ] + list( self.dump.values ) ) + ' ) ;',
    ] ) )


  def build_base_allocation( self, n ) :
    return """
      """ + self.name + """ """ + n + """ = $CAST(""" + self.name + """,nom_malloc( sizeof( struct """ + self.name + """_struct ) )) ;
      """ + n + """->objective = """ + self.name + """_objective ;
      """ + n + """->pix = """ + str( self.pix ) + """ ;
      """ + n + """->dump = """ + self.name + """_dump ;
    """

  def create_native_constructor_function( self ) :
    return FUNCTION( self.name + ' ' + self.name + '_new( ' + self.build_native_constructor_signature() + ' )', '\n'.join( [
#      'printf( "' + self.name + '\\n") ;',
      self.build_base_allocation( 'new_object' ),
      '\n'.join( [
        a.build_set( 'new_object', a.name ) + ' ;'
        for a in self.attributes
      ] ),
      'return new_object ;',
    ] ) )

  def build_declare_object_struct( self ) :
    return '\n'.join( [
      'struct ' + self.name + '_struct {',
      '\n'.join( [
        '  ' + a.type + ' ' + a.name + ' ;'
        for a in ( [
          A( 'n_objective', 'objective' ),
          A( 'n_integer', 'pix' ),
          A( 'n_dump', 'dump' ),
        ] + self.attributes )
      ] ),
      '} ;'
    ] )

  def build_native_constructor_signature( self ) :
    if ( self.attributes == [] ) :
      return "void"
    else :
      return ', '.join( [
        a.type + ' ' + a.name
        for a in self.attributes
      ] )

  def get_action_function( self, pattern ) :
    return 'JUMP__' + pattern.build_function_name() + '__fallback'

  def build_objective( self ) :
    return self.build_objective_box( self.objective )

  def build_objective_box( self, objective ) :
    return '\n'.join( [
      'do {',
      '$IFLET( task, FRAME__TASK, CONTEXT ) ;',
      '$IFLET( ACTION, ' + self.name + ', task->action ) ;',
      'ANY THAT = task->that ; (void)THAT ;',
      objective.strip(),
      'return ;',
      '} while ( $FALSE ) ;',
      '$OUT( OBJECTIVE applied on non-task context ) ;',
      'nom_fail( CONTEXT, "Unhandled message.", $NONE ) ;',
      'return ;',
    ] ).strip()


  def isOk( self ) :
    return self.inherit == []

  def fix( self ) :
    if not self.isOk() :
      obj = CORE.get_object( self.inherit[ -1 ] )
      if obj.isOk() :
        self.merge_inherit( obj )
        del self.inherit[ -1 ]
        self.fix()

  def merge_inherit( self, obj ) :
    obj.children.append( self )
    self.attributes = obj.attributes + [ a for a in self.attributes if a not in obj.attributes ]

  def is_substruct_of( self, obj ) :
    for i, a in enumerate( obj.attributes ) :
      if a != self.attributes[ i ] :
        return False
    return True

  def get_all_substructs_of( self, obj ) :
    if self.is_substruct_of( obj ) :
      substructs = [ self ]
      for sub in self.children :
        substructs += sub.get_all_substructs_of( obj )
      return substructs
    else :
      return []


class OBJECT ( OBJECTIVE ) :
  def __init__( self, name, attributes = [], methods = [], dump = D(), inherit = [] ) :
    self.name = name
    self.methods = methods
    super( OBJECT, self ).__init__( name,
      inherit = inherit,
      attributes = attributes,
      dump = dump
    )
    CORE.register_object( self )

  def get_action_function( self, pattern ) :
    method = self.get_method( pattern )
    if ( method ) :
      return method.this.name + '__' + method.pattern.build_function_name() + '__jump_wrapper'
    else :
      return 'JUMP__' + pattern.build_function_name() + '__fail'

  def build_primitive_dispatch( self ) :
    return '\n'.join( [
      m.build_primitive_dispatch()
      for m in sorted( self.methods, key = lambda x : x.buoyancy )
    ] )


  def build_objective( self ) :
    return self.build_objective_box( """
      ARRAY_MUTABLE_NOLOCK reification = nom_array_mutable_nolock_new() ;
      """ + self.build_primitive_dispatch() + """
      nom_do_sync( FRAME__TASK_new( task->parent, $CA(UNION_new( $CA(reification) )), THAT ) ) ;
    """ )


  def fix( self ) :
    if not self.isOk() :
      obj = CORE.get_object( self.inherit[ -1 ] )
      if obj.isOk() :
        self.merge_inherit( obj )
        del self.inherit[ -1 ]
        if self.isOk() :
          self.attach_methods()
        else :
          self.fix()

  def merge_inherit( self, obj ) :
    obj.children.append( self )
    self.attributes = obj.attributes + [ a for a in self.attributes if a not in obj.attributes ]
    self.methods = self.methods + [ copy.deepcopy( m ) for m in obj.methods if m not in self.methods ]

  def attach_methods( self ) :
    for m in self.methods :
      m.attach( self )

  def get_method( self, pattern ) :
    for m in self.methods :
      if ( m.has_signature( pattern ) ) :
        return m
    return False


class FRAME ( OBJECT ) :
  def __init__( self, name, attributes = [], methods = [], dump = D() ) :
    super( FRAME, self ).__init__( 'FRAME__' + name,
      inherit = [ 'FRAME' ],
      attributes = attributes,
      methods = methods + [ MF() ],
      dump = dump
    )

  def get_action_function( self, pattern ) :
    method = self.get_method( pattern )
    if ( method ) :
      return method.this.name + '__' + method.pattern.build_function_name() + '__jump_wrapper'
    else :
      return 'JUMP__' + pattern.build_function_name() + '__forward'


class TYPE ( OBJECT ) :
  def __init__( self, name, methods = [], dump = D(), primitive = None ) :
    self.primitive = primitive
    super( TYPE, self ).__init__( name,
      inherit = [ 'TYPE' ],
      methods = [
        MS( ARG( CW( 'test' ), CG( 'ANY', 'object' ) ), """
          JUMP__produce_TID__""" + name + """_single( CONTEXT, PARAM_object, """ + name + """_single() ) ;
        """ ),
        MS( ARG( CW( 'consume' ), CG( 'LIST', 'phrase' ) ), '\n'.join( [
          self.build_consume_opt(),
          'nom_clause_consume( CONTEXT, $CA(ACTION), PARAM_phrase ) ;',
        ] ) ),
      ] + methods,
      dump = dump
    )

  def build_consume_opt( self ) :
    if self.primitive :
      return """
        $OPT(
          $IFLET( array, ARRAY_MUTABLE_NOLOCK, PARAM_phrase ) ;
          $ARRAY_MUTABLE_NOLOCK__NONEMPTY( CONTEXT, array ) ;
          ANY value = nom_array_mutable_nolock_value( array ) ;
          $IFLET_SUBSTRUCT( object, """ + self.primitive + """, value ) ;
          JUMP__return_ANY( CONTEXT, CONTEXT, PARAM_phrase );
        )
      """
    else :
      return ''



class CLASS ( OBJECT ) :
  def __init__( self, name, attributes = [], methods = [], factory_methods = [], dump = D(), inherit = []  ) :
    super( CLASS, self ).__init__( name,
      inherit = inherit,
      attributes = attributes,
      methods = [
        MTID_IS( name )
      ] + methods,
      dump = dump
    )
    TYPE( name + '_FACTORY', factory_methods, primitive = name )


class PRIMITIVE ( CLASS ) :
  def __init__( self, name, attributes = [], methods = [], factory_methods = [], dump = D(), inherit = []  ) :
    super( PRIMITIVE, self ).__init__( name,
      inherit = inherit,
      attributes = attributes,
      methods = [
        MTID_EXTRACT( name ),
      ] + methods,
      factory_methods = factory_methods,
      dump = dump
    )
    TYPE( name + '_EXTRACT_TYPE', primitive = name )


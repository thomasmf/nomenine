

def APPEND_H( s ) :
  CORE.toph += s + '\n'

def APPEND_C( s ) :
  CORE.topc += s + '\n'

def APPEND_INIT( s ) :
  CORE.init += s + '\n'

def ROOT_SCOPE_METHOD( *methods ) :
  CORE.root_scope_methods += methods



class BUILDER :

  def __init__( self ) :
    self.toph = ''
    self.topc = ''
    self.init = ''
    self.nom = ''
    self.objectives = []
    self.objects = []
    self.methods = []
    self.patterns = []
    self.tests = []
    self.doc_nodes = []
    self.doc_root_node = None
    self.cfuncs = []
    self.root_scope_methods = []

  def write_to_files( self, base_filename ) :
    file_h = base_filename + '.h'
    if arg_parser_args.verbose :
      print 'Writing', file_h, '...',
    open( file_h, 'w' ).write( self.build_h() )
    if arg_parser_args.verbose :
      print 'Ok'

    file_c = base_filename + '.c'
    if arg_parser_args.verbose :
      print 'Writing', file_c, '...',
    open( file_c, 'w' ).write( self.build_c() )
    if arg_parser_args.verbose :
      print 'Ok'

    if arg_parser_args.verbose :
      print 'Output size', sum( [ 0 if ( l.isspace() ) else 1 for l in open( file_h ) ] ) + sum( [ 0 if ( l.isspace() ) else 1 for l in open( file_c ) ] ), 'lines', os.stat( file_h ).st_size + os.stat( file_c ).st_size, 'bytes'

    if self.doc_root_node != None :
      open( 'readme.html', 'w' ).write( self.doc_root_node.build( [], self.doc_nodes ) )
    else :
      print "Warning: DOC_ROOT_NODE object not specified"


  def register_objective( self, o ) :
    self.objectives.append( o )

  def register_object( self, o ) :
    self.objects.append( o )

  def register_method( self, o ) :
    self.methods.append( o )

  def register_pattern( self, o ) :
    for p in self.patterns :
      if ( p == o ) :
        return
    self.patterns.append( o )

  def register_test( self, o ) :
    self.tests.append( o )

  def register_doc_node( self, o ) :
    self.doc_nodes.append( o )

  def register_doc_root_node( self, o ) :
    if self.doc_root_node != None :
      print "Warning: multiple DOC_ROOT_NODE objects"
    else :
      self.doc_root_node = o


  def register_cfunc( self, o ) :
    self.cfuncs.append( o )

  def create_init_function( self ) :
    return FUNCTION( 'void nom_core_init()', self.init )

  def create_pix_to_objective_verify_function( self ) :
    return FUNCTION( 'n_boolean nom_pix_to_objective_verify( ANY object )', '\n'.join( [
      'const static n_objective objective_list[] = { ',
      ', '.join( [ obj.name + '_objective' for obj in self.objectives ] ),
      '} ;',
      'return objective_list[ object->pix ] == object->objective ;',
    ] ) )

  def create_test_function( self ) :
    return FUNCTION( 'void nom_core_test()', '\n'.join( [
      '\n'.join( [
        t.build_test()
        for t in self.tests
      ] ),
      'printf( "\\tFinished testing.\\n" ) ;',
    ] ) )

  def create_test_substruct_function( self, o ) :
    return FUNCTION( 'n_boolean TEST_SUBSTRUCT__' + o.name + '( ANY object )', '\n'.join( [
      'const static n_boolean substruct_list[] = { ',
      ', '.join( self.get_substruct_list( [ obj.name for obj in o.get_all_substructs_of( o ) ] ) ),
      ' } ;',
      'return substruct_list[ object->pix ] ;',
    ] ) )

  def build_declare_cfuncs( self ) :
    return '\n'.join( [ o.build_declare() for o in self.cfuncs ] )

  def build_define_cfuncs( self ) :
    return '\n\n'.join( [ o.build_define() for o in self.cfuncs ] )

  def build_declare_object_types( self ) :
    return '\n'.join( [
      '\n'.join( [
        'struct ' + p.name + '_struct ;',
        'typedef struct ' + p.name + '_struct * ' + p.name + ' ;'
      ] )
      for p in self.objectives
    ] )

  def build_declare_object_structs( self ) :
    return '\n\n'.join( [
      p.build_declare_object_struct()
      for p in self.objectives
    ] )

  def build_h( self ) :
    return '\n\n'.join( [
      '#ifndef _CORE_H_',
      '#define _CORE_H_',
      self.build_declare_object_types(),
      PRE( self.toph ),
      self.build_declare_cfuncs(),
      self.build_declare_object_structs(),
      '#endif /*_CORE_H_*/',
      '\n\n\n',
    ] )

  def build_c( self ):
    return '\n\n'.join( [
      PRE( self.topc ),
      self.build_define_cfuncs(),
      '\n\n\n',
    ] )

  def get_substruct_list( self, substructs ) :
    return [ ( '$TRUE' if ( o.name in substructs ) else '$FALSE' ) for o in self.objectives ]

  def fix_root_object( self ) :
    OBJECT( 'ROOT_SCOPE',
      methods = self.root_scope_methods
    )

  def fix_objects( self ) :
    ok = False
    while not ok :
      i = 0
      ok = True
      for o in self.objectives :
        i += 1
        o.fix()
        ok = ok and o.isOk()

  def fix_singles( self ) :
    for o in [ o for o in self.objectives if o.attributes == [] ] :
      FUNCTION( 'ANY ' + o.name + '_single()', """
        return $LAZY( ANY, $CA(""" + o.name + """_new()) ) ;
      """ )

  def fix_functions_per_objective( self ) :
    for o in self.objectives :
      o.create_objective_function()
      o.create_dump_function()
      o.create_native_constructor_function()
      self.create_test_substruct_function( o )

  def fix_functions_per_method( self ) :
    for o in self.methods :
      o.create_method_action_function()
      o.create_jump_function_wrapper()

  def fix_functions_per_pattern( self ) :
    for o in self.patterns :
      o.create_jump_function()
      o.create_jump_function_fail()
      o.create_jump_function_fallback()
      o.create_jump_function_forward()

  def fix( self ) :
    if arg_parser_args.verbose :
      print 'Building','...',
    self.fix_root_object()
    self.fix_objects()
    self.fix_singles()
    self.fix_functions_per_objective()
    self.fix_functions_per_method()
    self.fix_functions_per_pattern()
    self.create_pix_to_objective_verify_function()
    self.create_test_function()
    self.create_init_function()
    if arg_parser_args.verbose :
      print 'Ok'

  def get_object( self, name ) :
    for o in self.objects :
      if o.name == name :
        return o
    print "Build error: object " + name + " does not exist"
    sys.exit( 1 )

  def attach_methods( self ) :
    for o in self.objects :
      o.attach_methods()


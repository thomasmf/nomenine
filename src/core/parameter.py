

class PARAM ( object ) :
  pass

  def build_primitive_dispatch( self, i ) :
    return ''

class CW ( PARAM ) :
  def __init__( self, s ) :
    self.s = s
  def __eq__( self, other ) :
    if ( not isinstance( other, CW ) ) :
      return False
    return self.s == other.s
  def build_type_object( self ) :
    return 'WORD_new( "' + self.s + '" )'
  def build_name_component( self ) :
    return replace_all( { '\'': 'QUOTE', '.': 'POINT', '?': 'QUEST', '+': 'PLUS', '-': 'MIN', '*': 'MUL', '/': 'DIV', ':': 'COL', '@': 'AT', '=': 'EQ', '!': 'EXCLAIM', '<': 'EATRIGHT', '>': 'EATLEFT',} ,self.s )
  def build_formal_parameter( self ) :
    return ''
  def build_actual_parameter( self ) :
    return ''
  def build_message_object( self ) :
    return 'WORD_new( "' + self.s + '" )'
  def build_cast( self, s ) :
    return ''
  def build_primitive_dispatch( self, i ) :
    return """
      if ( !( that->size > """ + str( i ) + """ ) ) {
        append_component = $FALSE ;
        break ;
      }
      $IFLET( word_""" + str( i ) + """, WORD, nom_array_mutable_nolock_get( that, """ + str( i ) + """ ) ) ;
      if ( strcmp( word_""" + str( i ) + """->data, \"""" + self.s + """\" ) != 0 ) {
        append_component = $FALSE ;
        break ;
      }
    """

class CT ( PARAM ) :
  def __init__( self, t, n ) :
    self.n = n
    self.t = t
  def __eq__( self, other ) :
    if ( not isinstance( other, CT ) ) :
      return False
    return self.t == other.t
  def build_type_object( self ) :
    return self.t + '_EXTRACT_TYPE_single()'
  def build_name_component( self ) :
    return self.t
  def build_formal_parameter( self ) :
    return self.t + ' PARAM_' + self.n
  def build_actual_parameter( self ) :
    return 'PARAM_' + self.n
  def build_message_object( self ) :
    return self.build_actual_parameter()
  def build_cast( self, s ) :
    return '$C(' + self.t + ',' + s + ')'

class CG ( CT ) :
  def __init__( self, t, n ) :
    self.n = n
    self.t = t
  def __eq__( self, other ) :
    if ( not isinstance( other, CG ) ) :
      return False
    return self.t == other.t
  def build_type_object( self ) :
    return self.t + '_FACTORY_single()'
  def build_name_component( self ) :
    return self.t
  def build_formal_parameter( self ) :
    return 'ANY PARAM_' + self.n
  def build_cast( self, s ) :
    return '$CA(' + s + ')'

class CTID ( CG ) :
  def __init__( self, nv ) :
    super( CTID, self ).__init__( 'ANY', 'tid' )
    self.nv = nv
  def __eq__( self, other ) :
    if ( not isinstance( other, CTID ) ) :
      return False
    return self.nv == other.nv
  def build_name_component( self ) :
    return 'TID__' + self.nv
  def build_type_object( self ) :
    return 'TID_new( $CA(' + self.nv + '()) )'


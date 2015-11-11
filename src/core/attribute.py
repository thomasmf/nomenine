

class ATTRIBUTE ( object) :
  pass

  def build_set( self, o, v ) :
    return o + '->' + self.name + ' = ' + v

  def __eq__( self, other ) :
    return ( self.type == other.type ) and ( self.name == other.name )

class A ( ATTRIBUTE ) :
  def __init__( self, type, name ) :
    self.type = type
    self.name = name



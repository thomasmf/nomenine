

class FUNCTION( object ) :
  def __init__( self, signature, body ) :
    self.signature = signature
    self.body = body
    CORE.register_cfunc( self )
  def build_declare( self ) :
    return self.signature + ' ;'
  def build_define( self ) :
    return '\n'.join( [
      self.signature + '{',
      PRE( self.body ),
      '}'
    ] )


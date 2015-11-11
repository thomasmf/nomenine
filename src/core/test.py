

class TEST :

  tests = []

  def __init__( self, expression ) :
    self.expression = re.sub( '\s+', ' ', expression ).strip().replace( '"', '\\"' )
    CORE.register_test( self )

  def build_test( self ) :
    return '\n'.join( [
      'do {',
      'n_string expression = "' + self.expression + '" ;',
      'JUMP__evaluate_ANY( $CA(FRAME__CORE_UNIT_TEST_new( $CA(CORE_UNIT_TEST_DEADEND_new( expression )), expression )), $CA(STRING_new( expression )), ROOT_SCOPE_single() ) ;',
      '} while ( $FALSE ) ;'
    ] )



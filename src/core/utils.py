

def replace_all( d, s ) :
  for v in d :
    s = s.replace( v, d[ v ] )
  return s


def build_c_string( s ) :
  return '"' + re.sub( '\s+', ' ', s ).replace( '"', '\\"' ).replace( '$', '_' ) + '"'



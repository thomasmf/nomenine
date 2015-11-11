

def DOC_PARAGRAPH( s ) :
  return '<p>' + s.strip() + '</p>'

def DOC_QUOTE( s ) :
  return '<em>' + s.strip() + '</em>'

def DOC_HEADER_SIZED( n, s, id = '' ) :
  return '<h' + str( n ) + ' ' + ( '' if id == '' else 'id="' + id +'"' ) + '>' + s + '</h' + str( n ) + '>'

def DOC_HEADER( s ) :
  return DOC_HEADER_SIZED( 6, s )

def DOC_CODE( s ) :
  return '\n<pre><code>' + s.strip() + '</code></pre>\n'

def DOC_PHRASE( s ) :
  return '<code>' + s.strip() + '</code>'

def DOC_STRONG( s ) :
  return '<strong>' + s.strip() + '</strong>'

def DOC_WORD( s ) :
  return '<strong>' + s.strip() + '</strong>'

def DOC_TYPE( s ) :
  return '<strong>' + s.strip() + '</strong>'

def DOC_PURPOSE( *s ) :
  return '<em>' + PRE( ', '.join( s ).strip() ) + '</em>'

def DOC_LIST_ORDERED( *items ) :
  return '<ol>' + ''.join( [ '<li>' + PRE( e ) + '</li>' for e in items ] ) + '</ol>'

def DOC_LIST_UNORDERED( *items ) :
  return '<ul>' + ''.join( [ '<li>' + PRE( e ) + '</li>' for e in items ] ) + '</ul>'

def DOC_LIST_ITEMS( *items ) :
  return '<dl>' + ''.join( [ PRE( e ) for e in items ] ) + '</dl>'

def DOC_ITEM( n, *s ) :
  return PRE( '<dt>' + n + '</dt>' + '<dd>' + ', '.join( s ).strip() + '</dd>' )

def DOC_RELATED( *headers ) :
  return DOC_STRONG( 'Related:' ) + ' ' + ', '.join( [ DOC_LINK_NODE( h ) for h in headers ] )

def DOC_LINK( text, url ) :
  return '<a href="' + url + '">' + text + '</a>'

def DOC_LINK_NODE( header ) :
  return DOC_LINK( header, '#' + doc_create_anchor_id( header ) )

def DOC_LINK_SOURCE( path ) :
  return DOC_LINK( path, path )

def doc_create_anchor_id( s ) :
    return re.sub( '[^a-zA-Z]', '_', s )

class DOC_NODE ( object ) :
  def __init__( self, header, topic = '' ) :
    self.header = header
    self.topic = topic
    self.source_filename = current_source_filename
    CORE.register_doc_node( self )
  def build_path( self, path ) :
    return '\n'.join( [
      self.build_path( path ),
      DOC_HEADER( DOC_LINK_SOURCE( self.source_filename ) ),
    ] )
  def get_header_size( self, i ) :
    return max( min( i + 1, 5 ), 1 )
  def build_path( self, path ) :
    return '\n'.join( [
      DOC_HEADER_SIZED( self.get_header_size( len( path ) + 1  ), '.'.join( [ str( n ) for n in path ] ) + ' ' + self.header, id = doc_create_anchor_id( self.header ) ),
      DOC_HEADER( DOC_LINK_SOURCE( self.source_filename ) ),
    ] )
  def build_path_content( self, path ) :
    return DOC_HEADER_SIZED( self.get_header_size( len( path ) + 2 ), '.'.join( [ str( n ) for n in path ] ) + ' ' + DOC_LINK_NODE( self.header ) )


class DOC_CHAPTER ( DOC_NODE ) :
  def __init__( self, header, topic = '', text = '', nodes = [] ) :
    super( DOC_CHAPTER, self ).__init__( header = header, topic = topic )
    self.text = text
    self.nodes = nodes
  def build( self, depth, nodes ) :
    return '\n'.join( self.build_header_elements( depth, nodes ) + self.build_elements( depth, nodes ) )
  def build_header_elements( self, depth, nodes ) :
    return [
      self.build_path( depth ),
      PRE( self.build_text() ),
    ]
  def build_elements( self, depth, nodes ) :
    return self.build_nodes_elements( depth, nodes ) + self.build_topic_elements( depth, nodes )

  def build_content( self, depth, nodes ) :
    return '\n'.join( self.build_content_elements( depth, nodes )  )
  def build_content_elements( self, depth, nodes ) :
    return [
      self.build_path_content( depth ),
      self.build_content_nodes( depth, nodes ),
      self.build_content_topic( depth, nodes ),
    ]
  def build_content_nodes( self, depth, nodes ) :
    return '\n'.join( [ node.build_content( depth + [ i + 1 ], nodes ) for i, node in enumerate( self.nodes ) ] )
  def build_content_topic( self, depth, nodes ) :
    return '\n'.join( [ node.build_content( depth + [ i + 1 ], nodes ) for i, node in enumerate( [ d for d in nodes if self.header == d.topic and self.header != '' ] ) ] )
  def build_nodes_elements( self, depth, nodes ) :
    return [ node.build( depth + [ i + 1 ], nodes ) for i, node in enumerate( self.nodes ) ]
  def build_topic_elements( self, depth, nodes ) :
    return [ node.build( depth + [ i + 1 ], nodes ) for i, node in enumerate( [ d for d in nodes if self.header == d.topic and self.header != '' ] ) ]
  def build_text( self ) :
    result = []
    current_paragraph = ''
    balance = 0
    breaks = 0
    for c in self.text.strip() :

      if c == '\n' and balance == 0 and breaks == 1 :

        result.append( current_paragraph.strip() )
        current_paragraph = ''

      else :

        if c == '(' :
          balance -= 1
        elif c == ')' :
          balance += 1
        elif c == '\n' :
          breaks = +1
        else :
          breaks = 0

        current_paragraph += c

    result.append( current_paragraph.strip() )
    return '\n'.join( [ '\n<p>\n' + p + '\n</p>\n' for p in result if p != '' ] )


class DOC_ROOT_NODE ( DOC_CHAPTER ) :
  def __init__( self, header, text = '', nodes = [] ) :
    super( DOC_ROOT_NODE, self ).__init__( header = header, text = text, nodes = nodes )
    CORE.register_doc_root_node( self )
  def build( self, depth, nodes ) :
    return """
<html>
<head>
<link rel="stylesheet" href="github_markdown.css">
</head>
<body class="markdown-body">
""" + '\n<hr>\n'.join( [ '\n'.join( self.build_header_elements( depth, nodes ) ) ] + self.build_elements( depth, nodes ) ) + """
</body>
</html>
"""
  def build_content( self, depth, nodes ) :
    return '\n'.join( [ node.build_content( depth + [ i + 1 ], nodes ) for i, node in enumerate( self.nodes ) ] )


class DOC_CONTENT ( DOC_NODE ) :
  def __init__( self ) :
    super( DOC_CONTENT, self ).__init__( header = 'Content', topic = '' )
  def build( self, depth, nodes ) :
    return '\n'.join( [ self.build_path( depth ) ] + [ CORE.doc_root_node.build_content( [], CORE.doc_nodes ) ] )
  def build_content( self, depth, nodes ) :
    return self.build_path_content( depth )


class DOC_EMBED ( DOC_NODE ) :
  def __init__( self, source ) :
    super( DOC_EMBED, self ).__init__( header = '', topic = '' )
    self.source = source
  def build( self, depth, nodes ) :
    source = self.get_source( nodes )
    if not source :
      print "Warning: DOC_EMBED source '" + self.source + "' not found"
    return source.build( depth, nodes )
  def build_content( self, depth, nodes ) :
    source = self.get_source( nodes )
    if not source :
      print "Warning: DOC_EMBED source '" + self.source + "' not found"
    return source.build_content( depth, nodes )
  def get_source( self, nodes ) :
    for n in nodes :
      if n.header == self.source :
        return n
    return None



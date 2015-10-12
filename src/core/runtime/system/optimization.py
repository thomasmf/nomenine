

REGISTER_FLAG( 'no_optimize', 'disables non-essential shortcut codepaths' )

def OPT( code ) :
  if not arg_parser_args.no_optimize :
    return PRE( """
      do {
        """ + code + """
        return ;
      } while ( $FALSE ) ;
    """ )
  else :
    return ''


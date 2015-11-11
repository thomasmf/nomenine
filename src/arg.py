

def REGISTER_FLAG( flag, description ) :
  arg_parser_flags.add_argument( '--' + flag, action = 'store_true', help = description )

def arg_get_flag( flag ) :
  return vars( arg_parser_args )[ flag ]

def ENABLED( flag, code ) :
  if arg_get_flag( flag ) :
    return PRE( code )
  else :
    return ''

def DISABLED( flag, code ) :
  if not arg_get_flag( flag ) :
    return PRE( code )
  else :
    return ''



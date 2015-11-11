

# preprocessor:
# python variable: $asdf
# python expression: $( asdf asdf asdf )
#   expression is evaluated as is
# python function call: $asdf( adsf, asdf, asdf )
#   parameters are converted to stripped strings
# result is not repreprocessed, use return PRE( result ) or something
# comments are preprocessed


def is_identifier( c ) :
  return c.isalpha() or c.isdigit() or ( c == '_' )

def PRE( code ) :
  result = ''
  stage = 0
  for c in code :
    if stage == 0 :
      if c == '$' :
        stage = 1
        function_name = ''
      else :
        result += c
    elif stage == 1 :							# get function name
      if c == '(' :
        balance = 1
        if function_name == '' :
          stage = 2
          expression = ''
        else :
          stage = 3
          parameters = []
          parameter = ''
      elif not is_identifier( c ) :
        stage = 0
        if function_name != '' :
          result += str( globals()[ function_name ] ) + c
      else :
        function_name += c
    elif stage == 2 :							# get expression
      if c == '(' :
        balance += 1
      if c == ')' :
        balance -= 1
      if balance == 0 :
        stage = 0
        result += PRE( str( eval( expression, globals(), globals() ) ) )
      expression += c
    elif stage == 3 :							# get parameters for function call
      if c == '(' :
        balance += 1
      if c == ')' :
        balance -= 1
      if balance == 0 :
        stage = 0
        if parameter != '' :
          parameters.append( parameter.strip() )
        result += str( globals()[ function_name ]( * parameters ) )
      if balance == 1 and c == ',' :
        parameters.append( parameter.strip() )
        parameter = ''
      else :
        parameter += c
  return result



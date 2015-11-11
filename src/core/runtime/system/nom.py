

def NOM( context, that, code ) :
  return PRE( """
    nom_do_sync(
      FRAME__TASK_new( """ + context + """, $LAZY( ANY, $CA(CLOSURE_new( ROOT_SCOPE_single(), $CALL( parse, $CA(STRING_new( """ + build_c_string( code ) + """ )) ) )) ), """ + that + """ )
    ) ;
  """ )



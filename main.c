
#include <stdlib.h>
#include <stdio.h>
#include <sysexits.h>

#include "core.h"


int main( int argc, const char* argv[] ) {


  nom_core_init() ;

  if ( argc <= 1 ) {

    nom_core_test() ;

    printf( "\n" ) ;
    printf( "Argument error, missing filename.\n" ) ;
    printf( "Usage: %s <filename>\n", argv[ 0 ] ) ;

  } else {

    nom_run( (n_string)argv[ 1 ] ) ;

  }

  nom_wait_for_all_activity_to_finish() ;

  return EX_OK ;
}




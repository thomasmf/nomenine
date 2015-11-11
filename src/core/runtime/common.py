

APPEND_C( """

#define _GNU_SOURCE

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include <sysexits.h>

#include <pthread.h>
#include <stdarg.h>

$DISABLED( no_gc,
#define GC_THREADS
#include <gc.h>
)

#include "core.h"

""" )


APPEND_H( """

#include <gmp.h>

typedef size_t n_integer ;
typedef char n_character ;
typedef char n_boolean ;
typedef char n_byte ;
typedef n_character* n_string ;
typedef void (*n_objective)( ANY ) ;
typedef n_string (*n_dump)( ANY ) ;

""" )



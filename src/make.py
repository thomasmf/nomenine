

import os
import sys
import re
import copy
import argparse


current_source_filename = ''


def execDirectory( directory, verbose = False ) :

  global CORE, current_source_filename
  program = os.path.realpath( sys.argv[ 0 ] )
  lines = sum( [ 0 if ( l.isspace() ) else 1 for l in open( program ) ] )
  size = os.stat( program ).st_size

  for root, dirs, files in os.walk( directory ) :

    for filename in files :

      full_filename = root + '/' + filename
      current_source_filename = 'src' + full_filename[ len( directory) : ]

      if filename.endswith( ".py" ) and full_filename != program :

        if verbose :
          print 'Including', full_filename, '...',

        lines += sum( [ 0 if ( l.isspace() ) else 1 for l in open( full_filename ) ] )
        size += os.stat( full_filename ).st_size
        execfile( full_filename, globals(), globals() )

        if verbose :
          print 'Ok'

      elif verbose :
        print 'Skipping', full_filename

    if CORE == None :
      CORE = BUILDER()

  if verbose :
    print 'Input size:', lines, 'lines', size, 'bytes'



arg_parser = argparse.ArgumentParser( add_help = False )

arg_parser.add_argument( '-v', '--verbose', action = 'store_true', help = 'verbose output' )
arg_parser.add_argument( '-h', '--help', action = 'store_true', help = 'show this help message and exit' )

arg_parser_flags = arg_parser.add_argument_group( 'flags' )

arg_parser_args, arg_parser_unknown_args = arg_parser.parse_known_args()

CORE = None

execDirectory( os.path.dirname( os.path.realpath( sys.argv[ 0 ] ) ), arg_parser_args.verbose )

arg_parser_args = arg_parser.parse_args()

if arg_parser_args.help :
  print arg_parser.print_help()
else :
  CORE.fix()
  CORE.write_to_files( 'core' )



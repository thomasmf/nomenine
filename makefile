
CC=gcc

CFLAGS=-c -g -O2 -std=gnu99 -Wall -Winline -I/usr/include/gc -pthread

all:		nomenine

nomenine:	core.o main.o
		$(CC) core.o -lgc main.o -pthread -lgmp -o nomenine

main.o:	core.o main.c
		$(CC) $(CFLAGS) main.c

core.o:	FORCE
#		python src/make.py --call_by_future --type_checks --informative_errors
#		python src/make.py --call_by_future
#		python src/make.py --map_evaluation --map_parsing
#		python src/make.py --no_optimize --type_checks --informative_errors
#		python src/make.py --informative_errors	--type_checks --detach_threads
		python src/make.py --informative_errors	--type_checks
#		python src/make.py --no_optimize
#		python src/make.py
#		python src/make.py --detach_threads
#		python src/make.py --list_used_methods
#		python src/make.py --no_gc --no_optimize
#		python src/make.py --no_gc
#		python src/make.py --no_gc --call_by_future --detach_threads                       # causes unit test for lazy lists to fail sometimes
		$(CC) $(CFLAGS) core.c
		cp readme.html README.md



clean:
		rm *.o core.c core.h *.pyc nomenine *.h.gch *~ readme.html

FORCE:



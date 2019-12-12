clib.so: clib.o
	gcc -shared -o libclib.so clib.o
	
clib.o: clib.c
	gcc -c clib.c
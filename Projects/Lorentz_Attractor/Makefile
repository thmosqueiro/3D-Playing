CC = gcc
LDFLAGS= -L/usr/lib64 -lsundials_cvode -lsundials_nvecserial -lm


lorentz: $(OBJECTS)
	$(CC) -o Lorentz Lorentz.c $(LDFLAGS)


run: Lorentz
	./Lorentz

all : lorentz run clean

clean :
	rm -f *.o *~ Lorentz

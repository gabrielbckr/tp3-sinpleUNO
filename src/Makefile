RANDPORT:=$(shell python -c 'from random import randint; print(randint(2500, 4500));')

all:	
	x-terminal-emulator -e   python	servidor.py $(RANDPORT) 2
	python cliente.py local $(RANDPORT)
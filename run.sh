#!/bin/bash
RANDPORT=$(python -c 'from random import randint; print(randint(2500, 4500));')
echo "PORT IS $RANDPORT"
	
gnome-terminal -e "python	src/servidor.py $RANDPORT 1"
sleep 1
gnome-terminal -e  "python src/cliente.py local $RANDPORT"
sleep 1
python src/cliente.py local $RANDPORT
#!/bin/bash
RANDPORT=$(python -c 'from random import randint; print(randint(2500, 4500));')
NUM=2
if [ $# != 0 ] 
then
    NUM="$1"
fi
echo "PORT IS $RANDPORT"
echo "Deploy server"
x-terminal-emulator -e "python	src/servidor.py $RANDPORT $NUM"
sleep 1
ii=0
while [ "$ii" -lt "$NUM" ]
    do
        echo "Deploy client `expr $ii + 1` of $NUM"
        x-terminal-emulator -e  "python src/cliente.py local $RANDPORT"
        sleep 1
        ii=`expr $ii + 1`
done
python src/cliente.py local $RANDPORT
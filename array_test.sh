#!/bin/bash
length= 0

while [[ 1 ]]
do
        echo "Enter a new word:"
        read command
        if [ $command == "list" ]; then
                for i in ${array[*]}
                do
                        echo "$i"" "
                done
        elif [ $command == "quit" ]; then
                break
        else
                array+=$command
                let length+=1
                echo "Length:$length"
        fi
done


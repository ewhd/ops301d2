#!/bin/bash

# Script:                       challenge304-menu-conditionals.sh
# Author:                       Ethan Denny
# Date of latest revision:      3/4/2021
# Purpose:     
#               This script launches a menu system, gets a selection input from the user, then 
#               uses a conditional statement to figure the selection, then a loop to bring the
#               menu back up again.

# Define Variables

input_var=""

# Define Functions

option_selector() {
    if [[ $input_var == 1 ]]; then
        echo "Hello World"
    elif [[ $input_var == 2 ]]; then
        ping -c 4 127.0.0.1
    elif [[ $input_var == 3 ]]; then
        ip a
    elif [[ $input_var == 4 ]]; then
        exit
    else
        echo "
            Invalid input. PLease try again.
            "
    fi
}

# Menu

while true; do
    echo "
    Please select from the following optinos:
        1. Hello world (prints “Hello world!” to the screen)
        2. Ping self (pings this computer’s loopback address)
        3. IP info (print the network adapter information for this computer)
        4. Exit

    "
    read -p "Input option (1/2/3/4): " input_var
    option_selector
done


# End
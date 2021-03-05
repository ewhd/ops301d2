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
    if [[ $input_var == 2 ]]; then
        ping 127.0.0.1
    if [[ $input_var == 3 ]]; then
        ip a
    if [[ $input_var == 4 ]]; then
        exit
}

# Menu

while true; do
    echo "option menu"
    read input_var
    option_selector
done


# End
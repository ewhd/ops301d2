#!/bin/bash

# Script:                       challenge305-clear-logs.sh
# Author:                       Ethan Denny
# Date of latest revision:      3/5/2021
# Purpose:     
#   This script contains a function clear the contents of any file in /var/log/
#   while narrating the process to the using and showing the file's contents before
#   and after.
#   It also contains a de-fanged, test version of the script, for testing and demon-
#   stration purposes.
#   IMPORTANT: Because this script is designed to modify system files, it must be run
#   as root.


# Define Variables


# Define Functions

# This function takes the name of a file within /var/log/ as an argument, 
# prints the contents, confirms the user would like to clear said contents,
# sends the content to /dev/null, and prints the new contents of the file 
# which is nothing.
clear_log() {
    # Print the contents of the log file:
    read -p "    Press any key to display the contents of /var/log/$1
    "
    cat /var/log/$1

    # Now clear the contents of the log:
    read -p "    
    Press any key to clear /var/log/$1 (or Ctrl-C to exit):
    "
    cat /dev/null > /var/log/$1

    # Print the contents of the log file (should be empty):
    read -p "    Press any key to display the current contents of /var/log/$1
    "
    cat /var/log/$1
    sleep 1
    echo "    Function finished
    "
}


# As clear_log() above, except this version takes the name of a file within 
# /var/log/ as an argument, copies that file to the current directory, then 
# performs the same operations (printing, confirming, clearing, printing).
# At the end, the copied (and now empty) file is removed.
clear_log_test() {
    # Copy file to current directory so I can test it multiple times:
    cp /var/log/$1 .

    # Print the contents of the log file:
    read -p "    Press any key to display the contents of /var/log/$1
    "
    cat $1

    # Now clear the contents of the log:
    read -p "
    Press any key to clear /var/log/$1 (or Ctrl-C to exit):
    "
    cat /dev/null > $1

    # Print the contents of the log file (should be empty):
    read -p "    Press any key to display the current contents of /var/log/$1
    "
    cat $1
    sleep 1
    echo "    Function finished
    "

    # Remove the copied file as cleanup:
    rm $1

}

# Main

#clear_log_test syslog
#clear_log_test wtmp

clear_log syslog
clear_log wtmp


# End
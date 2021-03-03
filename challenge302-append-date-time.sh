#!/bin/bash

# Script:                       challenge302-append-date-time.sh
# Author:                       Ethan Denny
# Date of latest revision:      3/2/2021
# Purpose:     
#               Copies /var/log/syslog to the current directory
#               Appends the current date and time to the file


# Main

# This line copies /var/log/syslog to the current directory
cp /var/log/syslog $(pwd)

# This line appends the current date and time to the file
# In the format "Mar  2 18:14:00"
# I note that syslog uses UTC, hence the -u suffix
echo $(date +%b -u) $(date +%e -u) $(date +%X -u) >> syslog


# End
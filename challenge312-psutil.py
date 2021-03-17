#!/user/bin/env python3

# Script:                       challenge312-psutil.py
# Author:                       Ethan Denny
# Date of latest revision:      3/16/2021
# Purpose:     Fetch information using Psutil
# This script fetches the following information using psutil:
    # Time spent by normal processes executing in user mode
    # Time spent by processes executing in kernel mode
    # Time when system was idle
    # Time spent by priority processes executing in user mode
    # Time spent waiting for I/O to complete.
    # Time spent for servicing hardware interrupts
    # Time spent for servicing software interrupts
    # Time spent by other operating systems running in a virtualized environment
    # Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel
# It formats and labels this information and saves it to a text file


import psutil, os


# Define Variables

# This line stores the output of psutil.cpu_times() as a variable to avoid calling
# the function multiple times
psutil_cpu_times_var = psutil.cpu_times()

# This variable will hold all of the output and explanation text. This allows the script to write out
# to the file all at once instead of multiple times
output_to_write = ""


#  Main

# This line opens a file to write the output to
output_file = open("cpu_times_report.txt", "a")

# This section calls elements from the stored output of psutil.cpu_times(), converts them into a string, 
# and concatonates them together along with explanation text and line breaks, and adds each string to the
# output_to_write variable
output_to_write += \
    "Time spent by normal processes executing in user mode: " + str(psutil_cpu_times_var[0]) + "\n" +\
    "Time spent by processes executing in kernel mode:" + str(psutil_cpu_times_var[2]) + "\n" +\
    "Time when system was idle:" + str(psutil_cpu_times_var[3]) + "\n" +\
    "Time spent by priority processes executing in user mode:" + str(psutil_cpu_times_var[1]) + "\n" +\
    "Time spent waiting for I/O to complete:" + str(psutil_cpu_times_var[4]) + "\n" +\
    "Time spent for servicing hardware interrupts:" + str(psutil_cpu_times_var[5]) + "\n" +\
    "Time spent for servicing software interrupts:" + str(psutil_cpu_times_var[6]) + "\n" +\
    "Time spent by other operating systems running in a virtualized environment:" + str(psutil_cpu_times_var[7]) + "\n" +\
    "Time spent by normal processes executing in user mode:" + str(psutil_cpu_times_var[8])

# This section writes the colelctive output to the file and closes the file
output_file.write(output_to_write)
output_file.close()


# End
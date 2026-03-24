#!/bin/bash
#Outputs the status for the step (apt update), exits if update fails 
#IMPORTANT : (no step shall be executed if the packets are not updated for security reasons)
if [ $1 -eq 0 ]; then
    echo -e "\e[1;32mSystem Updated Successfully !\e[0m"
else
    echo -e "\e[1;31mSystem Update Failure ! exiting to prevent zero day exploits\e[0m"
    exit 1
fi
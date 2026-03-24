#!/bin/bash
#Outputs the status for the step (packages installation via apt)
if [ $1 -eq 0 ]; then
    echo -e "\e[1;32mAll packages installed Successfully !\e[0m"
else
    echo -e "\e[1;31mOne or more packages failed during installation !\e[0m"
fi
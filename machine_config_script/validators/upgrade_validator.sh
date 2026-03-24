#!/bin/bash
#Outputs the status for the step (apt upgrade)
if [ $1 -eq 0 ]; then
    echo -e "\e[1;32mSystem Upgraded Successfully !\e[0m"
else
    echo -e "\e[1;31mSystem Upgrad Failure !\e[0m"
fi
#!/bin/bash
#Outputs the status for the step (git main branch config) 
if [ $1 -eq 0 ]; then
    echo -e "\e[1;32m$2 has been set as principal branch\e[0m"
else
    echo -e "\e[1;31mFailed to set $2 as a principal branch !\e[0m"
fi
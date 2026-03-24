#!/bin/bash
#Outputs the status for the step (git credentials)
if [ $1 -eq 0 ]; then
    echo -e "\e[1;32m$2 has been set as a Git credential !\e[0m"
else
    echo -e "\e[1;31mFailed to set $2 as a git credential!\e[0m"
fi
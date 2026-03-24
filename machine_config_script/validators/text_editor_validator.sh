#!/bin/bash
#Outputs the status for the step (default text editor configuration)
if [ $1 -eq 0 ]; then
    echo -e "\e[1;32mVim Basic is now the default text editor\e[0m"
else
    echo -e "\e[1;31Failed to set Vim Basic as default text editor !\e[0m"
fi
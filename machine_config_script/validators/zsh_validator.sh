#!/bin/bash
#Outputs the status for the step (is ZSH installed)
if [ $1 -eq 0 ]; then
    echo -e "\e[1;32mZsh FOUND!\e[0m"
    chsh -s $(which zsh)
    if [ $1 -eq 0 ]; then
         echo -e "\e[1;32mZsh is now default SHELL !\e[0m"
    else
         echo -e "\e[1;32mFailed to set ZSH as default SHELL\e[0m"
    fi
else
    echo -e "\e[1;31mZSH not installed on the machine!\e[0m"
fi

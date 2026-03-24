#!/bin/bash

#This scripts sets the git crednetials, Username EMail and main branch
USER_NAME="benoui_m"
USER_EMAIL="benoui_m@etna-alternance.net"
DEFAULT_BRANCH="main"
#funny Git  Step Announcer !
/usr/games/cowsay SETTING GIT CRETENTIALS AND MAIN BRANCH
#checks if git has been properly installed, if not skipps this step
git --version >/dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "\e[1;31mGit is NOT installed skipping git configuration...\e[0m"else
    return 0
fi


echo -e "Generating .gitconfig file ..."
touch "$HOME/.gitconfig"
git config --file $HOME/.git_config user.name "$USER_NAME"
./validators/git_setting_validator.sh "$?" "$USER_NAME"
git config --file $HOME/.git_config user.email "$USER_EMAIL"
./validators/git_setting_validator.sh "$?" "$USER_EMAIL"
git config --file ~/.git_config init.defaultBranch "$DEFAULT_BRANCH"
./validators/git_branch_validator.sh "$?" "$DEFAULT_BRANCH"
echo -e "$HOME/.gitconfig file configured."




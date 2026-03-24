#!/bin/bash
PACKETS="git curl wget zsh vim sl cowsay autojump fzf"
#Timeout check if script takes too long
TIMEOUT=90
trap "echo 'Setup is taking too much time, check your internet connexion'; exit 1" SIGTERM

(
    sleep $TIMEOUT
    echo -e "\e[1;31mTimeout reached. Exiting...\e[0m"
    kill $$  # kills the main script
) &
TIMER_PID=$!

# SYSTEM UPDATE
apt-get update
./validators/update_validator.sh "$?"

# SYSTEM UPGRADE
apt-get upgrade -y
./validators/upgrade_validator.sh "$?"

# INSTALL PACKAGES
apt-get install -y $PACKETS
./validators/packages_install_validator.sh "$?"

# GIT CONFIG
./git_setters/git_setter.sh

# DEFAULT TEXT EDITOR CONFIG
echo -e "Setting default text editor to vim Basic ..."
update-alternatives --set editor /usr/bin/vim.basic
./validators/text_editor_validator.sh "$?"

# CHECK ZSH INSTALLATION
which zsh >/dev/null 2>&1
./validators/zsh_validator.sh "$?"

# INSTALL OH-MY-ZSH FOR THE USER
RUNZSH=no CHSH=no sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" >> /dev/null 2>&1
chsh -s $(which zsh)

# CONFIGURE .zshrc
#touch "$HOME/.zshrc"
sed -i 's/^plugins=.*/plugins=(git z autojump fzf history-substring-search colored-man-pages)/' "$HOME/.zshrc"
THEME="agnoster"
sed -i "s/^ZSH_THEME=.*/ZSH_THEME=\"$THEME\"/" "$HOME/.zshrc"

# Add alias only if it does not exist
grep -qxF "alias gs='git status'" "$HOME/.zshrc" || \
echo "alias gs='git status'" >> "$HOME/.zshrc"

#source function file and run vimrc setting function
source ./vim_setters/vim_setter.sh
setup_vimrc

# FUN
/usr/games/sl -a
echo "YOU SHALL NOW START HACKING THE WORLD!"

kill $TIMER_PID

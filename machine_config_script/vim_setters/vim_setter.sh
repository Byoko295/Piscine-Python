#!/bin/bash
#set vimrc_config
setup_vimrc() {
    local file="$HOME/.vimrc"

    # create file if it doesn't exist
    touch "$file"

    # only add config block if it isn't already there
    if ! grep -q "dotfiles-basic-config" "$file"; then
        cat >> "$file" <<'EOF'

" dotfiles-basic-config
set number
set tabstop=4
set shiftwidth=4
set expandtab
syntax on
EOF
    fi
}
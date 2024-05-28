#!/bin/bash
CONFIG="./config.toml"

# extremely simplified script from: https://stackoverflow.com/a/26035652

function set_config(){
    sudo sed -i "s/^\($1\s*=\s*\).*\$/\1$2/" $CONFIG
}

set_config $1 $2 # SETS THE NEW VALUE
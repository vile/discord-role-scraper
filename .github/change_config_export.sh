#!/bin/bash
CONFIG="./config.toml"

# extremely simplified script from: https://stackoverflow.com/a/26035652

function set_config(){
    sudo sed -i "s/^\($1\s*=\s*\).*\$/\1$2/" $CONFIG
}

export_results=$1
set_config export_results $export_results # SETS THE NEW VALUE
#!/usr/bin/env bash
#############################################################################
#   __                          (`/\                                        #
#  |  |--.--.--.----.-----.-----`=\/\   This file is part of byron v0.1     #
#  |  _  |  |  |   _|  _  |     |`=\/\  An evolutionary optimizer & fuzzer  #
#  |_____|___  |__| |_____|__|__| `=\/  https://github.com/squillero/byron  #
#        |_____|                     \                                      #
#############################################################################
# Copyright 2022-23 Giovanni Squillero and Alberto Tonda
# SPDX-License-Identifier: Apache-2.0

if [[ $1 == -f ]]; then
    shift
    genomes=$(tail -1 -q "$@")
else
    genomes="$*"
fi

for g in $genomes; do
    ret="${g//[^1]}"
    echo ${#ret}
done

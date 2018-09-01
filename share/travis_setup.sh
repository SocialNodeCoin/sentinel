#!/bin/bash
set -evx

mkdir ~/.allgamescoincore

# safety check
if [ ! -f ~/.allgamescoincore/.allgamescoin.conf ]; then
  cp share/allgamescoin.conf.example ~/.allgamescoincore/allgamescoin.conf
fi

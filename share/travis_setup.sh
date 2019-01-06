#!/bin/bash
set -evx

mkdir ~/.decentralwaycore

# safety check
if [ ! -f ~/.decentralwaycore/.decentralway.conf ]; then
  cp share/decentralway.conf.example ~/.decentralwaycore/decentralway.conf
fi

#!/bin/bash
# script that takes URL and sends post request
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"

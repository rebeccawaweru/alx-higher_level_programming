#!/bin/bash
# script that sends JSON file and display body response
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"

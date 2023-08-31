#!/bin/bash
# script that takes urls and displays all HTTP methods accepted
curl -sI "$1" | grep "Allow:" | sed -ne 's/^Allow: //p'

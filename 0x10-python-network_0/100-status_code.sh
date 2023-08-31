#!/bin/bash
# script that sends request to URL and display only status code of response
curl -so /dev/null --write-out "%{http_code}" "$1"

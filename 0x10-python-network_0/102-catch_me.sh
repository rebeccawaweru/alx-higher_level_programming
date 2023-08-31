#!/bin/bash
# script that makes request to 0.0.0.0:5000/catch_me that causes server to respond with message You got me!
curl -sLX PUT -d "user_id=98" -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me

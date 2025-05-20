#!/bin/sh

docker rm -f web_flag_command 2>/dev/null
docker build -t web_flag_command .
docker run -d -p 5001:5000 --name web_flag_command web_flag_command
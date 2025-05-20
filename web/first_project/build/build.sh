#!/bin/sh

docker rm -f web_first_project 2>/dev/null
docker build -t web_first_project .
docker run -d -p 5000:5000 --name web_first_project web_first_project
#!/bin/sh

docker rm -f web_the_finder 2>/dev/null
docker build -t web_the_finder .
docker run -d -p 5006:8000 --name web_the_finder web_the_finder
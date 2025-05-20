#!/bin/sh

docker rm -f expme 2>/dev/null
docker build -t expme .
docker run -d -p 4003:1337 --name expme expme
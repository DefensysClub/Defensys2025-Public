#!/bin/sh

docker rm -f coin_flip 2>/dev/null

docker build -t coin_flip .
docker run -d -p 4001:1337 --name coin_flip coin_flip
#!/bin/sh

docker rm -f elden_ring 2>/dev/null

docker build -t elden_ring .
docker run -d --rm -p 8000:80 --name elden_ring elden_ring
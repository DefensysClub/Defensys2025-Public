#!/bin/sh

# Stop and remove any existing container named "sharing"
docker rm -f sharing 2>/dev/null

# Build and run the new container
docker build -t sharing .
docker run -d -p 4002:1337 --name sharing sharing
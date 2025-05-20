#!/bin/sh

docker rm -f web_premium_access 2>/dev/null
docker build -t web_premium_access .
docker run -d -p 5005:5000 --name web_premium_access web_premium_access
#!/bin/sh

docker rm -f web_ott 2>/dev/null
docker build -t web_ott .
docker run -d --rm -p 5004:5000 --name web_ott web_ott
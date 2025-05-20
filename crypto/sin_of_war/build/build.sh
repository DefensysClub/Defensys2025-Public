#!/bin/sh


docker rm -f sin_of_war 2>/dev/null
docker build -t sin_of_war .
docker run -d -p 4000:1337 --name sin_of_war sin_of_war
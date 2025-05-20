#!/bin/sh

docker rm -f secrets_vault 2>/dev/null
docker build -t secrets_vault .
docker run -d -p 4010:1337 --name secrets_vault secrets_vault
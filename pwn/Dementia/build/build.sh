#!/bin/sh

docker rm -f dementia 2>/dev/null
docker build -t dementia .
docker run --privileged --rm -it -d --cap-add=SYS_ADMIN --cap-add=SYS_PTRACE --cap-add=CAP_SYS_CHROOT --security-opt seccomp=unconfined -p 1333:5000 dementia:latest

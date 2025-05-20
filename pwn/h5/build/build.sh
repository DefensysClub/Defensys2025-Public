#!/bin/sh


docker rm -f hfive 2>/dev/null
docker build -t hfive .
docker run --rm -it --cap-add=SYS_ADMIN --cap-add=SYS_PTRACE --cap-add=CAP_SYS_CHROOT --security-opt seccomp=unconfined -p 1339:5000 hfive

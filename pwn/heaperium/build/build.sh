#!/bin/sh

docker rm -f heaperium 2>/dev/null
docker build -t heaperium .
docker run --rm -it --cap-add=SYS_ADMIN --cap-add=SYS_PTRACE --cap-add=CAP_SYS_CHROOT --security-opt seccomp=unconfined -p 1340:5000 heaperium

#!/bin/sh

docker rm -f ret2lose 2>/dev/null
docker build -t ret2lose .
docker run --privileged --rm -it -d --cap-add=SYS_ADMIN --cap-add=SYS_PTRACE --cap-add=CAP_SYS_CHROOT --security-opt seccomp=unconfined -p 1235:5000 --name ret2lose ret2lose

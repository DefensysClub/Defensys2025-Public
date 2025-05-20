#!/bin/sh


docker rm -f libra 2>/dev/null
docker build -t libra .
docker run --rm -it --cap-add=SYS_ADMIN --cap-add=SYS_PTRACE --cap-add=CAP_SYS_CHROOT --security-opt seccomp=unconfined -p 1341:5000 libra

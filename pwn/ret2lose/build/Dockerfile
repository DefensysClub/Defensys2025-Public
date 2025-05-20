FROM alpine:latest AS builder

RUN apk add --no-cache g++ make

WORKDIR /app

COPY ret2lose.c .
COPY flag.txt .

#change this to the correct compilation command
RUN gcc -o ret2lose ret2lose.c -fno-stack-protector -no-pie -Wno-implicit-function-declaration -fcf-protection=full

FROM alpine:latest

RUN apk add --no-cache socat

WORKDIR /app
COPY --from=builder /app/ret2lose .

RUN printf '#!/bin/sh\nsocat TCP-LISTEN:1337,reuseaddr,fork EXEC:"/app/ret2lose"\n' > /entrypoint.sh && \
    chmod +x /entrypoint.sh

EXPOSE 1337
ENTRYPOINT ["/entrypoint.sh"]

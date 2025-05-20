FROM alpine:latest AS builder

RUN apk add --no-cache g++ make

WORKDIR /app
COPY secrets_vault.cpp .

RUN g++ -o secrets_vault secrets_vault.cpp -O2 -static -s

FROM alpine:latest

RUN apk add --no-cache socat

WORKDIR /app
COPY --from=builder /app/secrets_vault .

RUN printf '#!/bin/sh\nsocat TCP-LISTEN:1337,reuseaddr,fork EXEC:"/app/secrets_vault"\n' > /entrypoint.sh && \
    chmod +x /entrypoint.sh

ENV FLAG=defensys{fnv1_hash_ftw_bruh_3214141234}

EXPOSE 1337
ENTRYPOINT ["/entrypoint.sh"]
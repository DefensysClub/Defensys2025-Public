FROM sagemath/sagemath:9.8

USER root
RUN apt-get update \
 && apt-get install -y socat \
 && rm -rf /var/lib/apt/lists/*

USER sage
WORKDIR /home/challenge

COPY chall.sage flag.txt ./

EXPOSE 1337


CMD ["socat", "TCP-LISTEN:1337,reuseaddr,fork", "EXEC:\"sage chall.sage\",pty,stderr"]

FROM python:3.9-slim

RUN /usr/sbin/useradd --no-create-home -u 1000 user
WORKDIR /home/user

COPY chall.py /home/user/
RUN apt-get update && apt-get install -y socat && rm -rf /var/lib/apt/lists/*
COPY requirements.txt /home/user/
RUN pip install --no-cache-dir -r /home/user/requirements.txt

CMD socat \
      TCP-LISTEN:1337,reuseaddr,fork \
      EXEC:"python /home/user/chall.py"

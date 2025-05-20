#!/bin/bash

while true; do
    gunicorn --bind 0.0.0.0:5000 app:app &
    APP_PID=$!

    sleep 300

    kill $APP_PID

    rm -f /app/token.db
done
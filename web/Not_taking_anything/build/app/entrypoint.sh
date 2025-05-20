#!/bin/bash

while true; do
    echo "Starting Flask server with Gunicorn..."
    gunicorn --chdir /app app:app -b 0.0.0.0:8081 &
    GUNICORN_PID=$!

    sleep 600

    echo "Stopping Flask server..."
    kill $GUNICORN_PID
    
    echo "Deleting sqlite.db file..."
    rm -f /app/users.db /app/notes.db
done
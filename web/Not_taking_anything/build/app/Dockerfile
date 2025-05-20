FROM python:3.8

ENV DISPLAY=:99

RUN pip install --upgrade pip
RUN pip install flask
RUN pip install flask_session
RUN pip install pyjwt
RUN pip install gunicorn


COPY . /app
WORKDIR /app

EXPOSE 8081

CMD ["python", "./app.py"]
#CMD ["./entrypoint.sh"]
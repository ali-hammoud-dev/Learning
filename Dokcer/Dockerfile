FROM python:3.8

RUN python3 -m pip install flask
RUN mkdir /app
WORKDIR /app

COPY app.py /app/

EXPOSE 5000

ENV FLASK_APP=app.py
CMD ["flask", "run", "--host=0.0.0.0"]
# FROM python:3.8

# RUN python3 -m pip install flask
# RUN mkdir /app
# WORKDIR /app

# COPY app.py /app/

# EXPOSE 5000

# ENV FLASK_APP=app.py
# CMD ["flask", "run", "--host=0.0.0.0"]
FROM python:3.10
EXPOSE 5000
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD [ "flask","run","--host","0.0.0.0" ]

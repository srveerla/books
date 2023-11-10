FROM python:3.8-slim

WORKDIR /app

COPY . /app

RUN pip install --trusted-host pypi.python.org Flask Flask-PyMongo

EXPOSE 5001

CMD ["python", "app.py"]

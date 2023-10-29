FROM python:3.11-slim-buster

WORKDIR /app

COPY requirements.txt .
RUN pip install -no-cache-dir -r requirements.txt

COPY src /app/src

ENTRYPOINT ["python", "/app/src/main.py"]

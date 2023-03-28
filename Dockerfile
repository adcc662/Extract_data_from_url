FROM python:3.10-slim-buster

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app
COPY app.py .

CMD ["python", "app.py"]
FROM python:3.9.12-alpine3.15

EXPOSE 5001
WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "--bind", "0.0.0.0:$PORT", "wsgi:app"]

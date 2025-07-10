FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN --no-cache-dir -r reqirements.txt

EXPOSE 5000

CMD ["python","app.py"]
# UPI Payment Tracker API (Mock)

A simple mock UPI payment system to demonstrate DevOps skills using Flask, Docker, and AWS EC2.

## Features

- `POST /pay` - Create a fake payment request
- `GET /status/<id>` - Get mock status (success, failed, pending)

## Stack

- Flask (Python)
- Docker
- AWS EC2 (Ubuntu)

## Deployment

```bash
sudo docker build -t upi-tracker .
sudo docker run -d -p 5000:5000 upi-tracker

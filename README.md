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

```

# 📸 Screenshots

## ✅ Flask app running on Docker inside AWS EC2
<img width="1913" height="632" alt="Screenshot 2025-07-10 220020" src="https://github.com/user-attachments/assets/2271cc2b-af0c-496a-ae86-c5aee3a34c01" />

<img width="1660" height="596" alt="Screenshot 2025-07-10 220100" src="https://github.com/user-attachments/assets/47811c82-3757-41bd-9bd7-175e75b6c5dc" />




## 📬 Successful API test in Postman


<img width="1396" height="790" alt="Screenshot 2025-07-10 215753" src="https://github.com/user-attachments/assets/5d54a0fb-615e-429c-a5e9-6a77dc126408" />


<img width="1382" height="741" alt="Screenshot 2025-07-10 215717" src="https://github.com/user-attachments/assets/e6a2fc3a-5f93-4a83-81b0-9dffb831b7ef" />


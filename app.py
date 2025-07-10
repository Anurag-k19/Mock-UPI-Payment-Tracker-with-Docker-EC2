from flask import Flask, request, jsonify
import random
import uuid

app = Flask(__name__)


payments = {}

@app.route("/pay", methods=["POST"])
def pay():
    data = request.json
    payment_id = str(uuid.uuid4())
    status = random.choice(["success", "pending", "failed"])

    payments[payment_id] = {
        "name": data.get("name"),
        "upi": data.get("upi"),
        "amount": data.get("amount"),
        "status": status
    }

    return jsonify({"payment_id": payment_id, "status": status})

@app.route("/status/<payment_id>", methods=["GET"])
def status(payment_id):
    if payment_id not in payments:
        return jsonify({"error": "Invalid Payment ID"}), 404
    return jsonify(payments[payment_id])

@app.route("/")
def home():
    return "Mock UPI Payment Tracker is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

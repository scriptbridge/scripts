"""
Sample Fishbowl Inventory script: Fetch the last 10 sales orders sorted by date.
"""
import requests
import json

FISHBOWL_HOST = "http://localhost:28192"
USERNAME = "your_username"
PASSWORD = "your_password"

# Authenticate
login_payload = {
    "IAID": 1234,
    "IAName": "ScriptBridge",
    "IAVersion": "1.0",
    "username": USERNAME,
    "password": PASSWORD
}
response = requests.post(f"{FISHBOWL_HOST}/api/login", json=login_payload)
response.raise_for_status()
session_token = response.json().get("sessionId")

# Get sales orders
headers = {"Authorization": session_token}
params = {"sortOrder": "desc", "sortBy": "dateIssued", "pageSize": 10}
so_response = requests.get(f"{FISHBOWL_HOST}/api/salesorder", headers=headers, params=params)
so_response.raise_for_status()
sales_orders = so_response.json()

# Pretty print
print(json.dumps(sales_orders, indent=2))

# real_time_tracking.py
import time
import random

def track_package():
    statuses = [
        "Shipment Accepted",
        "In Transit",
        "Out for Delivery",
        "Delivered"
    ]

    for status in statuses:
        print(f"Current Status: {status}")
        time.sleep(random.randint(1, 3))

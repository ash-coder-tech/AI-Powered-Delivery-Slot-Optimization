# slot_allocator.py
def assign_delivery_slot(predicted_time):
    if predicted_time <= 60:
        return "09:00 AM - 11:00 AM"
    elif predicted_time <= 120:
        return "11:00 AM - 02:00 PM"
    else:
        return "02:00 PM - 06:00 PM"

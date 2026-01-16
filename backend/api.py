from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import os

from slot_allocator import assign_delivery_slot

app = Flask(__name__)
CORS(app)  # Enable CORS for React frontend

# Load ML model
MODEL_PATH = "delivery_time_model.pkl"

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError("Trained model not found. Please run train_model.py first.")

model = joblib.load(MODEL_PATH)

@app.route("/predict-delivery", methods=["POST"])
def predict_delivery():
    try:
        data = request.get_json()

        # Input validation
        required_fields = ["distance_km", "traffic_level", "weather"]
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing field: {field}"}), 400

        distance = float(data["distance_km"])
        traffic = int(data["traffic_level"])
        weather = int(data["weather"])

        # ML prediction
        features = [[distance, traffic, weather]]
        predicted_time = model.predict(features)[0]

        # Dynamic slot allocation
        slot = assign_delivery_slot(predicted_time)

        return jsonify({
            "predicted_delivery_time_minutes": round(predicted_time, 2),
            "delivery_slot": slot
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "API is running"})


if __name__ == "__main__":
    app.run(debug=True)

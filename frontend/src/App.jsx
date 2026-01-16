import React, { useState } from "react";
import "./App.css";

function App() {
  const [distance, setDistance] = useState("");
  const [traffic, setTraffic] = useState("1");
  const [weather, setWeather] = useState("0");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);

    const response = await fetch("http://127.0.0.1:5000/predict-delivery", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        distance_km: Number(distance),
        traffic_level: Number(traffic),
        weather: Number(weather),
      }),
    });

    const data = await response.json();
    setResult(data);
    setLoading(false);
  };

  return (
    <div className="container">
      <h1>📦 AI Delivery Slot Optimization</h1>

      <form onSubmit={handleSubmit}>
        <label>Distance (km)</label>
        <input
          type="number"
          value={distance}
          onChange={(e) => setDistance(e.target.value)}
          required
        />

        <label>Traffic Level</label>
        <select value={traffic} onChange={(e) => setTraffic(e.target.value)}>
          <option value="1">Low</option>
          <option value="2">Medium</option>
          <option value="3">High</option>
        </select>

        <label>Weather</label>
        <select value={weather} onChange={(e) => setWeather(e.target.value)}>
          <option value="0">Clear</option>
          <option value="1">Rain</option>
        </select>

        <button type="submit">Predict</button>
      </form>

      {loading && <p>Predicting delivery time...</p>}

      {result && (
        <div className="result">
          <h3>Prediction Result</h3>
          <p>
            <strong>Estimated Time:</strong>{" "}
            {result.predicted_delivery_time_minutes} minutes
          </p>
          <p>
            <strong>Delivery Slot:</strong> {result.delivery_slot}
          </p>
        </div>
      )}
    </div>
  );
}

export default App;

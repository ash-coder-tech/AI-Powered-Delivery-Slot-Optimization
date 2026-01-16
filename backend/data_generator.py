# data_generator.py
import pandas as pd
import numpy as np

def generate_data(samples=1000):
    data = {
        "distance_km": np.random.uniform(1, 40, samples),
        "traffic_level": np.random.randint(1, 4, samples),  # 1=Low, 3=High
        "weather": np.random.randint(0, 2, samples),        # 0=Clear, 1=Rain
        "delivery_time_min": np.random.uniform(25, 160, samples)
    }
    return pd.DataFrame(data)

if __name__ == "__main__":
    df = generate_data()
    df.to_csv("delivery_data.csv", index=False)
    print("Delivery data generated")

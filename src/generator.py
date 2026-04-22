import pandas as pd
import numpy as np

def generate_telemetry_data(laps=10, points_per_lap=200):
    data = []

    for lap in range(1, laps + 1):
        base_speed = np.random.uniform(140, 180)

        for t in range(points_per_lap):
            throttle = np.random.uniform(40, 100)
            track_factor = np.random.uniform(0.85, 1.05)

            speed = base_speed * (throttle / 100) * track_factor
            acceleration = np.random.uniform(-3, 3)

            data.append({
                "lap": lap,
                "time_step": t,
                "speed": speed,
                "throttle": throttle,
                "acceleration": acceleration,
                "track_factor": track_factor
            })

    df = pd.DataFrame(data)
    df.to_csv("data/synthetic_telemetry.csv", index=False)

    return df

import pandas as pd
import numpy as np
from src.pitstop import generate_pit_stops, apply_pit_stop_effects

def generate_telemetry_data(laps=10, points_per_lap=200):
    data = []

    pit_stops = generate_pit_stops(laps)

    for lap in range(1, laps + 1):
        base_speed = np.random.uniform(140, 180)

        for t in range(points_per_lap):
            throttle = np.random.uniform(40, 100)
            track_factor = np.random.uniform(0.85, 1.05)

            speed = base_speed * (throttle / 100) * track_factor

            data.append({
                "lap": lap,
                "time_step": t,
                "speed": speed,
                "throttle": throttle,
                "track_factor": track_factor
            })

    data = apply_pit_stop_effects(data, pit_stops)

    df = pd.DataFrame(data)
    df.to_csv("data/synthetic_telemetry.csv", index=False)

    print("\nPit Stop Events:", pit_stops)

    return df

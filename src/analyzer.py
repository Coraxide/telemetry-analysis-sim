def analyze_data(df):
    results = {}

    results["avg_lap_speed"] = df.groupby("lap")["speed"].mean()
    results["speed_variability"] = df.groupby("lap")["speed"].std()
    results["efficiency"] = df["speed"] / df["throttle"]

    pit_laps = df[df["is_pit_lap"] == 1]
    results["pit_lap_impact"] = pit_laps["speed"].mean() if len(pit_laps) > 0 else None

    results["driver_consistency_score"] = calculate_driver_consistency(df)

    return results
    
import numpy as np

def calculate_driver_consistency(df):
    
    speed_std = df["speed"].std()
    throttle_std = df["throttle"].std()

    lap_avg_speed = df.groupby("lap")["speed"].mean()
    lap_variation = lap_avg_speed.std()

    instability = speed_std + throttle_std + (lap_variation * 2)

    consistency_score = max(0, 100 - instability)

    return round(consistency_score, 2)

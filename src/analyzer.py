def analyze_data(df):
    results = {}

    # Average speed per lap
    lap_speeds = df.groupby("lap")["speed"].mean()
    results["avg_lap_speed"] = lap_speeds

    # Consistency (lower std = more consistent performance)
    results["speed_variability"] = df.groupby("lap")["speed"].std()

    # Detect performance drop
    results["performance_trend"] = lap_speeds.diff()

    # Efficiency metric (simple derived model)
    results["efficiency"] = df["speed"] / df["throttle"]

    return results

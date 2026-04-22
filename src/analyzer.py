def analyze_data(df):
    results = {}

    # Lap speed averages
    results["avg_lap_speed"] = df.groupby("lap")["speed"].mean()

    # Consistency
    results["speed_variability"] = df.groupby("lap")["speed"].std()

    # Efficiency
    results["efficiency"] = df["speed"] / df["throttle"]

    # PIT STOP ANALYSIS
    pit_laps = df[df["is_pit_lap"] == 1]
    results["pit_lap_impact"] = pit_laps["speed"].mean() if len(pit_laps) > 0 else None

    return results

import numpy as np

def generate_pit_stops(laps, pit_probability=0.3):
    """
    Generates pit stop events per lap.
    Returns dictionary: {lap_number: pit_duration_seconds}
    """

    pit_stops = {}

    for lap in range(1, laps + 1):
        if np.random.rand() < pit_probability:
            # pit stop between 12–28 seconds (realistic range)
            pit_duration = np.random.uniform(12, 28)
            pit_stops[lap] = round(pit_duration, 2)

    return pit_stops


def apply_pit_stop_effects(data, pit_stops):
    """
    Modifies telemetry data to reflect pit stop impact.
    """

    modified_data = []

    for row in data:
        lap = row["lap"]

        if lap in pit_stops:
            pit_penalty = pit_stops[lap]

            # simulate performance drop during pit cycle
            row["speed"] *= 0.55   # pit lane speed reduction
            row["pit_penalty"] = pit_penalty
            row["is_pit_lap"] = 1
        else:
            row["pit_penalty"] = 0
            row["is_pit_lap"] = 0

        modified_data.append(row)

    return modified_data

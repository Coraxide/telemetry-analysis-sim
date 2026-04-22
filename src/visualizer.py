import matplotlib.pyplot as plt
import os

def create_visualizations(df, results):

    os.makedirs("outputs/graphs", exist_ok=True)

    plt.figure()
    plt.plot(df["speed"][:500])
    plt.title("Telemetry Speed Over Time (Including Pit Strategy)")
    plt.xlabel("Time Step")
    plt.ylabel("Speed")
    plt.savefig("outputs/graphs/speed_over_time.png")
    plt.close()

    plt.figure()
    results["avg_lap_speed"].plot()
    plt.title("Lap Performance Trend")
    plt.xlabel("Lap")
    plt.ylabel("Avg Speed")
    plt.savefig("outputs/graphs/lap_performance.png")
    plt.close()

    plt.figure()
    df.groupby("lap")["is_pit_lap"].sum().plot(kind="bar")
    plt.title("Pit Stop Occurrence per Lap")
    plt.xlabel("Lap")
    plt.ylabel("Pit Events")
    plt.savefig("outputs/graphs/pit_stops.png")
    plt.close()

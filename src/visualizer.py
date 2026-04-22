import matplotlib.pyplot as plt
import os

def create_visualizations(df, results):

    os.makedirs("outputs/graphs", exist_ok=True)

    # SPEED OVER TIME
    plt.figure()
    plt.plot(df["speed"][:500])
    plt.title("Simulated Telemetry: Speed Over Time")
    plt.xlabel("Time Step")
    plt.ylabel("Speed")
    plt.savefig("outputs/graphs/speed_over_time.png")
    plt.close()

    # LAP PERFORMANCE
    plt.figure()
    results["avg_lap_speed"].plot(kind="line")
    plt.title("Average Speed per Lap (Performance Trend)")
    plt.xlabel("Lap")
    plt.ylabel("Avg Speed")
    plt.savefig("outputs/graphs/lap_performance.png")
    plt.close()

    # EFFICIENCY DISTRIBUTION
    plt.figure()
    plt.hist(results["efficiency"], bins=20)
    plt.title("Throttle Efficiency Distribution")
    plt.xlabel("Efficiency")
    plt.ylabel("Frequency")
    plt.savefig("outputs/graphs/efficiency_distribution.png")
    plt.close()

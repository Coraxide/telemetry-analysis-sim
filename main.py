from src.generator import generate_telemetry_data
from src.analyzer import analyze_data
from src.visualizer import create_visualizations

def main():
    print("\n[1] Generating synthetic telemetry data...")
    df = generate_telemetry_data()

    print("[2] Analyzing performance data...")
    results = analyze_data(df)

    print("[3] Creating visualizations...")
    create_visualizations(df, results)

    print("\nAnalysis complete. Outputs saved in /outputs directory.")

if __name__ == "__main__":
    main()

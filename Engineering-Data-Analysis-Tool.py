import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Data Generation / Simulation
# Demonstrating NumPy for engineering simulations
def generate_engineering_data():
    np.random.seed(42)
    time = np.linspace(0, 10, 100)
    # Simulating a decaying oscillation (common in mechanical engineering)
    signal = np.exp(-0.1 * time) * np.sin(2 * np.pi * time) + np.random.normal(0, 0.05, 100)
    return time, signal

# 2. Data Processing with Pandas
def process_data(time, signal):
    df = pd.DataFrame({'Time': time, 'Signal': signal})
    # Calculating a Rolling Average to smooth the noise
    df['SMA_5'] = df['Signal'].rolling(window=5).mean()
    # Identifying peaks (Anomalies)
    df['Anomaly'] = df['Signal'] > 0.8
    return df

# 3. Data Visualization with Matplotlib
def visualize_results(df):
    plt.figure(figsize=(10, 6))
    plt.plot(df['Time'], df['Signal'], label='Raw Engineering Signal', alpha=0.5, color='gray')
    plt.plot(df['Time'], df['SMA_5'], label='5-Point Moving Average', color='blue', linewidth=2)
    
    # Highlighting anomalies
    anomalies = df[df['Anomaly']]
    plt.scatter(anomalies['Time'], anomalies['Signal'], color='red', label='Peak Anomalies')

    plt.title('Engineering Signal Analysis: Decaying Oscillation', fontsize=14)
    plt.xlabel('Time (seconds)')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # Save the output for the GitHub README/LinkedIn Thumbnail
    plt.savefig('analysis_plot.png')
    plt.show()

if __name__ == "__main__":
    print("Starting Engineering Data Analysis...")
    t, s = generate_engineering_data()
    processed_df = process_data(t, s)
    
    print("\nFirst 5 rows of processed data:")
    print(processed_df.head())
    
    visualize_results(processed_df)
    print("\nAnalysis complete. Plot saved as 'analysis_plot.png'.")
import csv
import matplotlib.pyplot as plt

# Load heart rate data from CSV file
def load_heart_rate_data_from_csv(file_path):
    timestamps = []
    heart_rates = []
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row
        for row in reader:
            timestamps.append(row[0])
            heart_rates.append(int(row[1]))
    return timestamps, heart_rates

# Plot heart rate data
def plot_heart_rate_data(timestamps, heart_rates):
    plt.figure(figsize=(12, 6))
    plt.plot(timestamps, heart_rates, color='blue', linewidth=2)
    plt.xlabel('Timestamp', fontsize=12, labelpad=10)
    plt.ylabel('Heart Rate (BPM)', fontsize=12, labelpad=10)
    plt.title('Heart Rate Data for the Last 1 Hour', fontsize=14, fontweight='bold', pad=20)
    plt.xticks(rotation=45, ha='right', fontsize=10)
    plt.yticks(fontsize=10)
    plt.tick_params(axis='both', which='both', bottom=False, top=False, left=False, right=False)
    plt.grid(False)
    plt.show()

# Get file path of heart rate data CSV
file_path = 'heart_rate_data.csv'

# Load heart rate data from CSV
timestamps, heart_rates = load_heart_rate_data_from_csv(file_path)

# Plot heart rate data
plot_heart_rate_data(timestamps, heart_rates)

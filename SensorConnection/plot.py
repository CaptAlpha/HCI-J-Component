import csv
import matplotlib.pyplot as plt

def generate_heart_rate_plot(file_path):
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

    # Plot heart rate data and save as image file
    def plot_heart_rate_data(timestamps, heart_rates, file_path):
        plt.figure(figsize=(12, 6))
        plt.plot(timestamps, heart_rates, color='green', linewidth=2)
        plt.xlabel('Timestamp', fontsize=12, labelpad=10)
        plt.ylabel('Heart Rate (BPM)', fontsize=12, labelpad=10)
        plt.title('Heart Rate Data for the Last 1 Hour', fontsize=14, fontweight='bold', pad=20)
        plt.xticks(rotation=45, ha='right', fontsize=10)
        plt.yticks(fontsize=10)
        plt.tick_params(axis='both', which='both', bottom=False, top=False, left=False, right=False)
        plt.grid(False)

        # Identify heart rates that are too high (above 100 BPM) or too low (below 60 BPM)
        high_heart_rates = [hr if hr > 90 else None for hr in heart_rates]
        low_heart_rates = [hr if hr < 70 else None for hr in heart_rates]

        # Plot high heart rates in red
        plt.scatter(timestamps, high_heart_rates, color='red', marker='o', s=30, label='High HR (>100 BPM)')

        # Plot low heart rates in blue
        plt.scatter(timestamps, low_heart_rates, color='blue', marker='o', s=30, label='Low HR (<60 BPM)')

        plt.legend()

        # Save plot as image file
        plt.savefig(file_path, bbox_inches='tight')

        plt.close()

    # Load heart rate data from CSV
    timestamps, heart_rates = load_heart_rate_data_from_csv(file_path)

    # Plot heart rate data and save as image file
    plot_heart_rate_data(timestamps, heart_rates, 'heart_rate_plot.png')

    # Return path to the image file
    return 'heart_rate_plot.png'

file = 'heart_rate_data.csv'
generate_heart_rate_plot(file)

import random
import csv
from datetime import datetime, timedelta

# Function to generate simulated heart rate data, save it as a CSV file, and return the file path
def generate_heart_rate_data_csv():
    # Function to generate simulated heart rate data for a given timestamp
    def generate_heart_rate(timestamp):
        # Simulate heart rate data in beats per minute (BPM)
        heart_rate = random.randint(60, 100)  # Generate random heart rate between 60 and 100 BPM
        return heart_rate, timestamp

    # Get current timestamp
    current_timestamp = datetime.now()

    # Generate simulated heart rate data for the last 1 hour
    heart_rate_data = []  # List to store heart rate data
    for i in range(60):
        timestamp = current_timestamp - timedelta(minutes=i)  # Subtract i minutes from current timestamp
        heart_rate, timestamp = generate_heart_rate(timestamp)  # Generate heart rate for the timestamp
        heart_rate_data.append([timestamp.strftime('%Y-%m-%d %H:%M:%S'), heart_rate])  # Append timestamp and heart rate as a list

    # Save heart rate data as CSV
    filename = 'heart_rate_data.csv'
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Timestamp', 'Heart Rate'])  # Write header row
        writer.writerows(heart_rate_data)  # Write heart rate data rows

    return filename  # Return the file path where the heart rate data is saved

# Call the function and get the file path
file_path = generate_heart_rate_data_csv()
print(f"Heart rate data for the last 1 hour has been saved to '{file_path}'.")

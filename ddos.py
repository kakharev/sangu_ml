def read_log_file(log_file_path):
    with open(log_file_path, 'r') as file:
        log_data = file.readlines()
    return log_data


def extract_timestamps(log_data):
    timestamps = []
    for line in log_data:
        timestamp = line.split('[')[1].split(']')[0]
        timestamps.append(timestamp)
    return timestamps


def analyze_timestamps(timestamps):
    time_slots = {}
    for timestamp in timestamps:
        hour = timestamp.split(':')[1]
        if hour in time_slots:
            time_slots[hour] += 1
        else:
            time_slots[hour] = 1
    return time_slots


def identify_ddos_attack_time_slots(time_slots, threshold):
    attack_time_slots = []
    for hour, count in time_slots.items():
        if count > threshold:
            attack_time_slots.append(hour)
    return attack_time_slots


def main():
    log_file_path = 'logfile-attack.log'  # Path to your log file
    log_data = read_log_file(log_file_path)
    timestamps = extract_timestamps(log_data)
    time_slots = analyze_timestamps(timestamps)

    # Define a threshold for identifying DDoS attack time slots
    threshold = 100  # Adjust this threshold based on your analysis

    attack_time_slots = identify_ddos_attack_time_slots(time_slots, threshold)

    print("Potential DDoS Attack Time Slots:")
    for hour in attack_time_slots:
        print("Hour:", hour)


if __name__ == "__main__":
    main()

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


def calculate_regression(timestamps):
    # For the sake of demonstration, let's assume a simple linear regression model
    n = len(timestamps)
    sum_x = sum(range(1, n + 1))
    sum_y = sum([int(timestamp.split(':')[1]) for timestamp in timestamps])
    sum_xy = sum([(i + 1) * int(timestamp.split(':')[1]) for i, timestamp in enumerate(timestamps)])

    mean_x = sum_x / n
    mean_y = sum_y / n

    beta = (sum_xy - n * mean_x * mean_y) / (sum_x - n * mean_x ** 2)
    alpha = mean_y - beta * mean_x

    return alpha, beta


def main():
    log_file_path = 'logfile-attack.log'  # Path to your log file
    log_data = read_log_file(log_file_path)
    timestamps = extract_timestamps(log_data)
    time_slots = analyze_timestamps(timestamps)

    # Calculate regression (for demonstration purposes)
    alpha, beta = calculate_regression(timestamps)

    print("Statistical Analysis:")
    print("Total requests:", len(timestamps))
    print("Time slots distribution:", time_slots)
    print("Regression analysis - Alpha:", alpha, "Beta:", beta)


if __name__ == "__main__":
    main()

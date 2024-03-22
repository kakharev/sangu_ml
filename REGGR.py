import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
from tkinter import ttk
from collections import Counter

def read_log_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

def parse_log_data(log_data):
    ip_addresses = []
    timestamps = []
    methods = []
    urls = []
    protocols = []
    status_codes = []
    referers = []
    user_agents = []
    bytes_sent = []

    for log in log_data:
        parts = log.split(' ')
        ip_addresses.append(parts[0])
        timestamps.append(parts[3][1:] + ' ' + parts[4][:-1])
        methods.append(parts[5][1:])
        urls.append(parts[6])
        protocols.append(parts[7])
        status_codes.append(parts[8])
        referers.append(parts[10][1:-1])
        user_agents.append(' '.join(parts[12:-2]))
        bytes_sent.append(parts[-1])

    return {
        'IP Address': ip_addresses,
        'Timestamp': timestamps,
        'Method': methods,
        'URL': urls,
        'Protocol': protocols,
        'Status Code': status_codes,
        'Referer': referers,
        'User-Agent': user_agents,
        'Bytes Sent': bytes_sent
    }

def get_status_code_explanation(status_code):
    # Add explanations for status codes as needed
    status_code_explanations = {
        '200': 'OK',
        '301': 'Moved Permanently',
        '302': 'Found',
        '304': 'Not Modified',
        '400': 'Bad Request',
        '401': 'Unauthorized',
        '403': 'Forbidden',
        '404': 'Not Found',
        '500': 'Internal Server Error'
        # Add more status codes and explanations as needed
    }
    return status_code_explanations.get(status_code, 'Unknown')

def detect_potential_attacker(df, threshold=100):
    attacker_counts = Counter(df['IP Address'])
    potential_attackers = [ip for ip, count in attacker_counts.items() if count > threshold]
    return potential_attackers

def upload_file():
    file_path = filedialog.askopenfilename(filetypes=[("log ფაილი", "*.log")])
    if file_path:
        log_data = read_log_file(file_path)
        parsed_data = parse_log_data(log_data)
        df = pd.DataFrame(parsed_data)
        df['Status Explanation'] = df['Status Code'].apply(get_status_code_explanation)
        display_data(df)
        display_most_used_ip(df)
        display_potential_attackers(df)

def export_to_csv(df):
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if file_path:
        df.to_csv(file_path, index=False)
        messagebox.showinfo("Export Successful", "Log data exported to CSV successfully.")

def display_data(df):
    for widget in frame.winfo_children():
        widget.destroy()

    tree = ttk.Treeview(frame)
    tree["columns"] = list(df.columns)
    tree["show"] = "headings"

    for column in df.columns:
        tree.heading(column, text=column)

    for index, row in df.iterrows():
        tree.insert("", "end", values=list(row))

    tree.pack(fill="both", expand=True)

    export_button = tk.Button(frame, text="Export to CSV", command=lambda: export_to_csv(df))
    export_button.pack(pady=5)

def display_most_used_ip(df):
    most_common_ip = Counter(df['IP Address']).most_common(1)
    if most_common_ip:
        messagebox.showinfo("Most Used IP Address", f"The most used IP address is: {most_common_ip[0][0]}")
    else:
        messagebox.showinfo("Most Used IP Address", "No data available")

def display_potential_attackers(df):
    potential_attackers = detect_potential_attacker(df)
    if potential_attackers:
        messagebox.showinfo("Potential Attackers", f"Potential attackers detected: {', '.join(potential_attackers)}")
    else:
        messagebox.showinfo("Potential Attackers", "No potential attackers detected.")

root = tk.Tk()
root.title("Log File Parser")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

upload_button = tk.Button(frame, text="მჭირდება ლოგ ფაილი", command=upload_file)
upload_button.pack(pady=5)

root.mainloop()

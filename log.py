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
    }
    return status_code_explanations.get(status_code, 'Unknown')


def upload_file():
    file_path = filedialog.askopenfilename(filetypes=[("log ფაილი", "*.log")])
    if file_path:
        log_data = read_log_file(file_path)
        parsed_data = parse_log_data(log_data)
        df = pd.DataFrame(parsed_data)
        df['Status Explanation'] = df['Status Code'].apply(get_status_code_explanation)
        display_data(df)
        display_most_used_ip(df)
        display_most_grouped(df)
        display_most_continuous_ip(df)
        display_regression_graph(df)
        display_unique_ip_addresses(df)


def export_to_csv(df):
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if file_path:
        df.to_csv(file_path, index=False)
        messagebox.showinfo("ექსპორტი დასრულდა", "ფაილი წარმატებით დაექსპორტდა.")


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

    export_button = tk.Button(frame, text="შევინახოთ CSV", command=lambda: export_to_csv(df))
    export_button.pack(pady=5)


def display_most_used_ip(df):
    most_common_ip = Counter(df['IP Address']).most_common(1)
    if most_common_ip:
        messagebox.showinfo("განმეორებადი მისამართია", f"The most used IP address is: {most_common_ip[0][0]}")
    else:
        messagebox.showinfo("განმეორებადი მისამართი", "No data available")


def display_most_grouped(df):
    most_grouped_timestamp = Counter(df['Timestamp']).most_common(1)
    most_grouped_ip = Counter(df['IP Address']).most_common(1)
    messagebox.showinfo("Most Grouped Data", f"The most grouped timestamp is: {most_grouped_timestamp[0][0]}\n"
                                             f"The most grouped IP address is: {most_grouped_ip[0][0]}")


def display_most_continuous_ip(df):
    ip_counter = Counter(df['IP Address'])
    max_count = max(ip_counter.values())
    most_continuous_ips = [ip for ip, count in ip_counter.items() if count == max_count]
    messagebox.showinfo("ეს რაღაცას მაიმუნობს აშკარად!!!",
                        f"The most continuous IP address(es) is/are: {', '.join(most_continuous_ips)}")


def display_regression_graph(df):
    # Add regression graph display code here
    pass


def display_unique_ip_addresses(df):
    unique_ips = list(set(df['IP Address']))
    unique_ips_window = tk.Toplevel()
    unique_ips_window.title("Unique IP Addresses")

    # Frame to hold the listbox and scrollbar
    frame = tk.Frame(unique_ips_window)
    frame.pack(padx=10, pady=10)

    # Listbox to display unique IP addresses
    listbox = tk.Listbox(frame, width=40, height=10)
    listbox.pack(side="left", fill="y")

    # Scrollbar
    scrollbar = tk.Scrollbar(frame, orient="vertical", command=listbox.yview)
    scrollbar.pack(side="right", fill="y")

    listbox.config(yscrollcommand=scrollbar.set)

    # Insert unique IP addresses into the listbox
    for ip in unique_ips:
        listbox.insert("end", ip)


root = tk.Tk()
root.title("Log File Parser")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

upload_button = tk.Button(frame, text="მჭირდება ლოგ ფაილი", command=upload_file)
upload_button.pack(pady=5)

root.mainloop()

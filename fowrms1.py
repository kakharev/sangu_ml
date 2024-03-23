import tkinter as tk

def submit():
    name = name_entry.get()
    surname = surname_entry.get()
    output_text.set(f"Name: {name}\nSurname: {surname}")

# Create main window
root = tk.Tk()
root.title("Name and Surname Form")

# Create labels
name_label = tk.Label(root, text="Name:")
surname_label = tk.Label(root, text="Surname:")

# Create entry fields
name_entry = tk.Entry(root)
surname_entry = tk.Entry(root)

# Create submit button
submit_button = tk.Button(root, text="Submit", command=submit)

# Create text area for output
output_text = tk.StringVar()
output_area = tk.Label(root, textvariable=output_text, justify="left")

# Positioning widgets
name_label.grid(row=0, column=0, padx=10, pady=5)
name_entry.grid(row=0, column=1, padx=10, pady=5)
surname_label.grid(row=1, column=0, padx=10, pady=5)
surname_entry.grid(row=1, column=1, padx=10, pady=5)
submit_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5)
output_area.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

# Start the GUI event loop
root.mainloop()

import tkinter as tk


def button_click(value):
    entry.insert(tk.END, value)


def clear():
    entry.delete(0, tk.END)


def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")


root = tk.Tk()
root.title("კალკულატორი")

entry = tk.Entry(root, width=30)
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row = 1
col = 0

for button in buttons:
    if button == '=':
        tk.Button(root, text=button, command=calculate).grid(row=row, column=col)
    elif button == '0':
        tk.Button(root, text=button, command=lambda b=button: button_click(b), width=15).grid(row=row + 4, column=col,
                                                                                              columnspan=2)
        col += 1
    else:
        tk.Button(root, text=button, command=lambda b=button: button_click(b)).grid(row=row + int((row - 1) / 3),
                                                                                    column=col)

    col += 1

    if col > 3:
        col = 0
        row += 1

clear_button = tk.Button(root, text="გასუფთავება", command=clear)
clear_button.grid(row=row + 1, column=0, columnspan=4, pady=5)

root.mainloop()

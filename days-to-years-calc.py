import tkinter as tk
from tkinter import messagebox

def calculate_reverse():
    try:
        days = int(days_entry.get())

        if days < 0:
            raise ValueError

        weeks = round(days / 7, 2)
        months = round(days / 30.44, 2)
        years = round(days / 365.25, 2)

        result = (
            f"Total Days: {days}\n"
            f"Weeks: {weeks}\n"
            f"Months: {months}\n"
            f"Years: {years}"
        )

        messagebox.showinfo("Results", result)

    except ValueError:
        messagebox.showerror("Error", "Enter only integer")

# ---------------- GUI ----------------
root = tk.Tk()
root.title("Days To Years Converter")
root.geometry("300x180")
root.resizable(False, False)

tk.Label(root, text="Enter Total Days", font=("Cascadia Code", 10)).pack(pady=10)
days_entry = tk.Entry(root, width=25, font=("Cascadia Code", 9))
days_entry.pack(pady=5)

tk.Button(root, text="Convert", width=15, command=calculate_reverse).pack(pady=15)

root.mainloop()

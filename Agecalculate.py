import tkinter as tk
from tkinter import messagebox
from datetime import date

def calculate_age_gui():
    try:
        birth_day = int(day_entry.get())
        birth_month = int(month_entry.get())
        birth_year = int(year_entry.get())

        birth_date = date(birth_year, birth_month, birth_day)
        current_date = date.today()

        if birth_date > current_date:
            messagebox.showerror("Error", "Please enter a valid date of birth.")
            return

        years = current_date.year - birth_date.year
        months = current_date.month - birth_date.month
        days = current_date.day - birth_date.day

        if days < 0:
            months -= 1
            days += get_days_in_month(birth_date.month, birth_date.year)
        if months < 0:
            years -= 1
            months += 12

        # Create output frame dynamically after calculation
        global output_frame, result_label
        if 'output_frame' in globals():
            output_frame.destroy()  # Remove previous output if exists

        output_frame = tk.Frame(root, bg="#F0F8FF", bd=3, relief="groove", padx=20, pady=20)
        output_frame.pack(pady=10)

        result_text = f"Your age is {years} years, {months} months, {days} days."
        result_label = tk.Label(output_frame, text=result_text, bg="#F0F8FF", font=("Arial", 16, "bold"), fg="#333")
        result_label.pack()

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")


def get_days_in_month(month, year):
    if month == 2:
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            return 29
        else:
            return 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31


# Hover effects for button
def on_enter(e):
    calculate_button['background'] = '#4CAF50'  # Green
    calculate_button['foreground'] = 'white'


def on_leave(e):
    calculate_button['background'] = '#90EE90'  # Light Green
    calculate_button['foreground'] = 'black'


# Tkinter GUI
root = tk.Tk()
root.title("Age Calculator")
root.geometry("450x300")
root.configure(bg="white")
root.resizable(False, False)

tk.Label(root, text="Enter your Date of Birth", bg="white", font=("Arial", 14, "bold")).pack(pady=10)

frame = tk.Frame(root, bg="white")
frame.pack(pady=5)

tk.Label(frame, text="Day", bg="white").grid(row=0, column=0, padx=5)
tk.Label(frame, text="Month", bg="white").grid(row=0, column=1, padx=5)
tk.Label(frame, text="Year", bg="white").grid(row=0, column=2, padx=5)

day_entry = tk.Entry(frame, width=5)
day_entry.grid(row=1, column=0)
month_entry = tk.Entry(frame, width=5)
month_entry.grid(row=1, column=1)
year_entry = tk.Entry(frame, width=7)
year_entry.grid(row=1, column=2)

calculate_button = tk.Button(root, text="Calculate Age", bg="#90EE90", font=("Arial", 12, "bold"), relief="raised",
                             padx=10, pady=5, command=calculate_age_gui)
calculate_button.pack(pady=15)

# Bind hover events
calculate_button.bind("<Enter>", on_enter)
calculate_button.bind("<Leave>", on_leave)

root.mainloop()

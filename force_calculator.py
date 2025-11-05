"""
Force Calculator App
--------------------
A Python GUI tool to estimate the force exerted by an object in a vehicle
based on torque increase and speed decrease.
Created by Harsh | 2025
"""

import tkinter as tk
from tkinter import messagebox

def calculate_force():
    try:
        speed_no_load = float(entry_speed_no_load.get())
        speed_load = float(entry_speed_load.get())
        torque_increase = float(entry_torque.get())
        radius = float(entry_radius.get())

        if speed_load == 0 or radius == 0:
            raise ValueError("Speed and radius must be non-zero!")

        force = (torque_increase / radius) * (speed_no_load / speed_load)
        label_result.config(text=f"Estimated Force: {force:.2f} N")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values.")

# GUI setup
root = tk.Tk()
root.title("Force Calculator")
root.geometry("350x320")
root.resizable(False, False)
root.configure(bg="#101820")

title_label = tk.Label(root, text="Force Calculator", font=("Arial", 16, "bold"), bg="#101820", fg="#FEE715")
title_label.pack(pady=10)

frame = tk.Frame(root, bg="#101820")
frame.pack(pady=5)

labels = ["Speed (no load)", "Speed (with load)", "Torque Increase (Nm)", "Wheel Radius (m)"]
entries = []

for i, text in enumerate(labels):
    lbl = tk.Label(frame, text=text + ":", font=("Arial", 10), bg="#101820", fg="white")
    lbl.grid(row=i, column=0, padx=10, pady=6, sticky="e")
    entry = tk.Entry(frame, font=("Arial", 10), width=15)
    entry.grid(row=i, column=1, padx=10, pady=6)
    entries.append(entry)

entry_speed_no_load, entry_speed_load, entry_torque, entry_radius = entries

btn_calc = tk.Button(root, text="Calculate Force", command=calculate_force, bg="#FEE715", fg="black", font=("Arial", 11, "bold"), width=20)
btn_calc.pack(pady=10)

label_result = tk.Label(root, text="Estimated Force: -- N", font=("Arial", 12), bg="#101820", fg="white")
label_result.pack(pady=10)

footer = tk.Label(root, text="Made by Harsh ⚙️", font=("Arial", 9), bg="#101820", fg="gray")
footer.pack(side="bottom", pady=5)

root.mainloop()

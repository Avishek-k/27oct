"""A simple digital clock built with Python's standard-library Tkinter."""

import tkinter as tk
from time import strftime


def update_clock() -> None:
    """Refresh the displayed time and schedule the next update."""
    time_label.config(text=strftime("%I:%M:%S %p"))
    date_label.config(text=strftime("%A, %B %d, %Y"))
    root.after(1000, update_clock)


root = tk.Tk()
root.title("Digital Clock")
root.configure(bg="#1e1e2e")
root.resizable(False, False)

time_label = tk.Label(
    root,
    font=("Segoe UI", 48, "bold"),
    bg="#1e1e2e",
    fg="#cdd6f4",
    padx=30,
    pady=(24, 4),
)
time_label.pack()

date_label = tk.Label(
    root,
    font=("Segoe UI", 16),
    bg="#1e1e2e",
    fg="#a6adc8",
    padx=30,
    pady=(0, 24),
)
date_label.pack()

update_clock()
root.mainloop()
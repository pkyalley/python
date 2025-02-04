import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("My Second App")
window.geometry("400x400")

frame = tk.Frame(window, background="lightgrey")
frame.pack(padx=10, pady=10)

label = tk.Label(frame, text="Select an option:")
label.pack(pady=5)

combo = ttk.Combobox(frame, values=["Option1", "Option 2", "Option 3"])
combo.pack(pady=5)

def clicked():
    print(combo.get())

button = tk.Button(frame, text="click", command=clicked)
button.pack(pady=5)

window.mainloop()
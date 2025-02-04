# windows, buttons, labels, other widgets


import tkinter as tk

window = tk.Tk()                #Parent Container for the app
window.title("My First App")
window.geometry("400x400")

frame = tk.Frame(window, background="lightblue")
frame.pack(padx=20, pady=20, fill="both", expand=True)

label = tk.Label(frame, text="Hello",
                 font=("Arial", 24),
                 background="Orange")
label.grid(row=1, column=0, padx=10, pady=10)                #Placing the label inside the created container for the app

def on_button_click():
    name = user_input.get()
    label.config(text=f"Welcome {name}!")

user_input = tk.Entry(frame, font=("Arial", 12))
user_input.grid(row=0, column=0, padx=10, pady=10)

button = tk.Button(frame, text="Click Here",
                   command= on_button_click,
                   font=("Arial", 12))
button.grid(row=0, column=1, padx=10, pady=10)

window.mainloop()
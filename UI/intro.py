import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Hello World")
window.geometry("400x300")

frame = ttk.Frame(window, padding='10 10 10 10')
frame.pack(fill='both', expand=True)

def click_button1():
    window.title("Button Clicked!")
    name = name_text.get()
    label_text.set(f"{name} says Hello!")

def click_button2():
    window.destroy()


name_label = ttk.Label(frame, text="Name")
name_label.grid(column=0, row=0, sticky=tk.E)
#name_label.pack()

name_text = tk.StringVar()
name_entry = ttk.Entry(frame, width=25, textvariable=name_text)
name_entry.grid(column=1, row=0)
#name_entry.pack()

label = ttk.Label(frame, text="?")
label.grid(column=0, row=1, sticky=tk.E)
#label.pack()

label_text = tk.StringVar()
label_entry = ttk.Entry(frame, width=25, textvariable=label_text, state='readonly')
label_entry.grid(column=1, row=1)
#label_entry.pack()

button1 = ttk.Button(frame, text="Hello!", command=click_button1)
button1.grid(column=0, row=2)
button2 = ttk.Button(frame, text="Bye!", command=click_button2)
button2.grid(column=1, row=2)
#button1.pack()
#button2.pack()


for child in frame.winfo_children():
    child.grid_configure(padx=5, pady=5)

window.mainloop()
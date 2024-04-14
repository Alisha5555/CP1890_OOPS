import tkinter as tk
from tkinter import ttk
import Question_6_database as Q6

window = tk.Tk()
window.title("Edit Sales Amount")
window.geometry("350x200")

frame = ttk.Frame(window, padding="10 10 10 10")
frame.pack(fill="both", expand=True)


def button_1():
    date = date_entry.get()
    region = region_entry.get()
    Q6.get_data(conn, region, date)



def button_2():
    print("place holder")


def button_3():
    window.destroy()


conn = Q6.connect()

name_label = ttk.Label(frame, text="Enter date and region to get sales amount.")
name_label.grid(column=0, columnspan=3, row=0)

date_label = ttk.Label(frame, text="Date:")
date_label.grid(column=0, row=1, sticky=tk.E)
date_text = tk.StringVar()
date_entry = ttk.Entry(frame, width=25, textvariable=date_text)
date_entry.grid(column=1, row=1)

region_label = ttk.Label(frame, text="Region:")
region_label.grid(column=0, row=2, sticky=tk.E)
region_text = tk.StringVar()
region_entry = ttk.Entry(frame, width=25, textvariable=region_text)
region_entry.grid(column=1, row=2)

amount_label = ttk.Label(frame, text="Amount:")
amount_label.grid(column=0, row=3, sticky=tk.E)
amount_text = tk.StringVar()
amount_entry = ttk.Entry(frame, width=25, textvariable=amount_text)
amount_entry.grid(column=1, row=3)

ID_label = ttk.Label(frame, text="ID:")
ID_label.grid(column=0, row=4, sticky=tk.E)
ID_text = tk.StringVar()
ID_entry = ttk.Entry(frame, width=25, textvariable=ID_text, state='readonly')
ID_entry.grid(column=1, row=4)

button1 = ttk.Button(frame, text="Get Amount", command=button_1)
button1.grid(column=2, row=2)

button2 = ttk.Button(frame, text="Save Changes", command=button_2)
button2.grid(column=1, row=5, sticky=tk.W)

button3 = ttk.Button(frame, text="Exit", command=button_3)
button3.grid(column=1, row=5, sticky=tk.E)

for child in frame.winfo_children():
    child.grid_configure(padx=5, pady=3)

window.mainloop()

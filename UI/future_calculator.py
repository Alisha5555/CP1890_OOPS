import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Future Value Calculator")
window.geometry("400x300")

frame = ttk.Frame(window, padding='10 10 10 10')
frame.pack(fill='both', expand=True)

def click_button1():
    print("Click Button1")
def click_button2():
    window.destroy()

month_label = ttk.Label(frame, text="Monthly Investment:")
month_label.grid(column=0, row=0, sticky=tk.E)


month_text = tk.IntVar()
month_entry = ttk.Entry(frame, width=40, textvariable=month_text)
month_entry.grid(column=1, row=0)


yearly_label = ttk.Label(frame, text="Yearly Interest Rate:")
yearly_label.grid(column=0, row=1, sticky=tk.E)


yearly_text = tk.IntVar()
yearly_entry = ttk.Entry(frame, width=40, textvariable=yearly_text)
yearly_entry.grid(column=1, row=1)


years_label = ttk.Label(frame, text="Years:")
years_label.grid(column=0, row=2, sticky=tk.E)


years_text = tk.IntVar()
years_entry = ttk.Entry(frame, width=40, textvariable=years_text)
years_entry.grid(column=1, row=2)

FValue_label = ttk.Label(frame, text="Future Value:")
FValue_label.grid(column=0, row=3, sticky=tk.E)

FValue_text = tk.StringVar()
FValue_entry = ttk.Entry(frame, width=40, textvariable=FValue_text, state='readonly')
FValue_entry.grid(column=1, row=3)


button1 = ttk.Button(frame, text="Calculate", command=click_button1)
button1.grid(column=0, row=4)
button2 = ttk.Button(frame, text="Exit", command=click_button2)
button2.grid(column=1, row=4)



for child in frame.winfo_children():
    child.grid_configure(padx=5, pady=5)

window.mainloop()
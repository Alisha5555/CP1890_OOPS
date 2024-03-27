import tkinter as tk
from tkinter import ttk, messagebox

window = tk.Tk()
window.title("Player")
window.geometry("500x300")

frame = ttk.Frame(window,padding='10 10 10 10')
frame.pack(fill='both', expand=True)

def click_button1():
    print('save')
def click_button2():
    window.destroy()
def click_button3():
    print('player')

player_label = ttk.Label(frame, text="Player ID:")
player_label.grid(row=0, column=0, sticky=tk.E)

player_text = tk.IntVar()
player_entry = ttk.Entry(frame, width=40, textvariable=player_text)
player_entry.grid(column=1, row=0)

first_label = ttk.Label(frame, text="First Name:")
first_label.grid(row=1, column=0, sticky=tk.E)

first_text = tk.StringVar()
first_entry = tk.Entry(frame, width=40, textvariable=first_text)
first_entry.grid(column=1, row=1)

last_label = ttk.Label(frame, text="Last Name:")
last_label.grid(row=2, column=0, sticky=tk.E)

last_text = tk.StringVar()
last_entry = tk.Entry(frame, width=40, textvariable=last_text)
last_entry.grid(column=1, row=2)

position_label = ttk.Label(frame, text="Position:")
position_label.grid(row=3, column=0, sticky=tk.E)

position_text = tk.StringVar()
position_entry = ttk.Entry(frame, width=40, textvariable=position_text)
position_entry.grid(row=3, column=1)

bats_label = ttk.Label(frame, text="At bats:")
bats_label.grid(row=4, column=0, sticky=tk.E)

bats_text = tk.IntVar()
bats_entry = ttk.Entry(frame, width=40, textvariable=bats_text)
bats_entry.grid(row=4, column=1)

hits_label = ttk.Label(frame, text="Hits:")
hits_label.grid(row=5, column=0, sticky=tk.E)

hits_text = tk.IntVar()
hits_entry = ttk.Entry(frame, width=40, textvariable=hits_text)
hits_entry.grid(row=5, column=1)

battingAvg_label = ttk.Label(frame, text="Batting Avg:")
battingAvg_label.grid(row=6, column=0)

battingAvg_text = tk.IntVar()
battingAvg_entry = ttk.Entry(frame, width=40, textvariable=battingAvg_text)
battingAvg_entry.grid(row=6,column=1)


button1 = ttk.Button(frame, text="Save Changes", command=click_button1)
button1.grid(column=0, row=7)

button2 = ttk.Button(frame, text="Cancel", command=click_button2)
button2.grid(column=1, row=7)

button3 = ttk.Button(frame, text="Get Player", command=click_button3)
button3.grid(column=2, row=0)



for child in frame.winfo_children():
    child.grid_configure(padx=5, pady=5)

window.mainloop()


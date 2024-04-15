import tkinter as tk
from tkinter import ttk
import math


class pythagorean():
    def __init__(self):
        self.sideA = 0
        self.sideB = 0

    def calculate_hypotaneuse(self):
        # c^2 (hypotaneuse) is a^2 + b^2.
        squared = self.sideA ** 2 + self.sideB ** 2
        # taking square root of c^2 to have just c.
        sideC = math.sqrt(squared)
        return sideC

class pythag_frame(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")
        self.parent = parent
        self.pythagorean = pythagorean()

        self.sideA = tk.StringVar()
        self.sideB = tk.StringVar()
        self.sideC = tk.StringVar()

        self.initComponents()

    def initComponents(self):
        self.pack()
        # Creating Side A, Side B, and Side C labels, and text entry fields for Side A and Side B.
        ttk.Label(self, text="Side A:").grid(column=0, row=0, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.sideA).grid(column=1, row=0)

        ttk.Label(self, text="Side B:").grid(column=0, row=1, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.sideB).grid(column=1, row=1)

        ttk.Label(self, text="Side C:").grid(column=0, row=2, sticky=tk.E)
        # Assigning Side C state "readonly" so that calculation appears here instead of accepting text entry.
        ttk.Entry(self, width=25, textvariable=self.sideC, state="readonly").grid(column=1, row=2)

        self.makebuttons()

        # Assigning size to each cell in grid
        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=3)

    def makebuttons(self):
        buttonFrame = ttk.Frame(self)
        buttonFrame.grid(column=0, row=3, columnspan=2, sticky=tk.E)

        # Creating buttons 'Calculate' and 'Exit'. Button 'Exit' closing program when clicked.
        ttk.Button(buttonFrame, text="Calculate", command=self.calculate).grid(column=0, row=0, padx=5)
        ttk.Button(buttonFrame, text="Exit", command=self.parent.destroy).grid(column=1, row=0)

    def calculate(self):
        self.pythagorean.sideA = int(self.sideA.get())
        self.pythagorean.sideB = int(self.sideB.get())
        self.sideC.set(self.pythagorean.calculate_hypotaneuse())
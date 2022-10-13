from tkinter import ttk
from tkinter import *

import sqlite3

class Product:
    def __init__(self, window):
        self.wind = window
        self.wind.title("Products Applications")
        # self.window.geometry("1000x700")
        # self.window.resizable(0, 0)
        # self.window.configure(bg = "black")
  
        #creating a FRame Container
        frame = LabelFrame(self.wind, text = "Register A new Product")
        frame.grid(row = 0, column = 0, columnspan= 3, pady = 20)

        #name inputer
        Label(frame, text="Product Name:").grid(row = 1, column= 0)
        self.name = Entry(frame)
        self.name.grid(row = 1, column = 1)


if __name__ == '__main__':
    window = Tk()
    application = Product(window)
    window.mainloop()





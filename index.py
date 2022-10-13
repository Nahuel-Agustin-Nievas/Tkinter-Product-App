from tkinter import ttk
from tkinter import *

import sqlite3

class Product:
     
    db_name="database.db"

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
        self.name.focus()   # focus on the labelFrame
        self.name.grid(row = 1, column = 1)

        #price inputer
        Label(frame, text="Product Price:").grid(row = 2, column = 0)
        self.price = Entry(frame)
        self.price.grid(row = 2, column = 1)


        #button add product
        ttk.Button(frame, text="Save Product").grid(row = 3, columnspan = 2, sticky= W + E)

        #create table
        self.tree = ttk.Treeview(height=10, column= 2)
        self.tree.grid(row = 4, column = 0, columnspan = 2)
        self.tree.heading("#0", text="Name", anchor=CENTER)
        self.tree.heading("#1", text="Price", anchor=CENTER)


        self.get_products()

    def run_query(self, query, parameters =()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result= cursor.execute(query, parameters)
            conn.commit()   
            # data = cursor.fetchall()
        return result

    def get_products(self):
        #cleaning table
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        #quering database
        query= "SELECT * FROM product ORDER BY name DESC"
        db_rows = self.run_query(query)
        for row in db_rows:
            self.tree.insert("", 0, text=row[1], values= row[2])

if __name__ == '__main__':
    window = Tk()
    application = Product(window)
    window.mainloop()





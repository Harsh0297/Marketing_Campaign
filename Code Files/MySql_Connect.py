from tkinter import * 
from tkinter import messagebox
from sqlalchemy import create_engine
import pymysql
import pandas as pd 
import mysql.connector as msql
import mysql.connector
from mysql.connector import Error


file_name1="Data Files\Merged_Fact_Dim.xlsx"


raw_df1=pd.read_excel(file_name1)


_con=None
win = Tk()

def input_function():
    global _con  # Set the '_con' as a global variable
    username_input = username_entry.get()
    password_input = password_entry.get()
    localhost_input=localhost_entry.get()
    database_input=database_entry.get()
    tablename_input=tablename_entry.get()
    conn_str = 'mysql+pymysql://{}:{}@{}/{}'.format(username_input, password_input, localhost_input, database_input)
    _con = create_engine(conn_str)
    try:
        if _con is not None:
            raw_df1.to_sql(tablename_input, con=_con, if_exists='replace')  # Execute to_sql() if the connection is established
            messagebox.showinfo("Connection Status", "Connection successful!")
            messagebox.showinfo("Loading", "Data Loading")
            
            
            
        else:
            print("Connection not established.")
            messagebox.showinfo("Connection Status", "Connection not successful!")
        messagebox.showinfo("Done", "Data Loading Successful Done")
       
    except Exception as error: 
        messagebox.showinfo("Connection Status", "Connection not successful! \nCheck your usename and password")
   

 

sql_label=Label(win,text="SQL Label",font=("Monotype Corsiva" ,35,  "bold"))
sql_label.grid(row=0, column=1, padx=10, pady=10,sticky="n")

# Create the Entry widget
username_entry = Entry(win, font=("Times New Roman" ,15,  "italic"))
username_entry.grid(row=1, column=2, padx=10, pady=10, sticky="e")# Place it in the first row, first column, sticky="w" for left alignment

# # Create the Entry widget
password_entry = Entry(win, font=("Times New Roman" ,15,  "italic"))
password_entry.grid(row=2, column=2, padx=10, pady=10, sticky="e")  # Place it in the first row, first column, sticky="w" for left alignment

# # Create the Entry widget
localhost_entry = Entry(win, font=("Times New Roman" ,15,  "italic"))
localhost_entry.grid(row=3, column=2, padx=10, pady=10, sticky="e")  # Place it in the first row, first column, sticky="w" for left alignment

# # Create the Entry widget
database_entry = Entry(win, font=("Times New Roman" ,15,  "italic"))
database_entry.grid(row=4, column=2, padx=10, pady=10, sticky="e")  # Place it in the first row, first column, sticky="w" for left alignment

# # Create the Entry widget
tablename_entry = Entry(win, font=("Times New Roman" ,15,  "italic"))
tablename_entry.grid(row=5, column=2, padx=10, pady=10, sticky="e")  # Place it in the first row, first column, sticky="w" for left alignment


# Create the Label widget
username_label = Label(win, text="username", font=("Times New Roman" ,15,  "italic"))
username_label.grid(row=1, column=1, padx=10, pady=10, sticky="w")


# Create the Label widget
password_label = Label(win, text="password", font=("Times New Roman" ,15,  "italic"))
password_label.grid(row=2, column=1, padx=10, pady=10, sticky="w")  # Place it in the first row, second column, sticky="w" for left alignment


# Create the Label widget
localhost_label = Label(win, text="host", font=("Times New Roman" ,15,  "italic"))
localhost_label.grid(row=3, column=1, padx=10, pady=10, sticky="w")  # Place it in the first row, second column, sticky="w" for left alignment

database_label = Label(win, text="database", font=("Times New Roman" ,15,  "italic"))
database_label.grid(row=4, column=1, padx=10, pady=10, sticky="w")  # Place it in the first row, second column, sticky="w" for left alignment

# Create the Label widget
tablename_label = Label(win, text="Table Name", font=("Times New Roman" ,15,  "italic"))
tablename_label.grid(row=5, column=1, padx=10, pady=10, sticky="w")  # Place it in the first row, second column, sticky="w" for left alignment




okay_button = Button(win, text="Connect", command=input_function)  # Remove the parentheses from input_function
okay_button.grid(row=6, column=1, padx=10, pady=10, sticky="s")

okay_button = Button(win, text="Close", command=win.quit)  # Remove the parentheses from input_function
okay_button.grid(row=6, column=2, padx=10, pady=10, sticky="s")


win.mainloop()
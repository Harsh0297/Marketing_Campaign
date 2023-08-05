from tkinter import *
from tkinter import messagebox
from sqlalchemy import create_engine
import pandas as pd
from Visuals_Helper_Function import Label_Function,Label_Widget,Entry_Widget,button_function,close_button,sql_connect


raw_df1 = pd.read_excel("Data Files\Merged_Fact_Dim.xlsx")

win = Tk()

Label_Function(win, "SQL Label", "Monotype Corsiva", 35, "bold")

username_entry = Entry_Widget(win, "Times New Roman", 15, "italic", 1, 2, 10, 10, "e")
password_entry = Entry_Widget(win, "Times New Roman", 15, "italic", 2, 2, 10, 10, "e")
localhost_entry = Entry_Widget(win, "Times New Roman", 15, "italic", 3, 2, 10, 10, "e")
database_entry = Entry_Widget(win, "Times New Roman", 15, "italic", 4, 2, 10, 10, "e")
table_name_entry = Entry_Widget(win, "Times New Roman", 15, "italic", 5, 2, 10, 10, "e")

username_label = Label_Widget(win, "username", "Times New Roman", 15, "italic", 1, 1, 10, 10, "w")
password_label = Label_Widget(win, "password", "Times New Roman", 15, "italic", 2, 1, 10, 10, "w")
localhost_label = Label_Widget(win, "local host", "Times New Roman", 15, "italic", 3, 1, 10, 10, "w")
database_label = Label_Widget(win, "Database Name", "Times New Roman", 15, "italic", 4, 1, 10, 10, "w")
table_name_label = Label_Widget(win, "Table Name", "Times New Roman", 15, "italic", 5, 1, 10, 10, "w")


def connect_button_click():
    username = username_entry.get()
    password = password_entry.get()
    localhost = localhost_entry.get()
    database = database_entry.get()
    tablename = table_name_entry.get()
    sql_connect(raw_df1, username, password, localhost, database, tablename)


button_function(win, "Connect", connect_button_click, 6, 1, 10, 10, "s")
close_button(win, 6, 2, 10, 10, "s")

win.mainloop()

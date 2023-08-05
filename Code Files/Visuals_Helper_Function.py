from tkinter import * 
from tkinter import messagebox
from sqlalchemy import create_engine
import pymysql
import mysql.connector as msql
import mysql.connector
from mysql.connector import Error

def Label_Function(_win, _text, _Font_Type, _Font_Size, _typographical):
    sql_label = Label(_win, text=_text, font=(_Font_Type, _Font_Size, _typographical))
    sql_label.grid(row=0, column=1, padx=10, pady=10, sticky="n")


def Entry_Widget(_win, _Font_Type, _Font_Size, _typographical, _row, _column, _padx, _pady, _side):
    _entry_widget = Entry(_win, font=(_Font_Type, _Font_Size, _typographical))
    _entry_widget.grid(row=_row, column=_column, padx=_padx, pady=_pady, sticky=_side)
    return _entry_widget


def Label_Widget(_win, _label_name, _Font_Type, _Font_Size, _typographical, _row, _column, _padx, _pady, _side):
    _label_widget = Label(_win, text=_label_name, font=(_Font_Type, _Font_Size, _typographical))
    _label_widget.grid(row=_row, column=_column, padx=_padx, pady=_pady, sticky=_side)
    return _label_widget


def button_function(_win, _button_name, _command, _row, _column, _padx, _pady, _side):
    okay_button = Button(_win, text=_button_name, command=_command)
    okay_button.grid(row=_row, column=_column, padx=_padx, pady=_pady, sticky=_side)
    return okay_button


def close_button(_win, _row, _column, _padx, _pady, _side):
    _close_button = Button(_win, text="Close", command=_win.quit)
    _close_button.grid(row=_row, column=_column, padx=_padx, pady=_pady, sticky=_side)
    return _close_button


def sql_connect(_data_set, username_input, password_input, localhost_input, database_input, tablename_input):
    conn_str = 'mysql+pymysql://{}:{}@{}/{}'.format(username_input, password_input, localhost_input, database_input)
    _con = create_engine(conn_str)
    try:
        if _con is not None:
            _data_set.to_sql(tablename_input, con=_con, if_exists='replace')
            messagebox.showinfo("Connection Status", "Connection successful!")
            messagebox.showinfo("Loading", "Data Loading")
        else:
            print("Connection not established.")
            messagebox.showinfo("Connection Status", "Connection not successful!")
        messagebox.showinfo("Done", "Data Loading Successful Done")
    except Exception as error: 
        messagebox.showinfo("Connection Status", "Connection not successful! \nCheck your username and password")

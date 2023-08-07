<h1 align="center">Hi 👋, I'm Harsh Munjal</h1>
<h3 align="center">New to Data Analytics and it's tempting :)</h3>

### 🌱 I’m currently learning **Python,Mysql,PowerBi**

### 📫 How to reach me harshmunjalca@gmail.com   <img src="281769.png" alt="gmail" width="30" height="30"/>
### 📫 How to reach me [Linkedin](https://www.linkedin.com/in/harsh-munjal/)   <img src="Linkedin.png" alt="linkedin" width="30" height="30"/>


<h3 align="left">Languages and Tools:</h3>
<p align="left"> <a href="https://www.mysql.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original-wordmark.svg" alt="mysql" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/></a><a href="https://powerbi.microsoft.com/en-ca/" target="_blank" rel="noreferrer"> <img src="Microsoft-Power-BI-Symbol.png" alt="Power-BI" width="40" height="40"/> </a> </p>



## 🔭 I’m currently working on **Marketing Data set**

This repository contains Python and SQL scripts to perform data analysis and visualization using Power BI. The pipeline consists of the following steps:

### Step 1: Read Data in Python

- Use Python to read the relevant datasets and load them into memory for further processing.
  
 ```python
import pandas as pd

file_name1="Data Files\Marketing_Campaign_Dimension.xlsx"
file_name2="Data Files\Marketing_Campaign_Fact.xlsx"

raw_df1=pd.read_excel(file_name1) 

raw_df2=pd.read_excel(file_name2)
```

### Step 2: Data Cleansing and Transformation

- Perform data cleansing and transformation tasks in Python to ensure the data is clean and ready for analysis.
```python
import pandas as pd

# Dt_Customer is the time when the customer enrolled into the campaign


# It is in object type we have to convert them into Date Format 

raw_df1['Dt_Customer']=pd.to_datetime(raw_df1['Dt_Customer'],infer_datetime_format=False, dayfirst=True)
raw_df1['Enrolled_Date']=raw_df1['Dt_Customer'].dt.date
raw_df1=raw_df1.drop('Dt_Customer',axis=1)

# Calculating Age in "Age" Column the dropping the year of birth Column
raw_df1['Age']=2023-raw_df1['Year_Birth']
raw_df1=raw_df1.drop('Year_Birth',axis=1)

#Converting the Martital Status of people into numbers so that we can calculate Family Size
raw_df1.loc[(raw_df1['Marital_Status']=="Single"),"Marital_Status_People"] = "1"
raw_df1.loc[(raw_df1['Marital_Status']=="Together"),"Marital_Status_People"] = "2"
raw_df1.loc[(raw_df1['Marital_Status']=="Married"),"Marital_Status_People"] = "2"
raw_df1.loc[(raw_df1['Marital_Status']=="Divorced"),"Marital_Status_People"] = "1"
raw_df1.loc[(raw_df1['Marital_Status']=="Widow"),"Marital_Status_People"] = "1"
raw_df1.loc[(raw_df1['Marital_Status']=="Alone"),"Marital_Status_People"] = "1"
raw_df1.loc[(raw_df1['Marital_Status']=="Absurd"),"Marital_Status_People"] = "1"
raw_df1.loc[(raw_df1['Marital_Status']=="YOLO"),"Marital_Status_People"] = "1"
```

### Step 3: Merge Datasets in Python

- Combine and merge dataset 1 and dataset 2 into a single unified dataset using Python.
```python
# Peforming "Left" Merge (Joins) of Fact and Dimension Table on "ID" Column 
merge_file=pd.merge(raw_df1,raw_df2,on="ID",how="left")

# Removing Missing Values 
merge_file.dropna(inplace=True)

# Calling function from Helper Function 
load_in_execl("Merged_Fact_Dim",merge_file,"Merged_Fact_Dim","xlsx")
```
```python
# Helper Function "load_in_execl"
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl import Workbook

def load_in_execl(_Sheet_Name,_Data_set,_Save_File,_Extension):

    wb=Workbook()
    
    #Deleted predefined excel file 
    del wb['Sheet']
    

    # Created a worksheet name "Merged Data"
    ws=wb.create_sheet(_Sheet_Name)
    


    # This is the bydefault function to write data into excel file 
    for r in dataframe_to_rows(_Data_set,index=False,header=True):
            ws.append(r)

    
    # Save Excel file in XLSX format so tht i can upload it PowerBI for Visualization
    
    wb.save(f"Data Files\{_Save_File}.{_Extension}")
```

### Step 4: Connect Python and MySQL through Visual

- Set up a connection between Python and MySQL to facilitate data transfer between the two platforms.
```python
# Visual Helper Functions 

from tkinter import * 
from tkinter import messagebox

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

```
```python
# Actual code of My SQL Connect 
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


```

### Step 5: Send Data to MySQL

- Transfer the merged dataset from Python to MySQL for storage and further processing.
```python
# Heper Function SQL_Connect
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

```
```python

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

```

### Step 6: Data Grouping and Views in SQL

- Apply data grouping and create views in MySQL to organize and simplify the data for analysis.
```SQL
ALTER TABLE marketing_campaign_merged_data
MODIFY Enrolled_Date DATE;

```
```SQL
CREATE VIEW `education` AS 
SELECT Education,
COUNT(Education) AS `People with Education Type` 
FROM `marketing_campaign_merged_data` 
GROUP BY Education;

```
```SQL
CREATE VIEW `family_details` AS 
SELECT ID ,
Education,Marital_Status,
Income,
Enrolled_Date,Age,
Kidhome + Teenhome + Marital_Status_PeoplE AS `Family_Size`,
MntWines + MntFruits + MntMeatProducts + MntFishProducts + MntSweetProducts + MntGoldProds AS `Total_Spend`,
NumDealsPurchases + NumWebPurchases + NumCatalogPurchases + NumStorePurchases AS `Total_Deal_Purchases`,
NumWebVisitsMonth
FROM marketing_campaign_merged_data;
```
```SQL
CREATE  VIEW `marital_status_of_customer` AS 
SELECT Marital_Status,
COUNT(Marital_Status) AS `People with Status` 
FROM marketing_campaign_merged_data 
GROUP BY Marital_Status;
```



### Step 7: Connect SQL and Power BI

- Connect SQL and Power BI using the ODBC connector to enable smooth data access.

### Step 8: Data Visualization in Power BI

- Utilize Power BI to create insightful visualizations and reports based on the processed data.
<p align="center"> <img src="Final Assignment.png" alt="mysql" width="600" height="500"/> </a> </p>

Feel free to explore the scripts in the repository to understand the implementation of each step in detail. For any questions or issues, please don't hesitate to open an issue or contact the repository owners.

Happy data analysis and visualization!

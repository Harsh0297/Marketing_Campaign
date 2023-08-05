import pandas as pd 
from helper_functions import load_in_execl


file_name1="Data Files\Marketing_Campaign_Dimension.xlsx"
file_name2="Data Files\Marketing_Campaign_Fact.xlsx"

raw_df1=pd.read_excel(file_name1) 

raw_df2=pd.read_excel(file_name2)
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

# Peforming "Left" Merge (Joins) of Fact and Dimension Table on "ID" Column 
merge_file=pd.merge(raw_df1,raw_df2,on="ID",how="left")

# Removing Missing Values 
merge_file.dropna(inplace=True)

# Calling function from Helper Function 
load_in_execl("Merged_Fact_Dim",merge_file,"Merged_Fact_Dim","xlsx")



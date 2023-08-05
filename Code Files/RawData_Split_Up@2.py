import pandas as pd
from helper_functions import load_in_execl

file_name="Data Files\marketing_campaign.csv"

raw_df=pd.read_csv(file_name,sep="\t")

# print(raw_df.info())

raw_df2=raw_df[['ID','Year_Birth','Education','Marital_Status','Income','Kidhome','Teenhome','Dt_Customer','Recency']]

exluded_columns=raw_df[['Year_Birth','Education','Marital_Status','Income','Kidhome','Teenhome','Dt_Customer','Recency']]

raw_df3=raw_df.drop(columns=exluded_columns)

# Calling Function from Helper Function
load_in_execl("Marketing_Campaign_Dimension",raw_df2,"Marketing_Campaign_Dimension","xlsx")

# Calling Function from Helper Function
load_in_execl("Marketing_Campaign_Fact",raw_df3,"Marketing_Campaign_Fact","xlsx")


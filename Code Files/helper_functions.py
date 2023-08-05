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


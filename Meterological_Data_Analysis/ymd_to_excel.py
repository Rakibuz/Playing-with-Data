import xlsxwriter     
      
workbook = xlsxwriter.Workbook('C:/Users/rakib/OneDrive/Documents/GitHub/Playing-with-Data/Meterological_Data_Analysis/ymd_to_excel.xlsx')    
worksheet = workbook.add_worksheet()     
       
# Rows and columns are zero indexed.     
row = 1    
column = 0    
      
content = ["Parker", "Smith", "John"]     
      
# iterating through the content list     
for item in content :     
      
    # write operation perform     
    worksheet.write(row, column, item)     
      
    # incrementing the value of row by one with each iterations.     
    row += 1    
          
workbook.close()     
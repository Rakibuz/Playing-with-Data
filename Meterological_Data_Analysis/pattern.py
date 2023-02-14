import xlsxwriter     
      
workbook = xlsxwriter.Workbook('C:/Users/rakib/OneDrive/Documents/GitHub/Playing-with-Data/Meterological_Data_Analysis/ymd_to_excel.xlsx')    
worksheet = workbook.add_worksheet()   
row = 1    
column = 2  
month=0

list = [31,28,31,30,31,30,31,31,30,31,30,31]
list_leapyear = [31,29,31,30,31,30,31,31,30,31,30,31]
month_num_list=[1,2,3,4,5,6,7,8,9,10,11,12]
#list_leapyear=[4,4,2]
#list=[4,3,2]
for y in range(1998,2000,1):
    if(y%400 == 0) and (y%100 == 0):
        #leap year
        list=list_leapyear
    elif(y%4 ==0) and (y%100 != 0):
        #leap year
        list=list_leapyear
    else:
        #not leap year
        list=list

    print("Year: ",y)
    
    for x in list:
        print("List: ",x)
         
        for i in range(1, x+1, 1):
            #print(i)
            print("%s %s %s"%(y,month_num_list[month],i))
            
            worksheet.write(row, column, i) 
            ##worksheet.write(row, column, item)
            row += 1    
        month+=1
    month=0

workbook.close() 
 
 
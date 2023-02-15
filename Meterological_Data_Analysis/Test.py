list_not_leapyear = [31,28,31,30,31,30,31,31,30,31,30,31]
list_leapyear = [31,29,31,30,31,30,31,31,30,31,30,31]

def CheckLeap(y):
    if(y%400 == 0) and (y%100 == 0):
        #leap year
        list=list_leapyear
        #print(list)
    elif(y%4 ==0) and (y%100 != 0):
        #leap year
        list=list_leapyear
        #print(list)
    else:
        #not leap year
        list=list_not_leapyear
        #print(list)
    return list

print(CheckLeap(2022))
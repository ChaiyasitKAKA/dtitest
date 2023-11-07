#อ่านไฟล์ 
f_dti = open("op03.txt", "r", encoding="utf-8")
try :
    data = f_dti.read()
    
    for data_line_read in data :
        print(data_line_read,end="")
    
except Exception :
    print("Contact us 0578688755")
finally :
    f_dti.close()
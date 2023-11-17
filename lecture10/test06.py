#อ่านไฟล์ 
f_dti = open("op03.txt", "r", encoding="utf-8")
try :
    
    data = f_dti.readline()
    print(data, end="")
    data = f_dti.readline()
    print(data,end="")
    data = f_dti.readline()
    print(data,end="")
except Exception :
    print("Contact us 0578688755")
finally :
    f_dti.close()
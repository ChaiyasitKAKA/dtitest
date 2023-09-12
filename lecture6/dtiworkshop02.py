#วิเคราะห์
#มอง feature การทำงานว่ามีอะไรบ้าง เพื่อไปสร้าง function
# รับค่าทะเบียนรถ น้ำหนักรถ inputCarDetial
# ตรวจสอบน้ำหนักรถ และแสดงผล checkCarAndShowWeight

def inputCardetail() :
    CarNo = input("ทะเบียนรถ:")
    CarWeight = float(input("น้ำหนักรถ:"))
    return CarNo , CarWeight

def checkCarAndShowWeight(CarNo,CarWeight) :
    if CarWeight > 1000 :
        print(f"ทะเบียนรถ {CarNo} น้ำหนักไม่ผ่าเกณฑ์")
    else : 
        print(f"ทะเบียนรถ {CarNo} น้ำหนักผ่าเกณฑ์")
    

print("----------------------")
print("    Truck checker     ")
print("----------------------")
print("---------------------------")
CarNo , CarWeight = inputCardetail()
print("------------------------------")
checkCarAndShowWeight(CarNo, CarWeight)
print("------------------------------")

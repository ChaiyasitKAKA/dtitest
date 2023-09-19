#8. จงเขียนโปรแกรมPython ของโปรแกรมตรวจสอบค่า PH ของน้ าปะปาจากจังหวัดต่างๆ โดยรับชื อจังหวัด และค่า PH ทางแป้นพิมพ์ และแสดงผลทางหน้าจอ โดยหากค่า PH เป็น 7-8 แสดงข้อความ "Result is Normal" หากค่า PH มากกว่า 8 ให้แสดงข้อความ "Result is Acid" หากค่า PH น้อยกว่า 7 ให้แสดงข้อความ"Result is Alkali"
def InputnameprovinceAndPH():
    name = str(input("Enter name Province:"))
    PH = int(input("Enter Value PH:"))
    return name,PH

def checkPH(PH,name) :
    if   PH >= 7 and PH <= 8:
        print(f"{name}: PH = {PH}:Result is Normal")
    elif PH > 8:
        print(f"{name}: PH = {PH}:Result is Acid")
    elif PH < 7 :
        print(f"{name}: PH = {PH}:Result is Alkali")
    else:
        print(f"{name}: PH = {PH}: Result is Unknown")    
    

name,PH = InputnameprovinceAndPH()
checkPH(PH,name)

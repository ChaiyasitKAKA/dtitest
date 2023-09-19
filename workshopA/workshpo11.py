#11. จงเขียนโปรแกรมPython ค านวณค่าโทรศัพท์ โดยรับชื อผู้ใช้โทรศัพท์ เบอร์โทรศัพท์ และจ านวนนาทีที ใช้โทรศัพท์ทางแป้นพิมพ์ ทั้งนี้ ในการคิดค่าโทรศัพท์ มีหลักเกณฑ์ในการคิดค านวณ ดังนี้  นาทีที  1 -15 คิดที นาทีละ 5 บาท นาทีที  16 –30 คิดที นาทีละ 3 บาท นาทีที 31 เป็นต้นไปคิดที นาทีละ 1.50 บาท
def inputNamePhonenumAndTime():
    name = str(input("Enter name:"))
    phone = str(input("Enter phonenumber:"))
    time = int(input("Enter Time to use:"))
    return name,phone,time

def Calamountmoney(time):
    if time >= 31 :
        cost = time * 1.50
        return cost
    elif time >= 16 and time <= 30 :
        cost = time * 3
        return cost
    elif time >= 1 and time <=15 :
        cost = time * 5
        return cost
    else:
        return "No Resault"


def showresault(name,phone,time,cost):
    print(f"Name: {name} phonenum:{phone}")
    print(f"Time to use:{time} minuet price:{cost}Baht")

name,phone,time = inputNamePhonenumAndTime()
cost=Calamountmoney(time)
showresault(name,phone,time,cost)
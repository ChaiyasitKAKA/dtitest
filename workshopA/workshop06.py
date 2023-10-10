#6. จงเขียนโปรแกรมPython ของโปรแกรมค านวณอัตราดอกเบี้ยเงินกู้ โดยรับชื อผู้กู้ และจ านวนเงินกู้ทางแป้นพิมพ์ และแสดงผลอัตราดอกเบี้ยเงินกู้ที ค านวณได้ทางหน้าจอ ทั้งนี้อัตราดอกเบี้ยคิดจากยอดเงินกู้ หากเงินกู้ตั้งแต่ 1000บาทขึ้นไป คิดอัตราดอกเบี้ยที ร้อยละ 2.5 ของเงินกู้ หากไม่ถึงคิดอัตราดอกเบี้ยที ร้อยละ 5.5 ของเงินกู้
def inputnameAndAmount():
    name = str(input("Enter Name:"))
    amount = int(input("Enter Amount:"))
    year = int(input("Enter year:"))
    return name,amount,year

#ดอกเบี้ยที่ต้องจ่ายในงวดนั้น = (เงินต้นคง  เหลือ x อัตราดอกเบี้ย  ต่อปี x จำนวนวันในงวด) / จำนวนวันต่อปี
def CalInterestloan(amount,years):
    if amount >= 1000 :
        interest_rate = 2.5
    else:
        interest_rate = 5.5
    Interestloan = (amount * interest_rate * years) / 100
    return Interestloan

def showinterestloan(name,interloan):
    print(f"name:{name} loan interest :{interloan}")

name,amount,year = inputnameAndAmount()
interloan = CalInterestloan(amount,year)
showinterestloan(name,interloan)
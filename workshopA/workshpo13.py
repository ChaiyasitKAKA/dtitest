#13. จงเขียนโปรแกรมPython ตรวจสอบผลการเรียนของนักเรียน โดยป้อนจ านวนนักเรียนที จะตรวจสอบทางแป้นพิมพ์  และในการตรวจสอบนักเรียนแต่ละคนให้ป้อน รหัสนักเรียน ชื อนักเรียน และเกรดเฉลี ยนักเรียน โดยหากเกรดเฉลี ยไม่ถึง 2.00 ให้แสดงข้อความทางหน้าจอว่า “สอบไม่ผ่าน”หากได้เกรดเฉลี ยตั้งแต่ 2.00 ขึ้นไปให้แสดงข้อความทางหน้าจอว่า “สอบผ่าน”def inputnameAndAmount():
def inputidAndpointAmdamount
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
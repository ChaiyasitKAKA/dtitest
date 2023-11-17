try :
    num1 = int(input("Enter number 1 : "))
    num2 = int(input("Enter number 2 : "))

    result1 = num1 * num2 
    result2 = num1 / num2 

    print(f"{num1} x {num2} = {result1}")
    print(f"{num1} / {num2} = {result2}")
except ValueError :
    print("ตรวจสอบข้อมูลเนื่องจากป้อนข้อมูลไม่ถูกต้อง")
except ZeroDivisionError :
    print("ตัวเลขตัวที่ 2 ห้ามเป็น 0")
except Exception :
    print("Contact us 0256846480")
finally :
    print("Wow Woow Wooow")
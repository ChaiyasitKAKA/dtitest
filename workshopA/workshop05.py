#5. จงเขียนโปรแกรมPython ค านวนหาเงินเดือนสุทธิของพนักงาน แล้วแสดงผลทางหน้าจอ โดยรับค่ารหัสพนักงาน ชื อพนักงาน และเงินเดือนปกติของพนักงานทางแป้นพิมพ์ ทั้งนี้เงินเดือนสุทธิของพนักงานนั้นจะต้องหักค่าภาษี และเบี้ยประกันสังคมออกจากเงินเดือนปกติเสียก่อน โดยที พนักงานต้องเสียภาษี 7% ของเงินเดือนปกติ และจ่ายค่าเบี้ยประกันสังคม 500 บาท สูตร เงินเดือนสุทธิ  =  เงินเดือนปกติ  -(เงินเดือนปกติ * 7 / 100) -500
def InputValue():
    id = str(input("Enter ID:"))
    name = str(input("Enter Name:"))
    salary = int(input("Enter Salary:"))
    return id, name , salary
def Calsalary(salary):
    compleaatsalary  =  salary  -(salary * 7 / 100) -500
    return compleaatsalary
def Shwocompleatsalary(id,name,compleatsalary):
    print(f"{id}:{name}:Salary={compleatsalary}$")

id,name,salary = InputValue()
compleatsalary = Calsalary(salary)
comsal=Shwocompleatsalary(id,name,compleatsalary)

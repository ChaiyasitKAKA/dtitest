#12. จงเขียนโปรแกรมPython ค านวณค่าใช้จ่ายในการซื้อแพ็กเกจท่องเที ยวของกรุ๊ปทัวร์ ทั้งนี้รูปแบบการใช้งานโปรแกรมจะต้องป้อนชื อหัวหน้ากรุ๊ปทัวร์ เบอร์โทรศัพท์ติดต่อกลับของหัวหน้ากรุ๊ปทัวร์ และจ านวนคนที จะไปทัวร์ ทางแป้นพิมพ์ โดยในการคิดค านวณค่าใช้จ่ายในการซื้อแพ็กเกจท่องเที ยวของกรุ๊ปทัวร์ มีหลักเกณฑ์ในการคิดค านวณ ดังนี้ จ านวนคนที จะไปทัวร์ตั้งแต่ 1 -2 คน คิดแพ็กเกจละ 300บาทต่อคนจ านวนคนที จะไปทัวร์ตั้งแต่ 3 -5 คน คิดแพ็กเกจละ 250บาทต่อคนจ านวนคนที จะไปทัวร์ตั้งแต่ 6 -10 คน คิดแพ็กเกจละ 210บาทต่อคนจ านวนคนที จะไปทัวร์ตั้งแต่ 11 คนขึ้นไป คิดแพ็กเกจละ 150บาทต่อคนเพื อหาค่าน้อยที สุด มากที สุดผลรวม และค่าเฉลี ย ของข้อมูลที ป้อนN จ านวน
def inputTourDetails():
    group_leader_name = input("Enter group leader's name: ")
    contact_number = input("Enter contact number: ")
    group_size = int(input("Enter group size: "))
    return group_leader_name, contact_number, group_size

def calculatePackageCost(group_size):
    if group_size >= 1 and group_size <= 2:
        package_cost = 300 * group_size
    elif group_size >= 3 and group_size <= 5:
        package_cost = 250 * group_size
    elif group_size >= 6 and group_size <= 10:
        package_cost = 210 * group_size
    elif group_size >= 11:
        package_cost = 150 * group_size
    else:
        print("Invalid group size.")
        package_cost = 0
    return package_cost

def showResult(group_leader_name, contact_number, group_size, package_cost):
    print("-----------------------------")
    print("      TOUR PACKAGE COST      ")
    print("-----------------------------")
    print(f"Group Leader's Name: {group_leader_name}")
    print(f"Contact Number: {contact_number}")
    print(f"Group Size: {group_size}")
    print(f"Package Cost: {package_cost} THB")

group_leader_name, contact_number, group_size = inputTourDetails()
package_cost = calculatePackageCost(group_size)
showResult(group_leader_name, contact_number, group_size, package_cost)

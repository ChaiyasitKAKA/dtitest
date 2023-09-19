#13. จงเขียนโปรแกรมPython ตรวจสอบผลการเรียนของนักเรียน โดยป้อนจ านวนนักเรียนที จะตรวจสอบทางแป้นพิมพ์  และในการตรวจสอบนักเรียนแต่ละคนให้ป้อน รหัสนักเรียน ชื อนักเรียน และเกรดเฉลี ยนักเรียน โดยหากเกรดเฉลี ยไม่ถึง 2.00 ให้แสดงข้อความทางหน้าจอว่า “สอบไม่ผ่าน”หากได้เกรดเฉลี ยตั้งแต่ 2.00 ขึ้นไปให้แสดงข้อความทางหน้าจอว่า “สอบผ่าน”
def inputStudentDetails():
    student_id = input("Enter student ID: ")
    student_name = input("Enter student name: ")
    average_grade = float(input("Enter average grade: "))
    return student_id, student_name, average_grade

def checkStudentResult(average_grade):
    if average_grade < 2.00:
        return "สอบไม่ผ่าน"
    else:
        return "สอบผ่าน"

def showResult(student_id, student_name, result):
    print("-----------------------------")
    print("     ผลการเรียนของนักเรียน     ")
    print("-----------------------------")
    print(f"รหัสนักเรียน: {student_id}")
    print(f"ชื่อนักเรียน: {student_name}")
    print(f"ผลการเรียน: {result}")

num_students = int(input("ป้อนจำนวนนักเรียนที่ต้องการตรวจสอบ: "))

for i in range(num_students):
    student_id, student_name, average_grade = inputStudentDetails()
    result = checkStudentResult(average_grade)
    showResult(student_id, student_name, result)

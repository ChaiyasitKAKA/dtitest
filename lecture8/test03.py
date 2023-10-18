# OOP
class DtiSau :
    # data / property member ค่าข้อมูล
    stu_name = ""
    score = 0 
    gpa = 0
    
    # method member  คือ การทำงาน
    def histudent(self):
        print(f"สวัสดี {self.stu_name} " )
        
    def showScoreAndGPA(self):
        print(f"คะแนน {self.score} ได้เกรด  {self.gpa}")
        

# สร้าง object
obj01 = DtiSau() # ชื่อคลาสที่มี( ) เราเรียกว่าเป็นการสั่งให้ constrictor ของคลาสทำงาน
obj02 = DtiSau()
  
obj01.stu_name = input("Enter Name:")
obj01.histudent()
obj02.stu_name = input("Enter Name:")
obj02.score = 99
obj02.gpa = 3.99
obj02.histudent()
obj02.showScoreAndGPA()
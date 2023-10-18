#self เปลียบเสมือนสิ่งที่ใฃ้แทนคลาสตัวเอง เพื่อที่จะเรียกใช้member ในคลาสตัวเองได้
class Test04:
    data1 = 10
    
    #constructor
    def __init__(self,data2,data3) :
        print("Hi...")
        self.data2 = data2
        self.data3 = data3
        
        
    #method member
    def showSumData(self):
        print(self.data1 + self.data2 +self.data3)
        self.showWow()
        
    def showWow(self):
        print("Wow wow wow...")
        
objA = Test04(20,30)
objA.showSumData()
objA.showWow()
objB = Test04(10,20)
objB.showSumData()
objB.showWow()
objC = Test04(20,100)
objC.showSumData()
objC.showWow()
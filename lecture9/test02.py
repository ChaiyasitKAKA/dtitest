class Dtitest03 :
    # data
    infoA = 10
    infoB = 0
    infoC = 0

    #constructor จะเป็นตัวทำให้ object
    # ที่สร้างจากคลาสเดียวกัรไม่ตำเป็นต้องเหมือนกัน
    #constructor
    def __init__(self, infoB , infoC) :
        self.infoA = infoB
        self.infoC = infoC
        print("Wow wow wow")
        
    #method
    def showMixandInfo(self , Mix):
        print(self.infoA + self.infoB + self.infoC + Mix)
        
#สร้าง object
sau1 = Dtitest03(20 , 30)
sau2 = Dtitest03(10 , 100)
sau3 = Dtitest03(20 , 30)



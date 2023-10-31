class DtiTest01 :
    pass

class DtiTest02 :
    #data/attribute/property/field คือ ตัวแปรประเภทหรนี่ง
    infoA = ""
    infoB = 20
    
    #method คือ ฟังชั่นประเภทหนึ่ง
    def showHi(self) :
        print("Hi>>//")
        
    def showInfoAandB(self) :
        print(self.infoA)
        print(self.infoB)
# สร้างobject
     
objA = DtiTest02()
objA.showHi()
objA.showInfoAandB()       
objB = DtiTest02()
sombat = DtiTest02()

objA.infoA ="xxxx"
objB.infoB = 100

print(objA.infoB + objB.infoB)

sombat.showInfoAandB()

# คุณสมบัติ Encapsulation(ห่อหุ้ม data/attrubute/field/propr\erty)
class Dtitest05 :
    infoA   = 10 # ไม่ได้ Encap
    __infoB = 20  # Encap ดูจาก __????? -> เป็นการกำหนด access_modifier เป็น private
   
    def __init__(self,infoC,infoD) :
        self.infoC   = infoC #ไม่ได้ Encap
        self.__infoD = infoD #Encap

    #เมื่อใดก็ตาม Encap จะต้องมีเมธอด 2 ตัวนี้เสมอ คือ  get set  ของ data ตัวนั้น
    def setInfoB(self,infoB) :
         self.__infoB = infoB

    def getInfoB(self) :
        return self.__infoB

    def setInfoD(self,infoD) :
         self.__infoD = infoD

    def getInfoD(self) : 
        return self.__infoD
   
    def showInfo(self) :
        print(self.infoA, end='')
        print(self.__infoB, end='')
        print(self.infoC, end='')
        print(self.__infoD)
        print('-------------')
    
ob1 = Dtitest05(30,40)
ob1 = Dtitest05(30,100)
ob1.showInfo()
ob1.infoA   = 555
#ob1.__infoB = 999 ไม่เปลี่ยน เพราะมัน Encap
ob1.setInfoB(999)
ob1.showInfo()
#print(ob1.__infoB + on1.__infoD) มันถูก Encap  ถ้าจะใช้งานต้องใช้เมธอด get
print(ob1.getInfoB() + ob1.getInfoD())
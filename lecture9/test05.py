# inheritance สืบทอด คือ การที่คลาส1 สืบทอดอีกคลาส1 *** (re-use)
# สืบทอด มีแม่ (super class) มีลูก(sup class)
# แม่มีอะไรลูกมีด้วยเมื่อมีดารสืบทอด (Inheritance)

# polymorphism (พ้องรูป:พฤติกรรมเดียวกันแต่วิธีต่างกัน) คือ การที่คลาสลูกเอาเมธอดคลาสแม่มาเขียนใหม่ 
class Sau01 :
    infoA = 10
    
    def showHi() :
        print('Hi....')

class Sau02(Sau01) : #Inheritance
    infoB = 20
    
    def showHey():
        print('Hey....')
    #overiding method : polymorphism
    def showHi():
        print('Hi Hi Hi....')
ob1 = Sau01()
ob2 = Sau02()
ob2.showHi()


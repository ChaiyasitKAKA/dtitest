# Destructor

class DtiTest04 :
    data1 = 10
    def __init__(self,data2) :
        self.data2 = data2
        print("Hi....")
        
        
    def doTask1(self) :
        print('^_^')
         
    def doTask2(self,value) :
        print(value)
    
    # Destructor
    def __del__(self) :
         print("Bye Bye.....")
    
def showHey ():
    print('hey....')
    
#..........................................

sauA = DtiTest04(20)
sauB = DtiTest04(30)
sauC = DtiTest04(20)

sauC.doTask2('T_T')
sauC.doTask1()
print(sauA.data1 + sauB.data1)
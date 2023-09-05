#build-in function 
#about string
#ตัวเลข
import math
#inputradius
def inputradius() :
    r = input("ป้อนรัศมี :")
    #return r
    #r = float(input("ป้อนรัศมี :"))
    #return r
    #return input("ป้อนรัศมี :") 
    #return float(input("ป้อนรัศมี :"))
    return r

#calAreaCircle
def calAreaCircle( r ) :
    area = math.pi * r ** 2  
    # area = math.pi * r * r  
    # area = math.pi * math.pow(r, 2)  
    # return math.pi * math.pow(r, 2)
    return area


#calRoundCircle 2 * PI * r
def calRoundCircle (r) : 
    round = 2 * math.pi * r
    return round
#calCubeCircle 4 / 3 * PI * r * r * r 
def  calCubeCircle (r) :
    cube = 4/3 * math.pi * r * r * r 
    return cube

#showResult ทศนิยม 4 ตำแหน่ง
#พื้นที่วงกลมเป็น .... เส้นรอบวงเป็น .... ปริมาตรทรงกลมเป็น
print(f"พื้นที่วงกลม {area} เส้นรอยวงเป็น {round} ปรืมาตรทรงกลมเป็น {cube} ")

inputradius()


 
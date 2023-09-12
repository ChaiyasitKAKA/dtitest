#dtiworkshhop01.py
#คำนวณหาพื้นที่สามเหลี่ยม โดยรับค่าฐาน และสูงทางแป้นพิมพ์และแสดงพื้นที่สามเหลี่ยมที่คำนวณได้ทางหน้าจอ

#วิเคราะห์และออกแบบ
#มองหา featureการทำงานว่ามีอะไรบ้าง เพื่อไปสร้างเป็น function
#1 รับค่า ฐาน สูง
#2 คำนวน แสดงผล
def inputBaseHigh() :
    base = float (input("base : ") ) 
    high = float (input("high : ") )
    return base,high

def calAndshowTriangleArea(base, high) :
    area = base * high /2
    print(f"สามเหลี่ยมฐาน {base:.2f} สูง {high:.2f} มีพิ้นที่ {area:.2f}")
print("----------------------")
print("Calculate Triangle Area ")
print("----------------------")
base, high = inputBaseHigh()
print("----------------------")
calAndshowTriangleArea(base, high)
print("----------------------")



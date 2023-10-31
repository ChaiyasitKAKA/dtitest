import test06
import math
# import test08 '
from test08 import calcircleArea,calSquareArea,calTriangleArea


print(f'resault 10 + 20 = {test06.SumNum(10,20)}') 

test06.ShowHi()

print(f'price 20000 tax {2000 * test06.VAT}')

print(f'7 ยกกำลัง 15 มีต่า {math.pow(7,15)}')

print(f',พท้นที่วงกลม รัศมนี - มรค่า {math.pi* math.pow(3,2)}')

print(f'พื้นที่วงกลม รัสมี 8 {calcircleArea(8)}')

print(f'พื้นที่สีเหลี่ยม กว้าง ๅจ ยาว ถ มีค่า {calSquareArea(10,25)}')
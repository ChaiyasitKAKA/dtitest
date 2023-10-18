var2 = (10, 20, "Hello", True, (111,"wow"), "มานะ")
# var2[2] = "Hi" Error
# การเปบี่ยนแปลงค่า เพิ่ม ลบ ข้อมูล Tuple
# list() , tuple()
varTemp= list(var2)
varTemp[2] = "Hi"
var2 = tuple(varTemp)
print(var2)
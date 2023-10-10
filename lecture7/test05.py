# list fuctionn/Tuple function
# len()นับจำนวน,min(),max(),
#List
var1 = [10, 20, "Hello", True, [111,"wow"], "มานะ"]

#Tuple 
var2 = (10, 20, "Hello", True, (111,"wow"), "มานะ")

print(f"in var1 havedata {len(var1)} Data")
print(f"in var2 havedata {len(var2)} Data")
# min max ใช้ไม่ได้กับจ้อมูลคนละชนิดกัน
# print(min(var1)) Error
var3 = [10,20,30,True,10,20]
var4 = (10,20,30,True,10,20)
print(min(var3)) # True = 1 Flase = 0 
print(max(var4))
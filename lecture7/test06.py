# slicing data in list and tuple
# List
var1 = [10, 20, "Hello", True, [111,"wow"], "มานะ"]
# Tupele
var2 = (10, 20, "Hello", True, (111,"wow"), "มานะ")
# 20 , Hello , True
print(var1[1:4])
# True, (111, 'wow')
print(var2[3:5])
# 10, 20, 'Hello'
print(var2[:3])
# 'Hello', True, [111, 'wow'], 'มานะ'
print(var1[2:])

# List 
my_list = [10,20,10,"hi",True,[20,"hello"],(20,30),{10,20}]
print(my_list)


# Tuple
my_Tuple = (10,20,10,"hi",True,(20,"hello"),[10,True],{"hi",20})
print(my_Tuple)


# Set ไม่มีลำดับ
my_set = {10,20,10,"hi",True,(20,10)}

                    # Key คือ  associtive  คือ ตัวชี้ที่อ้างอิงไปยัง Value
                    # Value คือ ค่าข้อมูลที่เอาไปใฃ้งานได้
# Dictionaly ---->>> key:Value / key-->>> String-number / Value-->> Everthing
my_dict  = {"name":"Jhon", "age":20, 555:999, "flag":True}
print(my_dict["name"])
print(my_dict["age"]+my_dict[555])
my_dict["name"] = "kaka"
my_dict["major"] = "DTI"
print(my_dict)
my_dict.pop("name")
my_dict.pop(555)
print(my_dict)
my_dict.popitem()
print(my_dict)


for data in my_dict:
    print(data, end=" ")

print()  

for data in my_dict.keys() :
    print(data, end=" ")

print()

for data in  my_dict.values() :
    print(data, end=" ")
    
my_dict1 = {"a":10, "b":20, "c":30}

my_dict2 = my_dict1

my_dict3 = my_dict1.copy(  )


print(my_dict2)
print(my_dict3)

my_dict2["a"] = 999
my_dict3["a"] = 666

print(my_dict1)
print(my_dict2)
print(my_dict3)

# List 
my_list = [10,20,10,"hi",True,[20,"hello"]]
print(len(my_list))

# Tuple
my_Tuple = (10,20,10,"hi",True,(20,"hello"))

print(my_Tuple)
print(len(my_Tuple))
list_fr_tuple = list(my_Tuple)
list_fr_tuple[3] = "Hi" 
my_Tuple = (list_fr_tuple)
print(my_Tuple)

# Set ไม่มีลำดับ
my_set = {10,20,10,"hi",True,(20,10)}
print(my_set)  
print(len(my_set))

for data in my_set :
    print(data, end="/")

print("__________________________")
list_fr_set = list(my_set)
print(list_fr_set)
list_fr_set[1] = 30
print("__________________________")
my_set = set(list_fr_set)
print(my_set)


my_set1 = {10,20,30,"Hi"}
my_set2 = {10,"Hello","Hi",True}

my_set1.add(999)
print(my_set1)
my_set1.remove("Hi")
print(my_set1)

print(my_set1.intersection(my_set2))
print(my_set1.union(my_set2))

# lin , min , max
# print(min(my_set2)) Error

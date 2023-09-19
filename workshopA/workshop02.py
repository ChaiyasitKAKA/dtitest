#2. จงเขียนโปรแกรมPython ของโปรแกรมค านวณหาค่าเฉลี ยของคะแนนจากการสอบ 3 ครั้ง โดยรับค่า รหัสนักเรียน ชื อนักเรียน และคะแนนสอบแต่ละครั้งรวม 3 ครั้งทางแป้นพิมพ์ แล้วแสดงผลค่าเฉลี ยที ค านวณได้ทางหน้าจอ
def InputidAndname():
    id = int(input("Enter ID:"))
    name = input("Enter Name:")
    return id,name

def Inputpoint(id,name):
    data_list = []
    for i in range(3) :
        print(f"Enter points time{i + 1}")
        points = float(input("Enter points:"))
        data_set = {'id': id, 'name': name, 'points': points}
        # Append the data set to the list
        data_list.append(data_set)
    return data_list


def calaverage(data_list):
    all_points = [data['points'] for data in data_list]
    average_points = sum(all_points) / len(all_points)
    return average_points

def ShowAverage(name,id,average_point):
    print(f"Average Points  {name} (ID: {id}): {average_point}")

id, name = InputidAndname()
data_list = Inputpoint(id, name)
average_point = calaverage(data_list)
ShowAverage(name,id,average_point)







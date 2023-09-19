data_list = []
id_value = int(input("Enter ID: "))
name = input("Enter name: ")
for i in range(3) :
    print(f"Enter point {i + 1} time :")
    points = float(input("Enter points: "))
    
    data_set = {'id': id_value, 'name': name, 'points': points}
    data_list.append(data_set)

# Merge the points from all three data sets
all_points = [data['points'] for data in data_list]

# Calculate the average points
average_points = sum(all_points) / len(all_points)

# Display the average points
print("Average Points :", average_points)

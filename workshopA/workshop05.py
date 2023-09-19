# Define a function to calculate y based on x
def calculate_y(x):
    y = 2 * x**2 + 2 * x + 1
    return y

# Input the value of x from the user
x = float(input("Enter the value of x: "))

# Calculate y using the function
result_y = calculate_y(x)

# Display the calculated y value
print("The value of y is:", result_y)

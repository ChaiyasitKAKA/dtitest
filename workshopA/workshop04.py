# Define a function to calculate y based on x
def calculateeqution(x):
    y = 2 * x**2 + 2 * x + 1
    return y

x = float(input("Enter the value of x: "))

# Calculate y using the function

slove_y = calculateeqution(x)

# Display the calculated y value
print("The value of y is:", slove_y)

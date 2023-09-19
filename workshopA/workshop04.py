def inputX():
    x = float(input("Enter the value of x: "))
    return x

def calculateeqution(x):
    y = 2 * x**2 + 2 * x + 1
    return y

def Showresault(y) :
    print(f" y is: {y}")

print("_______________________________")
x = inputX()
print("_______________________________")
y = calculateeqution(x)
print("_______________________________")
Showresault(y)
print("_______________________________")


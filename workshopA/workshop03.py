def inputproductnameAndprice():
    productname = str(input("Productname:"))
    price = int(input("Price:"))
    return productname,price

def caltaxAndshow(productname,price) :
    pay = price - (price * 7/100)
    print(f"Productname: {productname} Tax: {pay} ")
print("--------------------------")
print("       TAXcalculator      ")
print("--------------------------")
productname,price=inputproductnameAndprice()
caltaxAndshow(productname,price)



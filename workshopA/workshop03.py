#3 จงเขียนโปรแกรมPython ของโปรแกรมค านวณภาษี ณ ที จ่ายของสินค้า โดยรับชื อสินค้า และราคาสินค้า ทางแป้นพิมพ์และแสดงผลภาษีที ค านวณได้ทางหน้าจอ ทั้งนี้ภาษีคิดที ร้อยละ 7 ของราคาสินค้า
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



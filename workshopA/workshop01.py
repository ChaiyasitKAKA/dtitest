#1. จงเขียนโปรแกรมPython ค านวณหาราคาขายสินค้า โดยรับชื อสินค้า และราคาสินค้า(ต้นทุน) ทางแป้นพิมพ์ แล้วค านวณหาราคาขายของสินค้า โดยราคาขายสินค้าจะคิดเพิ มจากราคาสินค้า (ต้นทุน) ร้อยละ 10 สูตร ราคาขายสินค้า  =  ราคาสินค้า(ต้นทุน)  + (ราคาสินค้า(ต้นทุน) * 10 / 100)
def InputAndcalCost() :
    cost = int(input("cost:"))
    seal_price =cost + ((cost)*10 / 100)
    return seal_price , cost

def CalincomeshowsealpriceAndincome(seal_price,cost) :
    print(f"sealprice {seal_price} Baht")
    cal_come = seal_price - cost 
    print(f"income {cal_come} Baht")


print("--------------------------")
print("        SEALPRICE         ")
print("--------------------------")
seal_price,cost = InputAndcalCost()
print("----------------------")
CalincomeshowsealpriceAndincome(seal_price,cost)
print("----------------------")
  
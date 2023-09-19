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
  
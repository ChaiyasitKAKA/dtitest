width  = float(input("width:"))
long = float(input("long:"))
heigth = float(input("heigth:"))
cal_font =(width)*(long)
cal_side =(width)*(heigth)
cal_top =(heigth)*(long)
Gallon = round( ((cal_font*2)+(cal_side*2)+(cal_top*2))/5 )
#print 4 type
print("จะต้องซื้อ:",Gallon,"gallon")
print("จะต้องซื้อ:"+""+str(Gallon)+"gallon")
print(f"จะต้องซื้อ:{Gallon}gallon")
print("จะต้องซื้อ:{}gallon".format(Gallon))

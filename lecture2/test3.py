emp_name =input("naem:")
sale_price =input("price:")
print("---------------------")
commission = float(sale_price) * 10 / 100
#fucntion to string be a number -> int() float()
print(f" {emp_name} allprice {float(sale_price):.2f} commission {commission:.2f} bath")
print((emp_name),"allprice",float(sale_price),"commission",(commission),"bath") #,
print(emp_name+"allprice"+str(float(sale_price))+"commission"+str(float(commission))+"bath") #+
print("{} allprice {:.2f} commission {:.2f} bath ".format(emp_name,float(sale_price),commission))# format
#10. จงเขียนโปรแกรมPython ของโปรแกรมแสดงข้อความต้อนรับนักศึกษา โดยรับชั้นปีทางแป้นพิมพ์แล้วแสดงข้อความต้อนรับ ดังนี้กรณีป้อน 1 แสดงข้อความ "Welcome Freshman"กรณีป้อน 2 แสดงข้อความ "Welcome Sophomore"กรน ณีป้อ3 แสดงข้อความ "Welcome Junior"กรณีป้อน 4 แสดงข้อความ "Welcome Senior"
def Inputyearclass():
    return int(input("Enter your year class 1-4:"))
    
def checkyear(year):
    if year == 1:
        return  "Welcome Freshman"
    elif year == 2:
        return  "Welcome Sophomore"
    elif year == 3:
        return  "Welcome Junior"
    elif year == 4:
        return  "Welcome Senior"
    else:
        return "Invalid year. Please enter a year between 1 and 4."


def showResault(message): 
    print("-----------------------------")
    print("        WELCOME MESSAGE      ")
    print("-----------------------------")
    print(f"       {message}            ")


year =  Inputyearclass()
message = checkyear(year)
showResault(message)

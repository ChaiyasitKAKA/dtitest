#7. จงเขียนโปรแกรมPython ของโปรแกรม Game Bingo โดยให้ผู้ใช้ป้อนตัวเลขที ต้องการทายทางแป้นพิมพ์ แล้วให้โปรแกรมตรวจสอบว่าตรงกับที โปรแกรมก าหนดไว้หรือไม่ในที นี้คือ 25 หากไม่ตรงให้แสดงข้อความว่า "Not Correct !!!." ทางหน้าจอ หากตรงให้แสดงข้อความว่า "Correct, You are the winner" 7. จงเขียนโปรแกรมPython ของโปรแกรม Game Bingo โดยให้ผู้ใช้ป้อนตัวเลขที ต้องการทายทางแป้นพิมพ์ แล้วให้โปรแกรมตรวจสอบว่าตรงกับที โปรแกรมก าหนดไว้หรือไม่ในที นี้คือ 25 หากไม่ตรงให้แสดงข้อความว่า "Not Correct !!!." ทางหน้าจอ หากตรงให้แสดงข้อความว่า "Correct, You are the winner" 
import random

def Randomnumber():
    random_number = random.randint(1, 100)
    return random_number

def InputNum():
    guess_number = int(input("Enter number:"))
    return guess_number

def CheckNum(random_number, guess_number):
    if guess_number == random_number:
        print("----------YAY----------------")
        print("-Correct, You are the winner-")
    else:
        print("-----  Not correct  !!! -----")
        print("-----  Try again    !!! -----")

def showResult(random_number):
    print(f"Random Number is: {random_number}")

print("-----------------------------")
print("        GAME BINGO           ")
print("-----------------------------")
random_number = Randomnumber()
guess_number = InputNum()
CheckNum(random_number, guess_number)
showResult(random_number)

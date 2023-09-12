# คำสั่ง break กับ continue 
# มักใช้ร่วมกับ Control flow

for x in range(5) :
    if x == 3 :
        break; #break ทำงานเมื่อไหร่จบ loop ทันที
    print(f"SAU..{x}")
        
print("++++++++++++++++++++++++")

for y in range(5) :
    if y == 3 :
        continue; #continue ทำงานเมื่อไหร่ ไปรอบต่อไปทันที
    print(f"SAU..{y}")
# ลบไฟล์
import os
from os import remove
if os.path.exists("op02.txt") :
    os.remove("op02.txt")
    print("Finish")
else :
    print("ไฟล์ที่จะลบไม่มี")
    
import os
import shutil

p = os.getcwd()
print(p)

#เขียนไฟล์
#data = str(p) + "\\Hello\\test_file.py"
#file = open(data, "w")
#file.write("print('hello world')")
#file.close

#อ่านไฟล์
# data = str(p) + "\\Hello\\test_file.py"
# file = open(data, "r")
# text = file.read()
# print(text)

#shutil.move(str(p) + "\\for_ta.py", str(p) + "\\Hello\\" + "for_ta.py") #ย้ายไฟล์

#os.rename(str(p) + "\\Hello\\for_ta.py", str(p) + "\\Hello\\yeet_ta.py") #เปลี่ยนชื่อไฟล์

#os.mkdir("C:/Users/X3Z/Desktop/my_work/Hello") #สร้างไฟล์

#os.remove(str(p) + "\\Hello\\test.py") #ลบไฟล์

#os.removedirs(str(p) + "\\test2") #ลบโฟลเดอร์

print(os.path.isfile(str(p) + "\\Hello\\yeet_ta.py")) #เช็คไฟล์
print(os.path.isabs(str(p) + "\\Hello")) #เช็คโฟลเดอร์
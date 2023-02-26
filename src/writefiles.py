# การใช้คำสั่งเขียนข้อมูลและเพิ่มมข้อมูล อ่านข้อมูล

with open('data.txt', 'w', encoding='utf-8') as file:
    file.write('Hello World')


# เพิ่มข้อมูลใหม่ได้ และขึ้นบรรทัดใหม่โดยใช้ \n
def adddata(text):
    with open('add-data.txt', 'a', encoding='utf-8') as file:
        file.writelines(text +'\n')

# adddata('Hello Thailand')

def readdata():
    with open('add-data.txt', encoding='utf-8') as file:
        # data = file.readlines() # อ่านข้อมูลรูปแบบ list
        data = file.read() # อ่านข้อมูลทั้งหมดในไฟล์
        print(data)
readdata()
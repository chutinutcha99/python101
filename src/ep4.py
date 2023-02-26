import tkinter as tk
import csv

# Writer
def writecsv(datalist):
    with open('data.csv','a',encoding='utf-8',newline='') as file:
        fw = csv.writer(file) # fw = file writer
        fw.writerow(datalist) # datalist = ['pen','pencil','eraser']

# data = ['ขนม',20,'7:00 น.']
# writecsv(data)

# def readcsv():
#     with open('data.csv',encoding='utf-8',newline='') as file:
#         fr = csv.reader(file) # fr = file reader
#         data = list(fr)
#     return data
# data = readcsv()
# print(data)

def save_data():
    # ดึงข้อมูลจาก entry widgets
    name = entry_name.get()
    email = entry_email.get()

    # สร้าง list ของข้อมูล
    data = [name, email]

    # เรียกใช้ฟังก์ชัน writecsv() เพื่อเขียนข้อมูลลงในไฟล์ CSV
    writecsv(data)

    # ล้างข้อมูลใน entry widgets
    entry_name.delete(0, tk.END)
    entry_email.delete(0, tk.END)


root = tk.Tk()
root.title("บันทึกข้อมูล")
 
# สร้าง label และ entry widgets สำหรับกรอกข้อมูล
label_name = tk.Label(root, text="ชื่อ:")
label_name.grid(row=0, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

label_email = tk.Label(root, text="อีเมล:")
label_email.grid(row=1, column=0)
entry_email = tk.Entry(root)
entry_email.grid(row=1, column=1)

# สร้างปุ่มบันทึกข้อมูล
button_save = tk.Button(root, text="บันทึก", command=lambda: save_data())
button_save.grid(row=2, column=1)

root.mainloop()



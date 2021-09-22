from tkinter import *
import math


def calculation(event):
    ผลลัพธ์ = float(น้ำหนัก_textbox.get())/math.pow(float(ส่วนสูง_textbox.get())/100, 2)
    ผลลัพธ์_label1.configure(text=ผลลัพธ์)
    if ผลลัพธ์ >= 30.0:
        ผลลัพธ์_label2.configure(text='อ้วนมาก')
    elif ผลลัพธ์ >= 25.0:
        ผลลัพธ์_label2.configure(text='อ้วน')
    elif ผลลัพธ์ >= 23.0:
        ผลลัพธ์_label2.configure(text='น้ำหนักเกิน')
    elif ผลลัพธ์ >= 18.6:
        ผลลัพธ์_label2.configure(text='น้ำหนักเหมาะสม')
    elif ผลลัพธ์ <= 18.5:
        ผลลัพธ์_label2.configure(text='น้ำหนักน้อยเกินไป')


main_page = Tk()
ส่วนสูง_label = Label(main_page, text='ส่วนสูง (cm)')
ส่วนสูง_label.grid(row=0, column=0)

น้ำหนัก_label = Label(main_page, text='น้ำหนัก (kg)')
น้ำหนัก_label.grid(row=1, column=0)

ผลลัพธ์_label1 = Label(main_page, text='ผลลัพธ์')
ผลลัพธ์_label1.grid(row=2, column=1)

ผลลัพธ์_label2 = Label(main_page, text=' ')
ผลลัพธ์_label2.grid(row=3, column=1)

ส่วนสูง_textbox = Entry(main_page)
ส่วนสูง_textbox.grid(row=0, column=1)

น้ำหนัก_textbox = Entry(main_page)
น้ำหนัก_textbox.grid(row=1, column=1)

calculation_button = Button(main_page, text="คำนวน")
calculation_button.grid(row=2, column=0)
calculation_button.bind('<Button-1>', calculation)

mainloop()

from tkinter import *

myForm = Tk()
myForm.title('Моя форма')
myForm.geometry("200x350")
myForm.configure(bg="#DB7093")

def calculate():  
    number = (ent_a.get().strip())
    if not number:
        lb.config(text="Пусто/пробелы")
        return
    try:
        number = float(number)
    except ValueError:
        lb.config(text="Не число")
        return
    if flag.get()==1:
        lb.config(text=f"= {number - 8}")
    if flag2.get()==1:
        lb.config(text=f"= {number + 2}")
    if flag3.get()==1:
        lb.config(text=f"= {number * 3}")
    if flag.get()==1 and flag2.get()==1 and flag3.get()==1:
        lb.config(text=f"= {(number - 8 + 2) * 3}")
    if flag.get()==1 and flag2.get()==1:
        lb.config(text=f"= {number - 8 + 2}")
    if flag2.get()==1 and flag3.get()==1:
        lb.config(text=f"= {(number + 2) * 3}")
    if flag.get()==1 and flag3.get()==1:
        lb.config(text=f"= {(number - 8) * 3}")
             
btn_calc = Button(text="Вычислить",command = calculate, width = 20)
btn_calc.place(x=25, y=230)

ent_a = Entry()
ent_a.place(x=25, y=33, width=90)

lb=Label(font="20", bg="#DB7093", fg="white")
lb.place(x=50, y=290, width=110)

flag = IntVar()
flag2 = IntVar()
flag3 = IntVar()

chb_1=Checkbutton(text="-8", variable=flag, font="16")
chb_1.place(x= 30, y=80)

chb_2=Checkbutton(text="+2", variable=flag2, font="16")
chb_2.place(x= 30, y=120)

chb_1=Checkbutton(text="*3", variable=flag3, font="16")
chb_1.place(x= 30, y=160)

myForm.mainloop()
# Вариант 3
from tkinter import *

myForm = Tk()
myForm.title('Моя форма') #устанавливает заголовок окна
myForm.geometry("450x100") #размер окна и отступ от левого врехнего края
myForm.configure(bg="#BDB76B")

def max_numb():
    a = (ent_a.get().strip())
    b = (ent_b.get().strip())
    
    if not a or not b:
        lb.config(text="Пусто/пробелы")
        return
    else:
        lb.config(text=f"= {max(a,b)}")
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        lb.config(text="Не число")
        return

def min_numb():
    a = (ent_a.get().strip())
    b = (ent_b.get().strip())
    
    if not a or not b:
        lb.config(text="Пусто/пробелы")
        return
    else:
        lb.config(text=f"= {min(a,b)}")
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        lb.config(text="Не число")
        return

btn_max = Button(root, text="Наибольшее",command = max_numb, width = 20, bg="#DEB887")
btn_max.place(x=70, y=50)

btn_min = Button(text="Наименьшее",command = min_numb, width = 20, bg="#DEB887")
btn_min.place(x=70, y=20)

ent_a = Entry()
ent_a.place(x=25, y=33, width=30)

ent_b = Entry()
ent_b.place(x=245, y=33, width=30)

lb=Label(font="20", bg="#BDB76B")
lb.place(x=300, y=35, width=120)

myForm.mainloop() # запускает цикл для обработки событий окна для взаиомодейтсвия с пользователем

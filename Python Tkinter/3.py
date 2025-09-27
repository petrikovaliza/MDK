from tkinter import *

myForm = Tk()
myForm.title('Моя форма')
myForm.geometry("210x200")
myForm.configure(bg="#FFF0F5")

def proverka():
    word = str(ent_a.get().strip())
    if not word.isalpha():
        lb.config(text="Не то")
        return
    if not word:
        lb.config(text="?Пусто?")
        return
    elif flag.get()==1:
        if word.startswith("А") or word.startswith("а"):
            lb.config(text="ДА")
        else:
            lb.config(text="НЕТ")
    elif flag.get()==2:
        if word.endswith("Ж") or word.endswith("ж"):
            lb.config(text="ДА")
        else:
            lb.config(text="НЕТ")
    else:
        if "Ф" in word or "ф" in word:
            lb.config(text="ДА")
        else:
            lb.config(text="НЕТ")
 
ent_a = Entry()
ent_a.place(x=20, y=33, width=100)

lb=Label(font="20", bg="#FFF0F5")
lb.place(x=120, y=30, width=90)

flag=IntVar()

rb1 = Radiobutton(text= "Начинается с A", font="14", value=1, command=proverka, variable=flag, bg="#E6E6FA")
rb1.place(x=10, y=60)

rb2 = Radiobutton(text= "Кончается с Ж", font="14", value=2, command=proverka, variable=flag, bg="#E6E6FA")
rb2.place(x=10, y=100)

rb3 = Radiobutton(text= "Содержит Ф", font="14", value=3, command=proverka, variable=flag, bg="#E6E6FA")
rb3.place(x=10, y=140)

myForm.mainloop()
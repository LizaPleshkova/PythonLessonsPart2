'''
1. создание виджета -> width - размер знакоместа;
параметры шрифта в виде кортежа;
jystify='left' or LEFT - left\right\top\... Только для многострочного текста
2. размещение виджета in window -> pack() | place() | grid()

ttk - модуль для графического редактирования виджета
'''
from tkinter import *
from tkinter import ttk

def clicked():
    print('Clicked')

root = Tk()
root.geometry('600x400+500+200')

# btn = Button(root, text='Button', command=clicked, width=10, font= 'Arial 20 italic')
# btn = Button(root, text='Button', command=clicked, width=10, font= ('Comic Sans MS', 20))

btn = Button(root, text='Button1\n2 2', justify='left', command= clicked)
# btn.configure(width=20, height=5)
# btn['font'] = 'Arial 15'


btn.pack()

# btn2 = ttk.Button(root, text='Button')
# btn2.pack()

root.mainloop()
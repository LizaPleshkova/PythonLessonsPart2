'''
упаковщики - методы которые позволяют размещать виджеты :
    pack() - доп=expand\side\fill
    grid()
    place()

    pack() - доп=expand\side\fill
    простейший метод не подходит для  размещения сложных интерфейсов, подходит для простоых интерфейсов и разметки окна
    создание фрейма
    в рамках одного родительского элемента нкльзя использовать различные менеджеры геометрии

side - TOP(default) LEFT

Frame - контейнерный виджет дл организации других виджетов
LabelFrame = фрейм с рамкой
'''

from tkinter import *

root = Tk()

root.geometry("600x400+100+300")
#
# f_top = Frame(root)
# f_bottom = Frame(root)
# f_top.pack()
# f_bottom.pack()

# f_top = LabelFrame(root, text='Top Frame',padx=10, pady=8)
# f_bottom = LabelFrame(root, text='Bottom Frame',padx=10, pady=8)
# f_top.pack(pady=20)
# f_bottom.pack()

# l1 = Label(root, text="1", font="15", fg="#fff", bg="#3498db", width=8, height=4).pack()
# l2 = Label(root, text="2", font="15", fg="#fff", bg="#2ecc71", width=8, height=4).pack()
# l3 = Label(root, text="3", font="15", fg="#fff", bg="#f1c40f", width=8, height=4).pack()
# l4 = Label(root, text="4", font="15", fg="#fff", bg="#34495e", width=8, height=4).pack()

# l1 = Label(root, text="1", font="15", fg="#fff", bg="#3498db", width=8, height=4).pack(side=TOP)
# l2 = Label(root, text="2", font="15", fg="#fff", bg="#2ecc71", width=8, height=4).pack(side=LEFT)
# l3 = Label(root, text="3", font="15", fg="#fff", bg="#f1c40f", width=8, height=4).pack(side=RIGHT)
# l4 = Label(root, text="4", font="15", fg="#fff", bg="#34495e", width=8, height=4).pack(side=BOTTOM)

#
# l1 = Label(f_top, text="1", font="15", fg="#fff", bg="#3498db", width=8, height=4).pack(side=LEFT)
# l2 = Label(f_top, text="2", font="15", fg="#fff", bg="#2ecc71", width=8, height=4).pack(side=LEFT)
# l3 = Label(f_bottom, text="3", font="15", fg="#fff", bg="#f1c40f", width=8, height=4).pack(side=LEFT)
# l4 = Label(f_bottom, text="4", font="15", fg="#fff", bg="#34495e", width=8, height=4).pack(side=LEFT)

# l1 = Label(root, text="1", font="15", fg="#fff", bg="#3498db", width=8, height=4).pack(expand=1,anchor=S )

f_top = Frame(root,padx=10, pady=15)
f_bottom = Frame(root)
f_top.pack()
f_bottom.pack()

l2 = Label(f_top, text="Login", font="15", fg="#fff", bg="#2ecc71", width=8, height=4).pack(side=RIGHT)
l3 = Label(f_top, text="Password", font="15", fg="#fff", bg="#f1c40f", width=8, height=4).pack(side=RIGHT)
b = Button(f_bottom, text='Input' )
b.pack(expand=0)

root.mainloop()
'''
виджеты
menu ..
text
    wrap - перенос по буквам or по словам
    insertbackground- цвет курсора
    selectbackground - цвет выделения
    ызфсштп1\ызфсштп2\spacing3 - м
Scrollbar привязать не только к текстовой области но и квиджеу
    связь scrollbar с текстовым полем по нужной оси
'''

from tkinter import *
root = Tk()
root.geometry('800x600+500+200')

f_menu = Frame(root, bg="#1F252A", height=40)
f_text = Frame(root)
f_menu.pack(fill=X)
f_text.pack(fill=BOTH,expand=1)

l_menu = Label(f_menu, text="Menu", bg="#2B3239", fg="#C6DEC1", font="Arial 10")
l_menu.place(x=10, y=10)

t = Text(f_text, bg="#343D46", fg="#C6DEC1", padx=10, pady=10, wrap=WORD,
         insertbackground="#EDA756", selectbackground="#4E5A65", spacing3=10)
t.pack(fill=BOTH,expand=1, side=LEFT)

scroll = Scrollbar(f_text, command=t.yview)
scroll.pack(fill=Y, side=LEFT)
t.config(yscrollcommand=scroll.set)# настроенный скролл сюда подставляем
root.mainloop()
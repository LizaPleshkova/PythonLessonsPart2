'''
grid()- болбше подходит для организации сложных интерфейсов
        позволяет строить сетки, таблицы, нумерация с 0
        размещяем виджеты руководствуясь сеткой
        column - номер столбца
        columnspan - сколько столбцов должен занимать элемент
        ipadx, ipady - установка отступов, по горизонтали\по вертикали от границ элемента до его текста
        padx, pady - установка отступов, от ячейки gtid-а до границ элемента
        row
        rowspan - сколько строк
        sticky - схож с anchor - выранивает элементы по сторонам света
'''

from tkinter import *

root = Tk()
# root.geometry('400x200+500+200')
# f = Frame(root)
# f.pack()

# btn_list=[
#     '7', '8', '9',
#     '4', '5', '6',
#     '3', '2','1',
#     '0',
# ]
#
# row = 0
# column = 0
# for i in btn_list:
#     if i == '0':
#         btn = Button(f, text=i, padx=10, pady=5).grid(row=row, columnspan = 3)
#     else:
#         btn = Button(f, text=i, padx=10, pady=5).grid(row=row, column=column)
#         column += 1
#         if column == 3:
#             column = 0
#             row += 1



# btn7 = Button(f, text='7', padx=10, pady=5).grid(row=0, column=0)
# btn8 = Button(f, text='8', padx=10, pady=5).grid(row=0, column=1)
# btn9 = Button(f, text='9', padx=10, pady=5).grid(row=0, column=2)
#
# btn4 = Button(f, text='4', padx=10, pady=5).grid(row=1, column=0)
# btn5 = Button(f, text='5', padx=10, pady=5).grid(row=1, column=1)
# btn6 = Button(f, text='6', padx=10, pady=5).grid(row=1, column=2)
#
# btn3 = Button(f, text='3', padx=10, pady=5).grid(row=2, column=0)
# btn2 = Button(f, text='2', padx=10, pady=5).grid(row=2, column=1)
# btn1 = Button(f, text='1', padx=10, pady=5).grid(row=2, column=2)
#
# btn0 = Button(f, text='0', padx=10, pady=5).grid(row=3, column=0, columnspan=3)

login = Label(root, text='login').grid(row=0, column=0, padx=10, pady=10, sticky= W)
l_user = Entry(root).grid(row=0, columnspan=2, column=1, padx=10,sticky=W+E)

password = Label(root, text='password').grid(row=1, column=0, padx=10, pady=10, sticky= W)
p_user = Entry(root).grid(row=1,columnspan=2,  column=1, padx=10, sticky=W+E)


btn = Button(root, text='Вход',padx=5).grid(row=3, column=0, pady=10)
btn_reg = Button(root, text='Регистрация', padx=5).grid(row=3, column=1, pady=10)
btn_forgot = Button(root, text='забыли пароль?', padx=5).grid(row=3, column=2, pady=10, padx=10)
root.mainloop()


'''
Напишиет программу, состоящую из семи кнопок, цвета которой соответствуют цветам радуги.
При нажатии на ту или иную кнопку в текстовом поле должен появиться код цвета, а в метку -- название цвета.
#ff0000: Красный
#ff7d00: Оранжевый
#ffff00: Желтый
#00ff00: Зеленый
#007dff: Голубой
#0000ff: Синий
#7d00ff: Фиолетовый
'''

# from tkinter import *
#
# def btns_click():
#     name_color.delete(0,END)
#
# def btn1_click():
#     btns_click()
#     cod_color['text'] = 'Red'
#     name_color.insert(0,'#ff0000')
#
# def btn2_click():
#     btns_click()
#     cod_color['text'] = 'Orange'
#     name_color.insert(0,'#ff7d00')
#
# def btn3_click():
#     btns_click()
#     cod_color['text'] = 'Yellow'
#     name_color.insert(0, '#ffff00')
#
# def btn4_click():
#     btns_click()
#     cod_color['text'] = 'Green'
#     name_color.insert(0, '#ffff00')
#
# def btn5_click():
#     btns_click()
#     cod_color['text'] = 'Blue'
#     name_color.insert(0, '#007dff')
#
# def btn6_click():
#     btns_click()
#     cod_color['text'] = 'Dark Blue'
#     name_color.insert(0, '#0000ff')
# def btn7_click():
#     btns_click()
#     cod_color['text'] = 'Purple'
#     name_color.insert(0, '#7d00ff')
#
#
# root = Tk()
# root.geometry('300x325+500+200')
# cod_color = Label(root, height=2)
# cod_color.pack(fill=X)
#
#
# name_color = Entry(root, justify='center')
# name_color.pack(fill=X, )
#
#
# btn1 = Button(root, command=btn1_click, height = 2,bg='#ff0000').pack(fill=X)
# btn2 = Button(root, command=btn2_click,height = 2, bg='#ff7d00').pack(fill=X)
# btn3 = Button(root, command=btn3_click,height = 2, bg='#ffff00').pack(fill=X)
# btn4 = Button(root, command=btn4_click,height = 2, bg='#00ff00').pack(fill=X)
# btn5 = Button(root, command=btn5_click,height = 2, bg='#007dff').pack(fill=X)
# btn6 = Button(root, command=btn6_click, height = 2,bg='#0000ff').pack(fill=X)
# btn7 = Button(root, command=btn7_click,height = 2, bg='#7d00ff').pack(fill=X)
#
#
# root.mainloop()



# второй вариант

# from tkinter import *
#
# def btns_click(_cod_color, _name_color):
#     name_color.delete(0,END)
#     cod_color['text'] = _cod_color
#     name_color.insert(0,_name_color)
#
# root = Tk()
# root.geometry('300x325+500+200')
# cod_color = Label(root, height=2)
# cod_color.pack(fill=X)
#
# name_color = Entry(root, justify='center')
# name_color.pack(fill=X, )
#
# btn1 = Button(root, command=lambda: btns_click('#ff0000', 'red'), height = 2,bg='#ff0000').pack(fill=X)
# btn2 = Button(root, command=lambda: btns_click('#ff7d00', 'orange'),height = 2, bg='#ff7d00').pack(fill=X)
# btn3 = Button(root, command=lambda: btns_click('#ffff00', 'yellow'),height = 2, bg='#ffff00').pack(fill=X)
# btn4 = Button(root, command=lambda: btns_click('#00ff00', 'green'),height = 2, bg='#00ff00').pack(fill=X)
# btn5 = Button(root, command=lambda: btns_click('#007dff', 'blue'),height = 2, bg='#007dff').pack(fill=X)
# btn6 = Button(root, command=lambda: btns_click('#0000ff', 'black blue'), height = 2,bg='#0000ff').pack(fill=X)
# btn7 = Button(root, command=lambda: btns_click('#7d00ff', 'Purple'),height = 2, bg='#7d00ff').pack(fill=X)
#
# root.mainloop()

# третий вариант
#
# from tkinter import *
#
# def get_color(cod,name):
#     e.delete(0,END)
#     l['text'] = cod
#     e.insert(0,name)
#
# root = Tk()
# root.geometry('300x200+500+200')
#
# l=Label(root, justify='center')
# l.pack(fill=X)
#
# e = Entry(root, justify='center')
# e.pack(fill=X)
#
# colors = {
#     '#ff0000': 'Красный',
#     '#ff7d00': 'Оранжевый',
#     '#ffff00': 'Желтый',
#     '#00ff00': 'Зеленый',
#     '#007dff': 'Голубой',
#     '#0000ff': 'Синий',
#     '#7d00ff': 'Фиолетовый'
# }
# # в лямбда ыункции указатель на переменную а не на значения
# for key, value in colors.items():
#     btn = Button(root, bg=key, command=lambda color=value, cod=key : get_color(cod, color))
#     btn.pack(fill=X)
#
# root.mainloop()



from tkinter import *

class Buttons():
    def __init__(self, master, text_color, hex_color):
        self.text_color = text_color
        self.hex_color = hex_color
        self.b = Button(root, bg=hex_color, command=self.get_color)
        self.b.pack(fill=X)

    def get_color(self):
        l['text'] = self.text_color
        e.delete(0, END)
        e.insert(0, self.hex_color)

root = Tk()
root.geometry('300x200+500+200')

l=Label(root, justify='center')
l.pack(fill=X)

e = Entry(root, justify='center')
e.pack(fill=X)

colors = {
    '#ff0000': 'Красный',
    '#ff7d00': 'Оранжевый',
    '#ffff00': 'Желтый',
    '#00ff00': 'Зеленый',
    '#007dff': 'Голубой',
    '#0000ff': 'Синий',
    '#7d00ff': 'Фиолетовый'
}
# в лямбда ыункции указатель на переменную а не на значения
for key, value in colors.items():
    Buttons(root, value, key)

root.mainloop()
'''
Entry -  созздает однострочное текстовое поле, в которое пользователь может вводить какие-то данные,
так же и для вывода информации для пользователя
'''
from tkinter import *

def add_str():
    e.insert(END,'Hello!')

def del_str():
    e.delete(0,END)

def get_str():
    l_text['text'] = e.get()


root = Tk()
root.geometry('600x400+500+200')

l = Label(root, text='Input text')
l.pack()

e = Entry(root)
e.insert(0,'Hello')
e.insert(END, ' world!')
e.pack()

l_text = Label(root, bg='blue', fg='#fff')
l_text.pack(fill=X)

btn_add = Button(root, text='add', command=add_str).pack()
btn_del = Button(root, text='del', command=del_str).pack()
btn_get = Button(root, text='get', command=get_str).pack()
root.mainloop()
'''
place - наиболее гибкие
    можем накладывать один элемент на другой
    height, width
    anchor
    bordermode границы элемента
    relheight, relwidth - доля от высоты родительского контейнера
    relx, rely - относительное смещение в процентаъ (0.0 ; 1.0)
    x,y - задать координаты элемента; смещение в пикселях точечно
'''

from tkinter import *

root = Tk()
root.geometry('400x400+500+200')
# l1 = Label(root, text='Hello', bg='#3498db', fg='#fff', font='16', padx=20, pady=8)
# l1.place(x=0,y=0,anchor='e')
#
# l2 = Label(root, text='Hello', bg='#3498db', fg='#fff', font='16', padx=20, pady=8)
# l2.place(relx=0.5,rely=0.5,anchor='c')#center


# left = Button(root, text='1', bg='#3498db', fg='#fff', font='16', padx=20, pady=8)
# left.place(relx=0.0,rely=0.0, anchor='nw')#left
#
# center = Button(root, text='2', bg='#3498db', fg='#fff', font='16', padx=20, pady=8)
# center.place(relx=0.5,rely=0.5,anchor='c')#center
#
# right = Button(root, text='3', bg='#3498db', fg='#fff', font='16', padx=20, pady=8)
# right.place(relx=1.0,rely=1.0, anchor='se')#center

dark = Label(root, bg='black', padx=20, pady=8)
dark.place(relheight= 0.8, relwidth=0.8, relx= 0.1,rely=0.1)

root.mainloop()
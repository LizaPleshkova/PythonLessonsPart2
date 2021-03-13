
from tkinter import *
from tkinter import ttk

img_path= r'E:\Python\[WebForMySelf] [Андрей Кудлай] Python. Полное руководство\videokurs\part2\4\04_files\python-logo.png'

root = Tk()
root.geometry('600x400+500+200')

# l = Label(root, text="Текст в строке 1\nСтрока 2\nСтрока 3\nСтрока4\n", bg='red', fg='#fff', font=('Comic Sans Ms',20,'bold'), justify=LEFT,
#           width=30, height=5, anchor='sw')
# l.pack()

img = PhotoImage(file=img_path)
l_logo = Label(root, image=img)
l_logo.pack()
root.mainloop()
'''
tkinter - установлен по умолчанию
1. создать объект класса Tk ->
2.root.mainloop()- для отображения окна на экране; метод, который запуск цикл обработки событий окна, для взаимодействия с пользователями
будет отлавливать\собирать события и выполняет все методы, привязанные к этим событиям
'''
from tkinter import *

to_ico = r'E:\Python\[WebForMySelf] [Андрей Кудлай] Python. Полное руководство\videokurs\part2\1\01_files\python.ico'
root = Tk()

root.title('Мое первое GUI приложение')# заголовок окна
root.iconbitmap(to_ico)# логотип окна

root.geometry('600x400+500+200')# изменение размера окна и  его положения
root.resizable(False,False)# доступ к изменению размера окна по ширине и высоте

# root.config(bg='red')
root['bg'] = 'red'


root.mainloop()
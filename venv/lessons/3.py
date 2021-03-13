from tkinter import *
import time

def check_time():
    btn_time['text'] = time.strftime('%H:%M:%S')
    # print(time.strftime('%H:%M:%S'))

clicks = 0

def counter():
    global clicks
    clicks += 1
    root.title(f'Counter {clicks}')

VAL1 = 10
VAL2 = 5
def my_sum():
    global VAL1, VAL2
    print(f'{VAL1} + {VAL2} = {VAL1+VAL2}')
    btn_sum['text'] = f'{VAL1+VAL2}'

def my_dif():
    global VAL1, VAL2
    print(f'{VAL1} - {VAL2} = {VAL1-VAL2}')

def my_div():
    global VAL1, VAL2
    print(f'{VAL1} / {VAL2} = {VAL1/VAL2}')

def my_multipl():
    global VAL1, VAL2
    print(f'{VAL1} * {VAL2} = {VAL1*VAL2}')

root = Tk()

#hometask +-*/
root.title('Counter')
root.geometry('600x400+500+200')

btn_sum = Button(root, text='+', command=my_sum)
btn_dif = Button(root, text='-', command=my_dif)
btn_div = Button(root, text='/', command=my_div)
btn_multipl = Button(root, text='*', command=my_multipl)

btn_div.pack()
btn_dif.pack()
btn_sum.pack()
btn_multipl.pack()
# btn_time = Button(root, text='Check time', command=check_time)
# btn_time.pack()
#
# btn_count = Button(root, text='Counter', command=counter)
# btn_count.pack()

root.mainloop()
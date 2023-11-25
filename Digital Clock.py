from tkinter import *
from time import *
from time import strftime

window = Tk()
window.title('CLOCK')
window.configure(bg='black')
window.geometry('1700x300')
window.resizable(False, False)


def time():
    t = strftime('%H:%M:%S  %p')
    label.config(text=t)
    label.after(1000, time)


label = Label(window, font=('ds-digital', 200), anchor='center', bg='black', fg='light grey')
label.pack()
time()

mainloop()

import tkinter as tk
import os
from tkinter import filedialog as fl  # работа с диалоговыми окнами
'''добавить меню с пунктом инфо (как работать с блокнотом) 
и пункт о программе (имя атвтора и версии)'''

def file_select():
    filename = fl.askopenfilename(initialdir='/', title='Выберите файл',
                                  filetypes=(('Текстовый файл', '.txt'),
                                             ('Все файлы', '*')))
    text['text'] = text['text'] + ' ' + filename  # добавит абсолютный путь до файла
    os.startfile(filename)


window = tk.Tk()
window.title('Проводник')
window.geometry('450x150')
window.configure(bg='black')
window.resizable(False, False)  # запретили менять размер окошка
text = tk.Label(window, height=2, width=64, text='Файл',
                background='silver')
text.grid(column=1, row=1)
button_select = tk.Button(window, height=2, width=13, text='Выберите файл',
                          background='silver', foreground='blue',
                          command=file_select)
button_select.grid(column=1, row=2)

window.mainloop()  # обновление окна
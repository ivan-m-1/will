from tkinter import *

tk = Tk()
tk.title("Мой мессенджер") # Добавим заголовок окна

canvas = Canvas(tk, width=400, height=400)
canvas.pack()
canvas.create_line(0, 0, 500, 500)
canvas.create_rectangle(10, 10, 50, 50)

# 1. Создаем виджет Label (надпись), куда будет выводиться текст
# wraplength нужен, чтобы текст переносился на новую строку, если он слишком длинный
info_label = Label(tk, text="Жми кнопку ниже", font=("Arial", 20), wraplength=350)
info_label.pack(pady=30)

def messege():
    # 2. Вместо print используем .config, чтобы изменить текст в Label
    info_label.config(text='Короче, я хотел сказать, что это начало того, что я хочу создать мессенджер или учавствовать в Недохакерс с полного нуля сам!')

btn = Button(tk, text='!нажми!', font=("Arial", 15), command=messege)
btn.pack()

tk.mainloop()
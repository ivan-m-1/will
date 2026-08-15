from tkinter import *
tk = Tk()

canvas = Canvas(tk, width=400, height=400)
canvas.pack()
canvas.create_line(0,0,500,500)
canvas.create_rectangle(10,10,50,50)

def messege():
    print('Короче, я хотел сказать чтоэто начало того что я хочу создать мессенджер с полного нуля сам!')

btn = Button(tk, text='!нажми!', command=messege)
btn.pack()







tk.mainloop()
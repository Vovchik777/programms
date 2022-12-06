from tkinter import *
import random
tochka=input('Введите * чтобы начать играть')
while tochka !='.':
    while True:
        window = Tk()
        window.title('Работа с canvas')
        canvas = Canvas(window, width=400, height=400, bg="gray", cursor="pencil")

        canvas.create_line(0, 200, 400, 200, width=5, fill="yellow")

        # canvas.create_line(400, 400, 0, 0, width=5, fill="yellow")
        # canvas.create_line(0, 400, 400, 0, width=5, fill="yellow")
        # canvas.create_line(0, 400, 150, 50, width=5, fill="yellow")
        # canvas.create_line(400, 400, 200, 50, width=5, fill="yellow")
        # canvas.create_line(400, 0, 150, 100, width=5, fill="yellow")
        # canvas.create_line(0, 400, 200, 100, width=5, fill="yellow")
        canvas.create_rectangle(150,0,250,50,fill='red')#,150,100,200,50)
        canvas.create_rectangle(150,350,250,400,fill='blue')#,150,100,200,50)
        x=random.randint(0,400)
        y=random.randint(0,200)
        canvas.create_rectangle(x, y, x, y, width=5, fill="blue",outline='blue')
        if x >150 and x <250 and y >0 and y < 50:
            canvas.create_text(50, 250, text="Попал ", font="Verdana 12", justify=CENTER, fill="blue")
            canvas.update()
            canvas.pack()
            window.mainloop()
            break
        x2=random.randint(0,400)
        y2=random.randint(200,400)
        canvas.create_rectangle(x2, y2, x2, y2, width=5, fill="red",outline='red')
        if x2 > 150 and x2 <250 and y2>350 and y2 <400:
            canvas.create_text(50, 150, text="Попал ", font="Verdana 12", justify=CENTER, fill="red")
            canvas.update()
            canvas.pack()
            window.mainloop()
            break
        # canvas.create_rectangle(150,50,200,100,fill='red')#,150,100,200,50)
        #
        # canvas.create_rectangle(150,350,200,300,fill='blue')#,150,300,200,350)
        # for i in range(0,2):
        #     canvas.create_text(350, 250, text="", font="Verdana 12", justify=CENTER, fill="blue")
        #     canvas.create_text(350,250,text=f"{i}",  font="Verdana 12",justify=CENTER,fill="blue")

        canvas.update()
        canvas.pack()
        window.mainloop()
    window = Tk()
    window.title('Работа с canvas')
    canvas = Canvas(window, width=1000, height=1000, bg="gray", cursor="pencil")
    canvas.create_text(200, 200, text="Конец игры", font="Verdana 12", justify=CENTER, fill="blue")
    canvas.create_text(200, 250, text="Чтобы продолжить играть напишите * чтобы закончить напишите .", font="Verdana 12", justify=CENTER, fill="blue")
    canvas.pack()
    window.mainloop()
    tochka = input()

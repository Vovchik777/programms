from tkinter import *
window = Tk()
window.title('Работа с canvas')
canvas = Canvas(window,width=600,height=600,bg="gray", cursor="pencil")
#canvas.create_rectangle(50,250,300,500,fill="white",outline="blue")
for r in range(200,49,-5):
    canvas.create_oval([300+r,300+r],[300-r,300-r])
canvas.pack()
window.mainloop()


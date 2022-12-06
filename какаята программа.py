from tkinter import *
import math
man = 0
x = [x/10 for x in range(0,400)]
y = [y/10 for y in range(200,400)]
window = Tk()
window.title('Работа с canvas')
canvas = Canvas(window, width=400, height=400, bg="gray", cursor="pencil")
canvas.create_line(0,200,400,200 )
for y2, in y:
    canvas.create_line([math.sin(),math.sin(y2)],[400,y])
canvas.update()
canvas.pack()
window.mainloop()
# for i in range(0,12):
#     print(math.ceil(math.sin(x[man])*100))
#     man += 1
#
# #x = int(input('Ввeдите данные:\b'))
#for x in range(0,6,1):

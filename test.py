from tkinter import *
window = Tk()
window.title('Работа с canvas')
canvas = Canvas(window,width=600,height=600,bg="gray", cursor="pencil")

# canvas.create_line(0,0,600,600,width=5,fill="red")
# canvas.create_line(0,600,600,0,width=5,fill="black")
# canvas.create_line(300,0,300,600,width=1,fill="green")
# for i in range(0, 600, 2):
#     canvas.create_line(0, 0, i, 600, width=1, fill="green")
#     canvas.create_line(600, 0, i, 600, width=1, fill="red")
#     canvas.create_line(600, 600, 0,i, width=1, fill="yellow")
#     canvas.create_line(600, 600, i ,0, width=1, fill="black")
# #canvas.create_line(10,0,300,600,width=5,fill="green")
# # canvas.create_line(0,600,600,0,width=5,fill="yellow")
# # canvas.create_rectangle(50,250,300,500,fill="white",outline="blue")
canvas.create_oval([400,250],[450,300],fill="pink")
# #canvas.create_polygon([0,600],[0,0],[600,0],fill="red", outline="red")
# #canvas.create_polygon([0,600],[300,300],[600,600],fill="white", outline="white")
# # canvas.create_text(250,280,text="Текст в canvas",  font="Verdana 12",justify=CENTER,fill="red")


canvas.pack()
window.mainloop()

# a = float(input("Длина верха:\n"))
# b = float(input("Длина низа:\n"))
# h = float(input('Высота:\n'))
# print('S=' + str(0.5 * (a + b) * h))

# a=float(input("A?"))
# b =float( input("B?"))
# if (a<0.01) or b<0.01 :
#     print("напиши число побольше")
# else:
#     p= a*b
#     s=p/2
#     print("S прямоугольного треугольника равна "+str(s))



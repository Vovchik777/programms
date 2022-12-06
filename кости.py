from tkinter import *


root = Tk()
root.geometry('400x200')
root.title('Игра в кости')
root.resizable(height=False,width=False)
root.iconphoto(True, PhotoImage(file='b1-5.png'))
font = PhotoImage(file='holst.png')
Label(root,image=font).pack()

root.mainloop()
from tkinter import *

root = Tk()
root.title("Nado GUI") #gui 이름 설정

label1 = Label(root, text="안녕하세요")
label1.pack()

photo = PhotoImage(file="gui_basic/img.png")
label2 = Label(root, width = 30, height = 30, image=photo)
label2.pack()

global photo2
photo2 = PhotoImage(file = "gui_basic/img2.png")
label2.config(image = photo2)

def change():
    label1.config(text="또만나요")


btn = Button(root, text="클릭", command = change)
btn.pack()


root.mainloop()
from tkinter import *

root = Tk()
root.title("Nado GUI") #gui 이름 설정

btn1 = Button(root, text="버튼1")
btn1.pack()  #버튼 호출

btn2 = Button(root, padx=5, pady=10, text="버튼2")
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼3")  # padx = 양옆 여백, pady = 위아래 여백 (크기 유동적)
btn3.pack()

btn4 = Button(root, width=10, height=3, text="버튼4") # 버튼 가로 세로 높이 지정 (고정 크기)
btn4.pack()

btn5 = Button(root, highlightbackground='yellow', text="버튼5") # foreground(글자색), background(배경색)
btn5.pack()

photo = PhotoImage(file="gui_basic/img.png")
btn6 = Button(root, image=photo)
btn6.pack()

def btncmd():
    print("버튼이 클릭되었어요.")
btn7 = Button(root, text="동작하는 버튼", command=btncmd)
btn7.pack()





root.mainloop()

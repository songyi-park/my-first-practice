from tkinter import *

root = Tk()
root.title("Nado GUI") #gui 이름 설정
root.geometry("640x480+300+100") #가로 x 세로 + x좌표 + y좌표

label1 = Label(root, text="메뉴를 선택하세요")
label1.pack()

burger_var = IntVar()
btn_burger1 = Radiobutton(root, text = "햄버거", value=1, variable=burger_var)
# btn_burger1.select() : 초기 선택
btn_burger2 = Radiobutton(root, text = "치즈버거", value=2, variable=burger_var)
btn_burger3 = Radiobutton(root, text = "치킨버거", value=3, variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

label2 = Label(root, text="음료를 선택하세요")
label2.pack()

dring_var = StringVar()
btn_drink1 = Radiobutton(root, text = "콜라", value="콜라", variable=dring_var)
btn_drink1.select() # 초기 버튼 선택을 의미
btn_drink2 = Radiobutton(root, text = "사이다", value="사이다", variable=dring_var)

btn_drink1.pack()
btn_drink2.pack()

def btncmd():
    print (burger_var.get())
    print (dring_var.get())

btn = Button(root, text="주문", command=btncmd)
btn.pack()

root.mainloop()
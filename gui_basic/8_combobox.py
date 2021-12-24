import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Nado GUI") #gui 이름 설정
root.geometry("640x480+300+100") #가로 x 세로 + x좌표 + y좌표

values = [str(i) + "일" for i in range(1, 32)]
combobox = ttk.Combobox(root, height=5, values=values, state="readonly") # 읽기 전용 상태
combobox.pack()
combobox.set("카드 결제일") # 목록 제목 설정

def btncmd():
    print(combobox.get())


btn = Button(root, text="선택", command=btncmd)
btn.pack()

root.mainloop()
import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Nado GUI") #gui 이름 설정
root.geometry("640x480+300+100") #가로 x 세로 + x좌표 + y좌표

# mode = indeterminate 가늠할 수 없는 , determinate 확실한
p_var2 = DoubleVar() # 소수점이 있는 숫자
progressbar = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
#progressbar.start(10) # 10ms 마다 움직임
progressbar.pack()

def btncmd():
    for i in range(1, 101):
        time.sleep(0.01)  #0.01초 대기

        p_var2.set(i) # 프로그레스바의 값 설정
        progressbar.update() # ui 업데이트 
        print(p_var2.get())

btn = Button(root, text="시작", command=btncmd)
btn.pack()

root.mainloop()
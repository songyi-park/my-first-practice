from tkinter import *

root = Tk()
root.title("Nado GUI") #gui 이름 설정
root.geometry("640x480+300+100") #가로 x 세로 + x좌표 + y좌표

listbox = Listbox(root, selectmode="extended", height=0) 
#selectmode = "single"인 경우 하나만 선택가능
#height=0 이 디폴트값, 다보여줌.
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박")
listbox.insert(END, "포도")
listbox.pack()


def btncmd():
    pass
    # # 삭제
    # listbox.delete(0)
    
    # # 갯수 확인
    # print("리스트에는", listbox.size(), "개가 있어요.")

    # # 항목 확인 (시작 idx, 끝 idx)
    # print("1번째부터 3번째까지의 항목 : ", listbox.get(0, 2))

    # # 선택된 항목 확인 (현재 위치로 반환 ex. (1, 2, 3))
    # print("선택된 항목 :", listbox.curselection())

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()
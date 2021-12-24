from tkinter import *

root = Tk()
root.title("Nado GUI") #gui 이름 설정
root.geometry("640x480+300+100") #가로 x 세로 + x좌표 + y좌표

def create_new_file():
    print("새 파일을 만듭니다.")

menu = Menu(root)

menu_file = Menu(menu, tearoff = 0)
menu_file.add_command(label="New File", command=create_new_file)
menu_file.add_command(label="New Window")
menu_file.add_separator() #구분자 -----
menu_file.add_command(label = "Open File...")
menu_file.add_separator()
menu_file.add_command(label = "Save All", state="disable") #비활성화
menu_file.add_separator()
menu_file.add_command(label = "Exit", command=root.quit) #창나가기
menu.add_cascade(label = "File", menu = menu_file)

menu_edit = Menu(menu, tearoff= 0)
menu.add_cascade(label="Edit", menu = menu_edit)

menu_lang = Menu(menu, tearoff= 0)
menu_lang.add_radiobutton(label = "Python")
menu_lang.add_radiobutton(label="Java")
menu_lang.add_radiobutton(label = "C++")

menu.add_cascade(label="Language", menu=menu)


root.config(menu=menu)
root.mainloop()
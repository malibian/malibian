import tkinter as tk
import time
from pynput.mouse import Listener,Controller, Button


def button_click():
    label.config(text="버튼이 클릭되었습니다!")
def button_lecord():
    def on_click(x, y, button, pressed):
        if pressed:
            label.config(text=f"마우스 좌표: ({x}, {y})")
            listener.stop()
            return x,y
    label.config(text="좌표 지정 모드입니다. 클릭해주세요.")
    listener = Listener(on_click=on_click)
    listener.start()

def execute_mouse_click(x, y):
    mouse = Controller()
    mouse.position = (x, y)
    mouse.press(Button.left)
    time.sleep(1)  # 클릭을 원하는 시간 (초)
    mouse.release(Button.left)
    

# 윈도우 생성
window = tk.Tk()

# 윈도우 제목 설정
window.title("윈도우 창")

# 윈도우 크기 설정
window.geometry("400x300")

# 라벨 생성
label = tk.Label(window, text="안녕, 윈도우!")
label.pack()

#버튼 생성
button = tk.Button(window,text="클릭하세요!", command=button_click)
button.pack()

record_button = tk.Button(window,text="좌표를 지정합니다", command=button_lecord)
record_button.pack()

on_click_button = tk.Button(window,text="위치 확인", command=execute_mouse_click)
on_click_button.pack()



# 윈도우 실행
window.mainloop()


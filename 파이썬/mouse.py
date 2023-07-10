import tkinter as tk
from pynput.mouse import Controller as MouseController

def set_coordinate():
    label.config(text="좌표를 지정하세요.")
    window.unbind("<Button-1>")
    window.bind("<Button-1>", on_click)

def on_click(event):
    global coordinate
    coordinate.set(f"({event.x_root}, {event.y_root})")
    label.config(text="좌표가 지정되었습니다.")
    window.unbind("<Button-1>")
    auto_mouse_button.config(state=tk.NORMAL)

def start_auto_mouse():
    label.config(text="오토마우스가 시작되었습니다.")
    window.unbind("<Button-1>")
    auto_mouse_button.config(state=tk.DISABLED)
    window.bind("<Escape>", stop_auto_mouse)
    auto_click(coordinate.get())

def stop_auto_mouse(event):
    if event.keysym == "Escape":
        label.config(text="오토마우스가 종료되었습니다.")
        window.unbind("<Escape>")
        auto_mouse_button.config(state=tk.NORMAL)

def auto_click(coordinate):
    mouse = MouseController()
    x, y = coordinate.split(",")
    x = int(x.strip()[1:])
    y = int(y.strip()[:-1])
    mouse.position = (x, y)
    mouse.click(button="left")
    window.after(1000, auto_click, coordinate)

# 윈도우 생성
window = tk.Tk()
window.title("오토마우스")

# 라벨 생성
label = tk.Label(window, text="안녕하세요. 오토마우스입니다.")
label.pack()

# 좌표 지정 버튼
set_coordinate_button = tk.Button(window, text="좌표를 지정하세요", command=set_coordinate)
set_coordinate_button.pack()

# 오토마우스 시작 버튼
auto_mouse_button = tk.Button(window, text="오토마우스를 시작합니다", command=start_auto_mouse, state=tk.DISABLED)
auto_mouse_button.pack()

# 좌표 변수
coordinate = tk.StringVar()

# 좌표 라벨
coordinate_label = tk.Label(window, textvariable=coordinate)
coordinate_label.pack()

# 윈도우 실행
window.mainloop()



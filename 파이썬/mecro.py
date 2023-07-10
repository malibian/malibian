from pynput.mouse import Listener, Button, Controller
import time

mouse = Controller()
coordinates=[]

def on_click(x, y, button, pressed):
    if button == Button.left and pressed:
        # 좌클릭이 발생한 경우 좌표를 추가합니다.
        coordinates.append((x, y))
        print(f"좌표 추가: ({x}, {y})")
    elif button == Button.right and pressed:
        # 우클릭이 발생한 경우 리스너를 멈춥니다.
        print("클릭 기능을 멈춥니다.")
        return False
# 마우스 이벤트 리스너 생성
listener = Listener(on_click=on_click)
listener.start()

# 리스너가 종료될 때까지 대기
listener.join()

# 찍힌 좌표 출력
print("찍힌 좌표:")
for coord in coordinates:
    print(coord)
click_x = coord[0]
click_y = coord[1]
mouse.position = (click_x,click_y)
mouse.click(Button.left)
time.sleep(5)


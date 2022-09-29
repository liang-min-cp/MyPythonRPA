import time

import pyautogui

if __name__ == '__main__':
    x_old, y_old = 0, 0
    while True:

        x, y = pyautogui.position()
        if x_old != x or y_old != y:
            print(x, y)
            x_old, y_old = x, y
            time.sleep(0.5)

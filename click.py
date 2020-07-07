import win32api
import win32con
import time
import ctypes


def key_down_up(num):
    if isinstance(num, str):
        num = int(num)

    MapVirtualKey = ctypes.windll.user32.MapVirtualKeyA
    time.sleep(0.4)
    win32api.keybd_event(num, MapVirtualKey(num, 0), 0, 0)
    time.sleep(0.2)
    win32api.keybd_event(num, MapVirtualKey(
        num, 0), win32con.KEYEVENTF_KEYUP, 0)


if __name__ == '__main__':
    num = input('>> ')
    print(f'NUM is: {num}')
    for j in range(10):
        key_down_up(num)
        time.sleep(1)

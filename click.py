import time
import ctypes
import win32api
import win32con
import threading


def key_down_up(num):
    if isinstance(num, str):
        num = int(num)

    MapVirtualKey = ctypes.windll.user32.MapVirtualKeyA
    # time.sleep(0.4)
    win32api.keybd_event(num,
                         MapVirtualKey(num, 0),
                         0,
                         0)
    # time.sleep(0.1)
    win32api.keybd_event(num,
                         MapVirtualKey(num, 0),
                         win32con.KEYEVENTF_KEYUP,
                         0)


class KeyPresser():
    def __init__(self, num, interval=3):
        self.num = num
        self.interval = interval
        self.stop = False

    def stop_pressing(self):
        self.stop = True

    def start_pressing(self):
        self.stop = False
        thread = threading.Thread(target=self.repeat_pressing)
        thread.start()

    def repeat_pressing(self):
        print(f'Start pressing {self.num} every {self.interval} seconds.')
        while True:
            if self.stop:
                break
            key_down_up(self.num)
            time.sleep(self.interval)
        print(f'Stop pressing {self.num} every {self.interval} seconds.')


# if __name__ == '__main__':
#     num = input('>> ')
#     print(f'NUM is: {num}')
#     for j in range(10):
#         key_down_up(num)
#         time.sleep(1)

if __name__ == '__main__':
    kps = [KeyPresser(num=49, interval=2),  # 1
           KeyPresser(num=50, interval=3),  # 2
           KeyPresser(num=51, interval=2),  # 3
           #    KeyPresser(num=52, interval=4),  # 4
           ]

    while True:
        input('Press enter to start')
        for kp in kps:
            kp.start_pressing()
            time.sleep(0.2)

        c = input('Press enter to stop')
        for kp in kps:
            kp.stop_pressing()

        if 'q' in c:
            break

    print('Done.')

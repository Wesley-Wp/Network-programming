import threading
import time


class MyThread(threading.Thread):
    def run(self):
        self.login()
        for i in range(3):
            time.sleep(1)
            msg = "I'm" + self.name + '@' + str(i)
            print(msg)

    def login(self):
        print("这是登录.........")


if __name__ == '__main__':
    t = MyThread()
    t.start()

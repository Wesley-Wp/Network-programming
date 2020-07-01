from greenlet import greenlet
import time


def task_A():
    while True:
        print("----A----")
        gr2.switch()
        time.sleep(0.5)


def task_B():
    while True:
        print("----B----")
        gr1.switch()
        time.sleep(0.5)


gr1 = greenlet(task_A)
gr2 = greenlet(task_B)

gr1.switch()

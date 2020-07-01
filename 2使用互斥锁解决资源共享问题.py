import threading
import time

# 定义一个全局变量
g_num = 0


def test1(num):
    global g_num
    # 上锁  如果在上锁之前，没有上锁，那么此时上锁成功，如果上锁之前已经被上锁了，那么会堵塞在这个位置，知道这个锁被解开
    mutex.acquire()
    for i in range(num):
        g_num += 1
    mutex.release()
    print("--------test1 g_num =%d------" % g_num)


def test2(num):
    global g_num
    mutex.acquire()
    for i in range(num):
        g_num += 1
    mutex.release()
    print("------test g_num = %d-------" % g_num)


# 创建一个互斥锁
mutex = threading.Lock()


def main():
    t1 = threading.Thread(target=test1, args=(100000,))
    t2 = threading.Thread(target=test2, args=(100000,))

    t1.start()
    t2.start()

    time.sleep(5)

    print("main thread g_num = %d" % g_num)


if __name__ == '__main__':
    main()

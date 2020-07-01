import socket


def socket_use():
    # 创建套接字
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        # 发送数据
        send_data = input("请输入发送的数据：")
        if send_data == "exit":
            break
        # 使用套接字收发数据
        s.sendto(send_data.encode("gbk"), ("192.168.1.105", 8080))  # Windows编码使用的是gbk方式
    # 关闭套接字
    s.close()


if __name__ == '__main__':
    socket_use()

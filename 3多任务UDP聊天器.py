from socket import *
import threading
import time


def recv_msg(udp_socket):
    """接收数据"""
    while True:
        recv_data = udp_socket.recvfrom(1024)
        print(recv_data)


def send_msg(udp_socket, dest_ip, dest_port):
    """发送数据"""
    while True:
        send_data = input("输入要发送的数据：")
        udp_socket.sendto(send_data.encode("utf-8"), (dest_ip,dest_port))


def main():
    """完成udp聊天器的完整控制"""
    # 创建套接字
    udp_socket = socket(AF_INET, SOCK_DGRAM)

    # 绑定本地西信息
    udp_socket.bind(("", 7890))

    # 获取对方的IP和port
    dest_ip = input("输入对方的IP：")
    dest_port = int(input("输入对方的port："))

    # 创建线程，执行相应的控制
    t_recv = threading.Thread(target=recv_msg, args=(udp_socket,))
    t_send = threading.Thread(target=send_msg, args=(udp_socket, dest_ip, dest_port,))

    t_recv.start()
    t_send.start()


if __name__ == '__main__':
    main()

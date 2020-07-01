from socket import *


def send_msg(udp_socket):
    """发送数据"""
    # 获取对方的地址和端口
    dest_ip = input("请输入对方的IP：")
    dest_port = int(input("输入对方的port："))
    send_data = input("请输入发送的数据：")
    udp_socket.sendto(send_data.encode("gbk"),(dest_ip, dest_port))



def recv_msg(udp_socket):
    """接收数据"""
    recv_data = udp_socket.recvfrom(1024)
    print("%s:%s" % (str(recv_data[1]),recv_data[0].decode("gbk")))


def main():
    # 创建套接字
    udp_socket = socket(AF_INET, SOCK_DGRAM)
    # 绑定地址和端口
    udp_socket.bind(("", 7788))
    # 使用循环处理事件
    while True:
        # 发送数据
        send_msg(udp_socket)
        # 接收数据
        recv_msg(udp_socket)



if __name__ == '__main__':
    main()
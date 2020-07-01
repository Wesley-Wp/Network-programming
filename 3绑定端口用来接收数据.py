from socket import *


def main():
    # 创建套接字
    udp_socket = socket(AF_INET, SOCK_DGRAM)
    # 绑定一个本地信息
    localdress = ("", 7788)
    udp_socket.bind(localdress)
    while True:
        # 接收数据
        recv_data = udp_socket.recvfrom(1024)
        recv_msg = recv_data[0]  # 存储接收的数据
        send_adree = recv_data[1]  # 存储发送方的地址信息
        # 打印接收到的数据
        print("%s:%s"%(str(send_adree),recv_msg.decode("gbk")))  # windows解码使用的还gbk
    # 关闭套接字
    udp_socket.close()


if __name__ == '__main__':
    main()

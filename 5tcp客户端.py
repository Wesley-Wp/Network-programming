from socket import *


def main():
    # 创建套接字
    tcp_socket = socket(AF_INET, SOCK_STREAM)

    # 连接服务器
    serve_ip = input("请输入IP：")
    serve_port = int(input("请输入port："))
    localadree = (serve_ip, serve_port)
    tcp_socket.connect(localadree)

    # 发送数据/接收数据
    send_data = input("请输入要发送的数据：")
    tcp_socket.send(send_data.encode("gbk"))

    # 关闭套接字
    tcp_socket.close()


if __name__ == '__main__':
    main()

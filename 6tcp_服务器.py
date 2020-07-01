from socket import *

def main():
    # 创建套接字
    tcp_sever_socket = socket(AF_INET, SOCK_STREAM)

    # 绑定本地信息
    tcp_sever_socket.bind(("", 7890))

    # 让默认的套接字有主动变为被动listen
    tcp_sever_socket.listen(128)

    # 等待客户端的链接 accept
    new_client_socket, new_client_addr = tcp_sever_socket.accept()

    # 接收客户端发过来的数据
    recv_data = new_client_socket.recv(1024)
    print(recv_data)

    # 回复一些数据给客户端
    new_client_socket.send("hahah----ok---".encode("utf-8"))

    # 关闭套接字
    new_client_socket.close()
    tcp_sever_socket.close()


if __name__ == '__main__':
    main()
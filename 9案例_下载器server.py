from socket import *


def send_file2client(new_client_socket, new_client_addr):
    # 接收客户端发过来要下载的文件名
    file_name = new_client_socket.recv(1024).decode("utf-8")
    print("客户端（%s)需要下载的文件名是：%s" % (str(new_client_addr), file_name))
    file_conent = None
    # 打开这个文件，读取数据
    try:
        f = open(file_name, "rb")
        file_conent = f.read()
        f.close()
    except Exception as ret:
        print("没有要下载的文件（%s）" % file_name)
        # 发送文件数据给客户端
        if file_conent:
            new_client_socket.send(file_conent)


def main():
    # 创建套接字
    tcp_sever_socket = socket(AF_INET, SOCK_STREAM)

    # 绑定本地信息
    tcp_sever_socket.bind(("", 7890))

    # 让默认的套接字有主动变为被动listen
    tcp_sever_socket.listen(128)
    while True:
        # 等待客户端的链接 accept
        new_client_socket, new_client_addr = tcp_sever_socket.accept()
        send_file2client(new_client_socket, new_client_addr)

        # 发送文件数据给客户端
        new_client_socket.send("hahah----ok---".encode("utf-8"))

        # 关闭套接字
        new_client_socket.close()
    tcp_sever_socket.close()


if __name__ == '__main__':
    main()

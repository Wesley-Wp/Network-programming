from socket import *

def main():
    # 创建套接字
    tcp_socket = socket(AF_INET, SOCK_STREAM)

    # 获取服务器的IP和port
    dest_ip = input("请输入IP：")
    dest_port = int(input("请输入port："))

    # 链接服务器
    tcp_socket.connect((dest_ip,dest_port))

    # 获取下载的文件名字
    download_file_name = input("需要下载的文件名字：")

    # 将文件发送到服务器
    tcp_socket.send(download_file_name.encode("utf-8"))

    # 接收文件中的数据
    recv_data = tcp_socket.recv(1024)
    if recv_data:
        # 保存接收到的数据到另外一个文件夹
        with open("[新]" + download_file_name, "wb") as f:
            f.write(recv_data)
    # 关闭套接字
    tcp_socket.close()


if __name__ == '__main__':
    main()
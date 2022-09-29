import socket


class tcp_client:
    def __init__(self, ip_am3352: str, port_am3352: int):
        self.Ip_am3352 = ip_am3352
        self.Port_am3352 = port_am3352
        self.Client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def Connect(self):
        self.Client.connect((self.Ip_am3352, self.Port_am3352))

    def Send(self, send_message):
        self.Client.send(send_message.encode("utf-8"))

    def Receive(self):
        message = self.Client.recv(1024)
        return message

    def Close(self):
        self.Client.close()


if __name__ == "__main__":

    # 创建一个socket对象
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = "127.0.0.1"
    port = 9999
    # 连接服务端
    client.connect((host, port))

    while True:
        send_msg = input("发送: ")
        # 设置退出条件
        if send_msg == "q":
            break
        send_msg = send_msg
        # 发送数据，编码
        client.send(send_msg.encode("utf-8"))
        # 接收服务端返回的数据
        msg = client.recv(1024)
        # 解码
        print("接收：" + msg.decode("utf-8"))
    # 关闭客户端
    client.close()

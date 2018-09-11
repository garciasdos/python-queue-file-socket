from socket import AF_INET, SOCK_STREAM, socket
import multiprocessing, queue, time, sys

class Server:

    def __init__(self, port=5011, host="localhost", bufsize=1024):
        """Initialization function"""
        self.port = port
        self.host = host
        self.buf_size = bufsize
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.q = queue.Queue()

    def __get_port(self):
        return self.port

    def __get_host(self):
        return self.host

    def __get_queue(self):
        return self.q

    def __get_addr(self):
        return (self.host, self.port)

    def __get_socket(self):
        return self.socket

    def __get_buf_size(self):
        return self.buf_size

    def __set_client_addr_sender(self, client_addr_sender):
        self.client_addr_sender = client_addr_sender

    def __set_client_addr_receiver(self, client_addr_receiver):
        self.client_addr_receiver = client_addr_receiver

    def __get_client_addr_sender(self):
        return self.client_addr_sender

    def __get_client_addr_receiver(self):
        return self.client_addr_receiver


    def close_sock(self):
        self.__get_socket().close()

    def handle_connections(self):
        socket = self.__get_socket()
        socket.bind(self.__get_addr())
        socket.listen(2)
        print("Waiting for sender...")
        client, client_addr_sender = socket.accept()
        self.__set_client_addr_sender(client_addr_sender)
        print("%s:%s has connected as sender." % client_addr_sender)

        while True:

            msg = client.recv(self.__get_buf_size()).decode("utf8")
            self.put_message_on_queue(msg)
            if msg == "":
                # socket.close()
                break

        print("Waiting for receiver...")
        socket.listen(20)
        receiver, client_addr_receiver = socket.accept()
        self.__set_client_addr_receiver(client_addr_receiver)
        print("%s:%s has connected as receiver." % client_addr_receiver)

        self.send_data(receiver)


    def put_message_on_queue(self, message):
        que = self.__get_queue()
        que.put(message)

    def send_data(self, receiver):
        sock = self.socket
        que = self.__get_queue()
        while not que.empty():
            message = que.get()
            try:
                receiver.send(bytes(message, "utf8"))
            except ValueError:
                print("Can't send message to %s" % receiver)
                sock.close()
                sys.exit(1)
        sock.close()


if __name__ == '__main__':

    port = int(input("Port?: [default 5011]") or "5011")
    host = str(input("Host?: [default localhost]") or "localhost")
    bufsize = int(input("Buffer Size?: [default 1024]") or "1024")

    server = Server(port=port, host=host, bufsize=bufsize)
    server.handle_connections()

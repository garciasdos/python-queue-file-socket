from socket import AF_INET, SOCK_STREAM, socket
import multiprocessing, queue, time, sys

class Client:
    def __init__(self, mode, port=5011, host="localhost", filename="begin.txt", bufsize = 1024):
        """Initialization function"""
        self.port = port
        self.host = host
        self.file = open(filename, mode=mode)
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.buf_size = bufsize

    def __get_port(self):
        return self.port

    def __get_host(self):
        return self.host

    def __get_file(self):
        return self.file

    def __get_addr(self):
        return (self.host, self.port)

    def __get_socket(self):
        return self.socket

    def __get_buf_size(self):
        return self.buf_size

    def connect(self):
        """Method to connect to Server"""
        sock = self.__get_socket()
        try:
           sock.connect(self.__get_addr())
           print("Connected to %s:%s" % self.__get_addr())
        except ConnectionError:
            print("Can't establish connexion to %s:%s" % self.__get_addr())
            sys.exit(1)

    def send(self):
        """Method that takes message from line file and send it to server"""
        sock = self.__get_socket()
        with self.__get_file() as f:
            for line in f:
                msg = line
                print("Sending line %s" % msg)
                try:
                    sock.send(bytes(msg, "utf8"))
                except ConnectionError:
                    print("Couldn't send message %s. Exiting program..." % msg)
                    sys.exit(1)
                time.sleep(0.2)
        sock.close()
        self.__get_file().close()

    def receive(self):
        """Method that receives message from queue server and put it into file"""
        sock = self.__get_socket()
        try:
            msg = sock.recv(self.__get_buf_size()).decode("utf8")
        except ConnectionError:
            print("Can't write to file, possibly bad connection")
            sys.exit(1)
        while msg != "":
            try:
                self.__get_file().write(msg)
                print("%s wrote on file %s" % (msg, self.__get_file().__getattribute__("name")))
            except ValueError:
                print("Can't write to file, check permissions or file mode")

            msg = sock.recv(self.__get_buf_size()).decode("utf8")
        self.__get_file().close()


if __name__ == '__main__':

    port = int(input("Port?: [default 5011]") or "5011")
    host = str(input("Host?: [default localhost]") or "localhost")
    filename = str(input("filename?: [default begin.txt]") or "begin.txt")
    client_type = input("Sender or receiver? [S/R]")

    while client_type != "S" and client_type != "R":
        client_type = input("Sender or receiver? [S/R]")

    if client_type == "S":

        client = Client(mode="r", port=port, host=host, filename=filename)
        client.connect()
        client.send()

    elif client_type == "R":
        client = Client(mode="w", port=port, host=host, filename=filename)
        client.connect()
        client.receive()
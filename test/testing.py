import unittest
import sys, multiprocessing, time
sys.path.insert(0, 'src')
import client
import server as servertest


class ServerClientTest(unittest.TestCase):
    def test_server_init_port(self):
        server = servertest.Server(port=5001)
        server.close_sock()
        self.assertEqual(server.__getattribute__("port"), 5001)

    def test_server_init_host(self):
        server = servertest.Server(host="localhost")
        server.close_sock()
        self.assertEqual(server.__getattribute__("host"), "localhost")


    def test_server_init_buf_size(self):
        server = servertest.Server(bufsize=1024)
        server.close_sock()
        self.assertEqual(server.__getattribute__("buf_size"), 1024)


    def test_files_equals(self):
        # server = servertest.Server(port=5555)
        # server.handle_connections()
        service_ = servertest.Server(port=5555)

        service = multiprocessing.Process(name="test_server", target=service_.handle_connections, args=(service_, ))

        service.start()

        sender = client.Client(mode="r", port=5555, filename="begin.txt")
        sender.connect()
        client_sender = multiprocessing.Process(name="test_sender", target=sender.send)
        client_receiver = multiprocessing.Process(name="test_receiver", target=client.Client.connect.receive, args=("mode=\"w\", port=5555, filename=\"end_test.txt\"", ))


        # service
        client_sender.start()
        client_sender.join()
        client_receiver.start()
        client_receiver.join()

        # client_sender = client.Client(mode="r", filename="begin.txt")
        # client_sender.connect()
        # client_sender.send()

        # client_receiver = client.Client(mode="w", filename="end_test.txt")
        # client_receiver.connect()
        # client_receiver.receive()



        file_begin = open(mode="r", file="begin.txt")
        file_end = open(mode="r", file="end_test.txt")

        self.assertEqual(file_begin.read(), file_end.read())

#    def test_files_equals(self):





if __name__ == '__main__':
    unittest.main()
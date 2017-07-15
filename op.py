import socket
import sys
import threading
import Queue

common_ports = {

    "7": "Echo",
    "21": "ftp",
    "22": "ssh",
    "23": "Telnet",
    "25": "smtp",
    "53": "DNS",
    "79": "Finger",
    "80": "http",
    "110": "POP3",
    "143": "IMAP4",
    "201": "AppleTalk",
    "443": "https",
    "520": "RIP",
    "902": "VMS",
    "1026": "WM"

}
print("enter host:")
host = raw_input()

def is_port_open(host, port):
    try:

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)
        sock.connect((host, port))
    except socket.error:
        return False
    return True


def scan(host):
    while True:
        port = port_queue.get()
        if is_port_open(host, port):
            if str(port) in common_ports:
                print("{}\t\t({})\t\t\tOpen".format(str(port), common_ports[str(port)]))
            else:
                print("{}\t\t\t\t\tOpen".format(port))
        port_queue.task_done()


port_queue = Queue.Queue()
for _ in range(20):
    t = threading.Thread(target=scan, kwargs={"host": host})
    t.daemon = True
    t.start()
for port in range(30000):
    port_queue.put(port)

port_queue.join()

import socket
import sys
import threading
import Queue

common_ports={

          "21":"ftp",
          "22":"ssh",
          "80":"http",
          "443":"https",
          "135":"rk"
    }

def is_port_open(host,port):
    try:
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.settimeout(0.5)
        sock.connect((host,port))
    except socket.error:
        return False
    return True
def scanner(host):
    while True:
        port =port_queue.get()
        if is_port_open(host,port):
            if str(port) in common_ports:
                print("{} is Open".format(str(port),common_ports[str(port)]))
            else:
                print("{} is Open".format(port))
        port_queue.task_done()
port_queue=Queue.Queue()
for _ in range(20):
    t=threading.Thread(target=scanner,kwargs={"host":sys.argv[1]})
    t.daemon=True
    t.start()
for port in range(1024):
    port_queue.put(port)

port_queue.join()


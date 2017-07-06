from threading import Thread
import socket
import subprocess
import os

#host = raw_input('Enter host:  ')
'''from_port = input('start scan from port : ')
to_port = input('finish scan to port :')
counting_open = []
counting_close = []
threads = []'''





def lookup(addr):
     try:
         return socket.gethostbyaddr(addr)
     except socket.herror:
         return None, None, None
def ARP_Scan(ip_add_range):
    with open(os.devnull, "wb") as limbo:
        for n in xrange(1, 50):
                ip=ip_add_range.format(n)


                resul=subprocess.Popen(["ping", "-n", "1", "-w", "200", ip],
                         stdout=limbo, stderr=limbo).wait()
                if  resul:
                     print(ip,"inactive")
                else:
                        name,alias,addresslist = lookup(ip)
                        if name != None:
                            name1 = name
                            print(ip, "active", name1)

                '''            def scan(port):
                                s = socket.socket()
                                result = s.connect_ex((ip, port))

                                for i in range(from_port, to_port + 1):
                                    t = Thread(target=scan, args=(i,))
                                    threads.append(t)
                                    t.start()

                                    [t.join() for t in threads]

                                if result == 0:
                                    counting_open.append(port)
                                    print(ip,"active",name1,(str(port)) + ' :open\n')
                                    s.close()
                                else:
                                    counting_close.append(port)
                                    print(ip,"active",name1,(str(port)) + ' :close\n')
                                    s.close()'''



                           # print (ip, "active",name1,counting_open)



ARP_Scan("10.4.16.{0}")

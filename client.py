# client connection
import socket
host = socket.gethostname()  # as both code is running on same pc

portc= 32451  # socket server port number

client_socket = socket.socket()  # instantiate
client_socket.connect((host, portc))  # connect to the server
client_socket.send("it is nice talking to you\n".encode())



def number_check():
    n = int(input("Enter number of elements : "))
    lst=[]
    for i in range(0, n):
        ele = int(input())
        lst.append(ele) # adding the element
    message= (lst)
 
        # initialize an empty string
    str1 = ' '.join([str(elem) for elem in lst])
    print("your list is :" , lst) 
    client_socket.send(str1.encode())

def client_program():

    message = input(" -> ")  # take input

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response

        print('Server: ' + data)  # show in terminal

        message = input(" -> ")  # again take input

    client_socket.close()  # close the connection


if __name__ == '__main__':
    n = int(input("Enter a number (1) for number option or (2) for server conversation : "))
    if n== 1:
        number_check()
    elif n == 2:
        client_program()
    else:
        print ("Please restart the connection and choose a number")
        client_socket.close()
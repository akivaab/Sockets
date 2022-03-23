from socket import *


def sendMessage():
    server_name = 'hostname'  # replace with IP address of server
    server_port = 12000
    client_socket = socket(AF_INET, SOCK_DGRAM)
    message = getMessage1()  # can replace with getMessage2() or getMessage3()
    client_socket.sendto(message.encode(), (server_name, server_port))
    modified_message, server_address = client_socket.recvfrom(2048)
    print(modified_message.decode())
    client_socket.close()


def getMessage1():
    message = input("Input lowercase sentence: ")
    return message


def getMessage2():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    message = ",".join([str(num1), str(num2)])
    return message


def getMessage3():
    message = input("Input name: ")
    return message


sendMessage()

from socket import *


def send_message():
    server_name = 'hostname'  # replace with IP address of server
    server_port = 12000
    client_socket = socket(AF_INET, SOCK_DGRAM)
    message = get_message1()  # can replace with get_message2() or get_message3()
    client_socket.sendto(message.encode(), (server_name, server_port))
    modified_message, server_address = client_socket.recvfrom(2048)
    print(modified_message.decode())
    client_socket.close()


def get_message1():
    message = input("Input lowercase sentence: ")
    return message


def get_message2():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    message = ",".join([str(num1), str(num2)])
    return message


def get_message3():
    message = input("Input name: ")
    return message


send_message()

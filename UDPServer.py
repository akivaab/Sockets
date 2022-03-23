from socket import *


def receive_message():
    server_port = 12000
    server_socket = socket(AF_INET, SOCK_DGRAM)
    server_socket.bind(('', server_port))
    print("Ready to receive.")
    while True:
        message, client_address = server_socket.recvfrom(2048)
        modified_message = modify_message1(message.decode())  # can replace with modify_message2() or modify_message3()
        server_socket.sendto(modified_message.encode(), client_address)


def modify_message1(message):
    modified_message = message.upper()
    return modified_message


def modify_message2(message):
    numbers = message.split(",")
    num_sum = int(numbers[0]) + int(numbers[1])
    return str(num_sum)


def modify_message3(message):
    names = ["Zero", "One", "Two", "Three", "Four", "Five"]
    numbers = [0, 1, 2, 3, 4, 5]
    index = names.index(message)
    return str(numbers[index])


receive_message()

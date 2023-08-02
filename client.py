from socket import *
import time
# AF_INET - указываем, что сокет сетевой
#SOCK_STREAM - указываем, что сокет потоковый

my_socket = socket(AF_INET,SOCK_STREAM) #создали объект сокет, работающий по протоколу TCP
my_socket.connect(('localhost',888)) #выполняется запрос к серверу
print(f"Бот отвечает на вопросы:\nКоторый час?\nКакой сегодня день?\nКакой день недели был ДД.ММ.ГГ?\nПосчитай [выражение]")
user_input = input("Введите запрос: ")
my_socket.send(user_input.encode('utf-8'))

data_server = my_socket.recv(1024) #принимать не более 1024 байт

print(f"Ответ: {data_server.decode('utf-8')}")

my_socket.close()
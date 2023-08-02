from socket import *
import time, datetime

def handle_request(request):
    request = request.strip().lower()
    if "который час" in request:
        return time.strftime('%H:%M:%S')
    elif "сегодня день" in request:
        days = {
            0: 'Понедельник',
            1: 'Вторник',
            2: 'Среда',
            3: 'Четверг',
            4: 'Пятница',
            5: 'Суббота',
            6: 'Воскресенье'
        }
        weekday = datetime.datetime.now().weekday()
        return days.get(weekday, 'Неизвестный день')

    elif "какой день недели был" in request:
        days = {
            0: 'Понедельник',
            1: 'Вторник',
            2: 'Среда',
            3: 'Четверг',
            4: 'Пятница',
            5: 'Суббота',
            6: 'Воскресенье'
        }
        try:
            date_str = request.replace("какой день недели был", "").strip()
            date_obj = datetime.datetime.strptime(date_str, "%d.%m.%y")
            weekday = date_obj.weekday()
            return days.get(weekday, 'Неизвестный день')
        except Exception as e:
            return "Ошибка при обработке даты."


    elif "посчитай" in request:
        expression = request.replace("посчитай", "")
        result = eval(expression)
        return str(result)
    else:
        return "Извините, я не понимаю ваш запрос."

my_socket = socket(AF_INET,SOCK_STREAM) #создали объект сокет, работающий по протоколу TCP
my_socket.bind(("",888)) #настроили сокет так, чтобы он принимал запросы по локальному
# IP 127.0.0.1 и по порту 8888
my_socket.listen(5) #Переходи8м в режим ожидания запросов и допускаем не более 5 запросов
# одновременно

while True:
    client,addr = my_socket.accept() #принимаем запрос на соединение
    print(f"Получен запрос на коннект по адресу {str(addr)}")

    request = client.recv(1024).decode('utf-8')
    answer = handle_request(request)

    # answer = time.ctime() + "\n" #информация для клиента о времени, когда он сделал коннект к серверу
    client.send(answer.encode('utf-8')) #преобразовали строковый ответ в байты и отправляем ответ клиенту
    client.close() #завершаем работу с клиентом


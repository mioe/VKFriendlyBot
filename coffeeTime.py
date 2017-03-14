import vk
import time
import datetime

# Выводим на экран название программы и автора
print('VKFriendlyBot by mioe')
print('ubuntu-16.04-amd64')
print('---')

# Авторизуем сессию с помощью access токена
session = vk.Session('afc7c4226e7b0dabf250a4af96427d553b76974bec99053c01d1bd47b4f7d172af34781db6b46ee4abe86')

# Создаем объект API
api = vk.API(session)

while (True):
    # Получим 20 последних входящих сообщений
    messages = api.messages.get()

    # Создадим список поддерживаемых команд
    commands = ['help', 'weather']

    # Найдем среди них непрочитанные сообщения с поддерживаемыми командами
    # таким образом получим список в формате [(id пользователя, id сообщения, команда), ..]
    messages = [(m['uid'], m['mid'], m['body'])
                for m in messages[1:] if m['body'] in commands and m['read_state'] == 0]

    # Отвечаем на полученные команды
    for m in messages:
        user_id = m[0]
        messages_id = m[1]
        comand = m[2]

        # Сформируем строку с датой и временем сервера
        date_time_string = datetime.datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')

        if comand == 'help':
            api.messages.send(user_id=user_id,
                              message=date_time_string + '\n>VKFriendlyBot by mioe\n>ubuntu-16.04-amd64\n>---')

        if comand == 'weather':
            api.messages.send(user_id=user_id,
                              message=date_time_string + '\n>Погода отличная!')

    # Формируем список id всех сообщений с командами через запятую
    ids = ', '.join([str(m[1]) for m in messages])

    # Помечаем полученные сообщения как прочитанные
    if ids:
        api.messages.markAsRead(message_ids=ids)

    # Проверяем сообщения каждые 3 секунды
    time.sleep(3)
import vk
import time
import datetime

# Выводим на экран название программы и автора
print('VKFriendlyBot by mioe')
print('ubuntu-16.04-amd64')
print('---')

# Авторизуем сессию с помощью access токена
session = vk.Session('59673b94838bfdf671e6851410f192e7a6cbacd8bed15891684a0a8ca3709d80a40b817e1b0137b1cc3f0')

# Создаем объект API
api = vk.API(session)

points = 0
game = 0

while (True):
    # Получим 20 последних входящих сообщений
    messages = api.messages.get()

    # Создадим список поддерживаемых команд
    commands = ['-v', '-h', '-g', '-y', '-n', '-p', '1', '2', '3', 'next']

    # Найдем среди них непрочитанные сообщения с поддерживаемыми командами
    # таким образом получим список в формате [(id пользователя, id сообщения, команда), ..]
    messages = [(m['uid'], m['mid'], m['body'])
                for m in messages[1:] if m['body'] in commands and m['read_state'] == 0]

    # Отвечаем на полученные команды
    for m in messages:
        user_id = m[0]
        messages_id = m[1]
        comand = m[2]

        if comand == '-v':
            api.messages.send(user_id=user_id, message='FriendlyBot v.001')

        if comand == '-h':
            api.messages.send(user_id=user_id, message='Список комманд:\n'
                                                       '-v - версия бота\n'
                                                       '-h - справочник\n'
                                                       '-g - начало игры')

        if comand == '-g':
            game = 1
            api.messages.send(user_id=user_id, message='WELLCOME TO HELL.PY\n'
                                                        '***\n'
                                                        'Правила игры:\n'
                                                        'Будет задан вопрос, ответь на него!\n'
                                                        '***\n'
                                                        'Ты готов?\n'
                                                        '-y(Да)  -n(Нет)/n')
        if comand == '-n':
            api.messages.send(user_id=user_id, message='ВЫ не готовы!!!\n')
            game = 0

        # Ответы порядок 4-3-2-1
        if (comand == '1' and game == 4):
            api.messages.send(user_id=user_id, message='ТЫ не готов!!!\n')
            points -= 1

        if (comand == '2' and game == 4):
            api.messages.send(user_id=user_id, message='Не удача... ;(\n')
            points -= 2

        if (comand == '3' and game == 4):
            api.messages.send(user_id=user_id, message='Правильно ;) напиши -p для вывода твоего результата\n')
            points += 1

        if (comand == '1' and game == 3):
            api.messages.send(user_id=user_id, message='Правильно ;) для продолжения напиши next\n')
            points += 1
            game = 4

        if (comand == '2' and game == 3):
            api.messages.send(user_id=user_id, message='ТЫ не готов!!!\n')
            points -= 5

        if (comand == '1' and game == 2):
            api.messages.send(user_id=user_id, message='Правильно ;) для продолжения напиши next\n')
            points += 1
            game = 3

        if (comand == '2' and game == 2):
            api.messages.send(user_id=user_id, message='ТЫ не готов!!!\n')
            points -= 2

        if (comand == '3' and game == 2):
            api.messages.send(user_id=user_id, message='Не удача... ;(\n')
            points -= 1

        if (comand == '1' and game == 1):
            api.messages.send(user_id=user_id, message='Правильно ;) для продолжения напиши next\n')
            points += 1
            game = 2

        if (comand == '2' and game == 1):
            api.messages.send(user_id=user_id, message='Не удача... ;(\n')
            points -= 1

        if (comand == '3' and game == 1):
            api.messages.send(user_id=user_id, message='ТЫ не готов!!!\n')
            points -= 2

        # Вывод результата
        if comand == '-p':
            api.messages.send(user_id=user_id, message='И так, ваш балл: ' + str(points) + '/4\n')

        # Вопросы
        if (comand == '-y' and game == 1):
            api.messages.send(user_id=user_id, message='Какие вы знаете логические значения в Python?\n'
                                                       '\n'
                                                       '    1. True and False\n'
                                                       '    2. true and false\n'
                                                       '    3. Truth and Falsity\n')
        if (comand == 'next' and game == 2):
            api.messages.send(user_id=user_id, message='Каким будет результат этой программы?\n'
                                                       'if 1 + 1 == 2:\n'
                                                       'if 2 * 2 == 8:\n'
                                                       'print("if")\n'
                                                       'else:\n'
                                                       'print("else")\n'
                                                       '\n'
                                                       '    1. Не будет выведено ничего\n'
                                                       '    2. else\n'
                                                       '    3. if\n')

        if (comand == 'next' and game == 3):
            api.messages.send(user_id=user_id, message='Каким будет результат этой программы?\n'
                                                       'if 1 + 1 * 3 == 6:\n'
                                                       '--print("Yes")\n'
                                                       'else:\n'
                                                       '--print("No")\n'
                                                       '\n'
                                                       '    1. No\n'
                                                       '    2. Yes\n')

        if (comand == 'next' and game == 4):
            api.messages.send(user_id=user_id, message='Каким будет результат этой программы?\n'
                                                       'x = 4\n'
                                                       'y = 2\n'
                                                       'if not 1 + 1 == y or x == 4 and 7 == 8:\n'
                                                       '--print("Yes")\n'
                                                       'elif:\n'
                                                       '--print("No")\n'
                                                       '\n'
                                                       '    1. Yes\n'
                                                       '    2. Yes No\n'
                                                       '    3. No\n')




    # Формируем список id всех сообщений с командами через запятую
    ids = ', '.join([str(m[1]) for m in messages])

    # Помечаем полученные сообщения как прочитанные
    if ids:
        api.messages.markAsRead(message_ids=ids)

    # Проверяем сообщения каждые 3 секунды
    time.sleep(3)
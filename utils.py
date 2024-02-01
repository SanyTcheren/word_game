import json
import requests
import urllib3

from classes.user import User
from classes.word import GameWord


def get_game_words(url):
    """
    Получение игровых слов
    :param url: путь к серверу JSON
    :return: список игровых слов
    """
    urllib3.disable_warnings()  # отключаем предупреждения об отключении верификации SSL сертификатов
    response = requests.get(url, verify=False)  # отключаем верификацию SSL сертификатов
    # if response.status_code == 200:
    #     print(f'Игровые слова успешно скачаны с {url}')
    data = response.json()
    words = []
    for word in data:
        words.append(GameWord(word['word'], word['subwords']))
    return words


def get_users(path):
    """
    Чтение данных о пользователях
    :param path: путь к JSON файлу
    :return: список пользователей
    """
    with open(path) as fp:
        data = json.load(fp)
        # print(f'Данные пользователей успешно загружены из {path}')
    users = []
    for user in data:
        users.append(User(user['name'], user['words']))
    return users


def put_users(path, users):
    """
    Сохранение данных пользователей в JSON файл
    :param path: путь к файлу
    :param users: список пользователей
    :return:
    """
    data = [user.to_dict() for user in users]
    with open(path, 'w') as fp:
        json.dump(data, fp)
        # print(f'Данные пользователей сохранены в файл {path}')


def get_or_create_user(users, name):
    """
    Поиск по имени либо создание нового пользователя
    :param users: список пользователей
    :param name: имя пользователя
    :return: найденный либо новый пользователь
    """
    user = None
    for item in users:
        if name == item.name:
            user = item
            break
    if user is None:
        user = User(name)
        users.append(user)
    return user

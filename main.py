from utils import get_game_words, get_users, put_users, get_or_create_user
from config import WORDS_URL, USERS_PATH


def main():
    # Определяем пользователя
    name = input('Введите имя игрока\n').title()
    users = get_users(USERS_PATH)
    user = get_or_create_user(users, name)
    print(f'Привет {user.name}!')

    # Определяем игровое слово
    words = get_game_words(WORDS_URL)
    game_word = None
    for word in words:
        if not user.is_guess(word.word):
            game_word = word
            break
    if game_word is None:
        print('Нет новых игровых слов, все слова разгаданы.')
        return

    # Начало игры
    print(f'Составьте {len(game_word.sub_words)} слов из слова {game_word.word.upper()}.')
    print('Слова должны быть не короче 3 букв.')
    print('Чтобы закончить игру, угадайте все слова или напишите "стоп".')
    user_word = input('Поехали, Ваше первое слово?\n').lower()

    # Игровой цикл
    score = 0
    while user_word != 'стоп':
        sub_word = game_word.find_word(user_word)
        if sub_word is None:
            print('Неверно!')
        elif sub_word.is_found():
            print(f'Слово уже найдено!')
        else:
            score += 1
            print(f'Верно! Отгадано слов - {score}')
            sub_word.founded = True
            if game_word.is_solved():
                user.add_word(game_word.word)
                break
        user_word = input().lower()

    # Завершение игры
    print(f'Игра завершена, Вы угадали {score} слов!')
    put_users(USERS_PATH, users)


main()

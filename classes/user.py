class User:
    """Пользователь для игры в слова"""
    def __init__(self, name, words=None):
        """
        :param name: имя пользователя
        :param words: список отгаданных слов
        """
        if words is None:
            words = []
        self.name = name
        self.words = words

    def __repr__(self):
        return f'{self.name}:{self.words}'

    def to_dict(self):
        """Преобразование в словарь"""
        return {
            'name': self.name,
            'words': self.words,
        }

    def add_word(self, word):
        """Добавление слова к отгаданным словам"""
        self.words.append(word)

    def is_guess(self, word):
        """Проверка, является ли слово разгаданным"""
        return word in self.words

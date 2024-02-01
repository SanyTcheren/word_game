class SubWord:
    """Слово, которое может быть составлено из букв другого слова"""
    def __init__(self, word):
        self.word = word
        self.founded = False  # слово еще не найдено

    def __repr__(self):
        return f'{self.word}:{self.founded}'

    def is_found(self):
        """Слово найдено"""
        return self.founded


class GameWord:
    """Игровое слово"""
    def __init__(self, word, sub_words):
        """
        :param word: игровое слово
        :param sub_words: список подслов
        """
        self.word = word
        self.sub_words = []
        for sub_word in sub_words:
            self.sub_words.append(SubWord(sub_word))

    def __repr__(self):
        return f'{self.word}:{self.sub_words}'

    def is_solved(self):
        """Все подслова найдены"""
        for word in self.sub_words:
            if not word.is_found():
                return False
        return True

    def find_word(self, word):
        """Поиск подслова"""
        for sub_word in self.sub_words:
            if word == sub_word.word:
                return sub_word
        return None

import os
from Slovar.settings import BASE_DIR


def get_words():
    dictionary = open(os.path.join(BASE_DIR, 'Perevod/dictionary.txt'), "r", encoding="utf-8").read().splitlines()
    words_ru = []
    words_en = []
    for line in dictionary:
        word1, word2 = line.split('-')
        words_ru.append(word1)
        words_en.append(word2)
    return words_ru, words_en

def add_words(word_ru: str, word_en: str):
    with open(os.path.join(BASE_DIR, 'Perevod/dictionary.txt'), "a", encoding="utf-8") as file:
        file.write(word_ru + "-" + word_en + "\n")
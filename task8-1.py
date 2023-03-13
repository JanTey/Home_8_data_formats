import json
import os

# Функция, которая принимает путь к файлу и возвращает список слов длиннее 6 символов
def get_words(filename):
    with open(filename, encoding='utf-8') as f:
        data = json.load(f)
    words = []
    for item in data['rss']['channel']['items']:
        words += item['description'].split()
    # Используем генератор списков и метод isalpha() для удаления знаков препинания
    words = [word.strip().lower() for word in words if len(word.strip()) > 6 and word.strip().isalpha()]
    return words

# Функция, которая принимает список слов и возвращает список кортежей вида (слово, количество вхождений)
def get_word_counts(words):
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    # Используем метод items() для создания списка кортежей и метода sorted() для сортировки по количеству вхождений
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_word_counts[:10]

# Функция для вывода топ 10 самых часто встречающихся в новостях слов длиннее 6 символов для каждого файла
def print_top_words():
    filename = 'newsafr.json'
    words = get_words(filename)
    word_counts = get_word_counts(words)
    print(f'Топ 10 слов длиннее 6 символов в файле {filename}:')
    for word_count in word_counts:
        print(f'{word_count[0]}: {word_count[1]}')

# Вызываем функцию для вывода топ 10 самых часто встречающихся в новостях слов длиннее 6 символов для каждого файла
print_top_words()
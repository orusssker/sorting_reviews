# скрипт для сортировки отзывов по тональности из конкретного документа в отдельный файл

import csv
import nltk
import os

# Загрузка словаря для анализа тональности
nltk.download('vader_lexicon')
from nltk.sentiment import SentimentIntensityAnalyzer

# Определение пути к файлу с отзывами
file_path = 'Тут указываете путь к своему файлу'

# Определение пути для нового файла
new_file_path = os.path.splitext(file_path)[0] + '_analyzed.csv'

# Открытие файла с отзывами
with open(file_path, 'r') as file:
    reader = csv.reader(file)
    headers = next(reader) # чтение заголовков столбцов
    reviews = [row for row in reader] # чтение всех строк

# Создание экземпляра класса для анализа тональности
analyzer = SentimentIntensityAnalyzer()

# Создание нового списка для отзывов и оценок
reviews_with_scores = []

# Анализ каждого отзыва и присвоение оценки
for review in reviews:
    score = analyzer.polarity_scores(review[1])['compound'] # определение компаунд-оценки отзыва
    if review[0].isdigit(): # проверка, что первый столбец содержит только числа
        rating = float(review[0])
    else:
        rating = review[0]
    reviews_with_scores.append([rating, review[1], round(score, 2)]) # добавление отзыва и оценки в новый список

# Сортировка отзывов по оценке
reviews_with_scores.sort(key=lambda x: x[2], reverse=True)

# Запись отранжированных отзывов в новый файл
with open(new_file_path, 'w', newline='') as new_file:
    writer = csv.writer(new_file)
    writer.writerow(['rating'] + headers[1:] + ['rate']) # добавление заголовка для нового столбца
    writer.writerows(reviews_with_scores)

print(f"Результат записан в файл {new_file_path}")

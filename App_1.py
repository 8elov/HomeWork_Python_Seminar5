# # 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

with open('file1.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    print('Исходный текст:', text)

text = text.lower()
find_text = 'а' or 'б'
new_text = list(filter(lambda word: not find_text in word, text.split()))
new_text = list(filter(lambda word: not 'в' in word, new_text))

print('Отредактированный текст:', ' '.join(new_text))
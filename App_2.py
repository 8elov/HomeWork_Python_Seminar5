# 4.Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Пример:
#     На сжатие входные данные: 
#     WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
#     Выходные данные:          
#     12W1B12W3B24W1B14W

def coding(text):
    count = 1
    res = ''
    for i in range(len(text)-1):
        if text[i] == text[i+1]:
            count += 1
        else:
            res = res + str(count) + text[i]
            count = 1
    if count > 1 or (text[len(text)-2] != text[-1]):
        res = res + str(count) + text[-1]
    return res


def decoding(text):
    number = ''
    res = ''
    for i in range(len(text)):
        if not text[i].isalpha():
            number += text[i]
        else:
            res = res + text[i] * int(number)
            number = ''
    return res

with open('file2.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    print('Исходный текст:', text)

print(f"Текст после кодировки: {coding(text)}")
print(f"Текст после дешифровки: {decoding(coding(text))}")
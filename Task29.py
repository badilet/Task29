# Напишите функцию где вводится нормализованный текст, который кроме слов
# может содержать определенные знаки препинания. Распечатать текст без знаков
# припинания, то есть удалить все знаки препинания.
# Примечание. Под нормализованным текстом будем понимать текст, в котором пробел ставится после знаков
# препинания, за исключением открывающей скобки.

str = input("Enter a text: ")
print(str.translate({ord(i): None for i in r',.!?/\'"+=-_][}{~@#$%^&*()'}))


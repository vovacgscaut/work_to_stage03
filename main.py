

import re
words="cet,cross,cat,combo,acces,net"
res=len(words)
print(res)
#
# string = "Пример строки с буквами"

# def check_letters(words,):
#     pattern = r"[a-zA-Z]"
#     if re.search(pattern, words):
#         return True
#     else:
#         return False
#
#
# if check_letters(words):
#     print("Строка содержит буквы")
# else:
#     print("Строка не содержит буквы")
start = -1
count = 0
buk=input("введите букву:" )
while True:
    start = words.find(buk, start+1)
    if start == -1:
        break
    count += 1

print("Количество вхождений символа в строку: ", count )
buk=input("введите букву:" )
print(buk)
while True:
    word_list = re.findall(r'\b\w+\b', words)
    rse_word=len(word_list)
    print("Количество слов в строке:", rse_word)
    print(word_list)

    word_out = words.find(buk)

    print("Поиск 'буквы' методом find:",word_out )
    print(rse_word-word_out)
    input('press any key for exit')
    break

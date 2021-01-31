# Fibonacci

# 1 1 2 3 5 8 13 21 34 55 89 144 ...
# i j i j i j  i  j  i  j  i  j ...

i = 1 # Первый элемент последовательности
j = 1 # Второй элемент последовательности
counter = 2 # Количество элементов в последовательности
sum_even_number = 0 # Сумма чётных чисел
all_even_number = [] # Все чётные числа
pre_last_number = 0 # Предпоследнее число последовательности


while i + j < 10000000:
    counter += 1
    if i > j:
        j += i
        if j % 2 == 0:
            sum_even_number += j
            all_even_number.append(j)
    else:
        i += j
        if i % 2 == 0:
            sum_even_number += i
            all_even_number.append(i)
    if i > j:
        pre_last_number = j
    else:
        pre_last_number = i


print(f"""
    Количество элементов в последовательности = {counter} 
    Сумма всех четных элементов = {sum_even_number}
    Все четные элементы = {all_even_number}
    Предпоследнее число последовательности = {pre_last_number}""")

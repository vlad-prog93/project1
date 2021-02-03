
def FizzBuzz(begin, finish):
    FB = 0
    B = 0
    F = 0
    p = 0
    for i in range(begin, finish):
        if i % 3 == 0 and i % 5 == 0:
            p += i
            FB += 1
            # print('FizzBuzz', str(FB))
        elif i % 3 == 0:
            F += 1
            # print(('Fizz'), str(F))
        elif i % 5 == 0:
            B += 1
            # print('Buzz', str(B))
            
    print(f'''Сумма чисел, которые деляться на 3 и на 5 = {p} 
Количество чисел, которые деляться на 3 и на 5 = {FB} 
Количество чисел, которые деляться на 3 = {F}
Количество чисел, которые деляться на 5 = {B}''')


FizzBuzz(1000, 20001)
# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.
# in
# 7

# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]

# in
# -1

# out
# Negative value of the number of numbers!
# []

# in
# 10

# out
# [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
# [6, 2, 3, 0, 9]

from random import choices 

def input_numbers(inputText):
    okey = False
    while not okey:
        try:
            number = int(input(f"{inputText}"))
            okey = True
            if number <= 0:
                okey = False
                print("Список не может быть равен 0 или меньше")
        except ValueError:
            print("Это не число!")
    return number


def creates_list(number):
    list_nums = choices(range(0, number), k = number)
    return list_nums

def looking_non_recurring(ls):
    result = []
    dup = [x for i, x in enumerate(ls) if x in ls[:i]]
    for i in ls:
        if i in result:
            continue
        for j in dup:
            if i != j:
                result.append(i)

    return result    



num = input_numbers("Задайте длинну списка: ")
used_list = creates_list(num)
print(used_list)
result = looking_non_recurring(used_list)
print(f"уникальные элементы списка: {result}")



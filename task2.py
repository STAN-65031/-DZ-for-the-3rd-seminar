# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# Простые делители числа

# in
# 54

# out
# [2, 3, 3, 3]

# in
# 9990

# out
# [2, 3, 3, 3, 5, 37]

# in
# 650

# out
# [2, 5, 5, 13]

def InputNumbers(inputText):
    okey = False
    while not okey:
        try:
            number = int(input(f"{inputText}"))
            okey = True
        except ValueError:
            print("Какое-то неправильное число!")
    return number


def func_search(num):
    rezult = []

    for i in range(2, num):
        while num % i == 0:
            num /= i
            rezult.append(i)
    return rezult


num = InputNumbers("Введите натуральное число N: ")


print(f"Cписок простых множителей: {func_search(num)}")
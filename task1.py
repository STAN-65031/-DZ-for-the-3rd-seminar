# 1. Вычислить число c заданной точностью d
# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001

# out
# 9.000000

# in
# Enter a real number: 8.98785
# Enter the required accuracy '0.0001': 0.001

# out
# 8.988

def InputNumbers(inputText):
    okey = False
    while not okey:
        try:
            number = float(input(f"{inputText}"))
            okey = True
        except ValueError:
            print("Какое-то неправильное число!")
    return number


def division(num1, num2):
    return num1 / num2


num1 = InputNumbers("Введите 1 число: ")
num2 = InputNumbers("Введите 2 число: ")
n = int(InputNumbers("Введите точность (количество знаков после запятой): "))
rezult = round(division(num1, num2), n)

print(f"Результат деления: {rezult}")
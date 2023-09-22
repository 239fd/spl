import math
def is_int(str):
    try:
        int(str)
        return True
    except ValueError:
        return False

def solve(a, b, c):
    D = (b ** 2) - 4 * a * c

    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        return min(x1, x2), max(x1, x2)
    elif D == 0:
        x1 = -b / (2 * a)
        x2 = x1
        return x1,x2
    else:
        str = "Нет действительных корней"
        return str, ""


a = input("Введите значение a: ")
while not is_int(a) or a == 0:
    a = input("Неверно, введите значение a: ")
b = input("Введите значение b: ")
while not is_int(b):
    b = input("Неверно, введите значение b: ")
c = input("Введите значение c: ")
while not is_int(c):
    c = input("Неверно, введите значение c: ")
a = int(a)
b = int(b)
c = int(c)
x1, x2 = solve(a, b, c)
print(x1, x2)

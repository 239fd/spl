def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Деление на ноль запрещено.")
        result = None
    except TypeError:
        print("Ошибка: неверный тип данных.")
        result = None
    finally:
        print("Завершение программы.")

    return result


print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide("10", 2))

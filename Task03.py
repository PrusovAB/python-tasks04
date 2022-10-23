# 3.Задайте последовательность чисел. Напишите программу, которая выведет
# список неповторяющихся элементов исходной последовательности.


# Список неповторяющихся элементов


def not_repeat(numbers):
    not_new_repeat = []
    for elem in numbers:
        if numbers.count(elem) == 1:
            not_new_repeat.append(elem)
    print(f"список неповторяющих элементов списка = {not_new_repeat}")


def Create_New_Array():
    try:
        b = []
        while 1:
            a = int(
                input("Введите число. Список будет заполнятся пока вводяться числа целые числа: "))
            b.append(a)
    except ValueError:
        return b

    return b


new_list = Create_New_Array()
print(f"Наш изначальный список {new_list}")
a = not_repeat(new_list)


def set_list(list_new):
    set_new = set(list_new)
    print(f"Список уникальных элементов {list(set_new)}")


set_list(new_list)

# 4.Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# *Пример:*

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


import random


def get_pol_dict(k):
    pol_dict = {}

    while k != -1:
        kk = random.randint(0, 101)
        pol_dict[k] = kk
        k -= 1
    return pol_dict


def wtite_pol_file(pol_dict, file_name):
    text_str = ""
    max_deg = max(pol_dict.keys())
    for deg in range(max_deg, -1, -1):
        if pol_dict[deg] != 0:
            if pol_dict[deg] > 0:
                sig = "+"
            else:
                sig = "-"

            if abs(pol_dict[deg]) == 1 and deg != 0:
                temp = ''
            else:
                temp = str(abs(pol_dict[deg]))
            if deg == 0:
                text_str += sig + " " + temp
            elif deg == 1:
                text_str += sig + " " + temp + "x "
            else:
                text_str += sig + " " + temp + f"x^{deg}"
    if text_str[-1] == " ":
        text_str += '= 0'
    else:
        text_str += " = 0"
    if text_str[0] == "+":
        text_str = text_str[2:]

    with open(file_name, "w") as data:
        data.write(text_str)
    print(f"Рандомный многочлен : {text_str} записан в фаилл {file_name}")


k = abs(int(input("Введите степень k: ")))

pol_dict = get_pol_dict(k)

print(f"Словарь полином: {pol_dict}")

file_name = 'file.txt'

wtite_pol_file(pol_dict, file_name)

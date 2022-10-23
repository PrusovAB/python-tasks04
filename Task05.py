# 5.Даны два файла, в каждом из которых находится запись многочлена.
#  Задача - сформировать файл, содержащий сумму многочленов.
import random


def get_kk(pol_str):
    polinom_dict = {}
    polinom_list = pol_str.split(" ")
    sign = 1

    for pol_num in range(0, len(polinom_list) - 2):

        if polinom_list[pol_num][0] == "-" or polinom_list[pol_num] == "-":
            sign = -1

        if polinom_list[pol_num] not in ("+", "-"):

            if polinom_list[pol_num].find("x") == -1:
                polinom_dict[0] = int(polinom_list[pol_num]) * sign
                sign = 1
            elif polinom_list[pol_num].find("^") == -1 and polinom_list[pol_num].find("x") != -1:
                temp = polinom_list[pol_num].replace("x", "")
                if len(temp) == 0:
                    temp = 1
                polinom_dict[1] = int(temp) * sign
                sign = 1
            else:
                temp = polinom_list[pol_num].replace("^", "")
                if temp.find("-") != -1:
                    temp = temp.replace("-", "")
                    temp = temp.split("x")
                    if len(temp[0]) == 0:
                        temp[0] = 1
                    polinom_dict[int(temp[1])] = int(temp[0]) * sign
                    sign = 1
    return polinom_dict


def sum_dict(pol_dict_1, pol_dict_2):
    sum_dict = pol_dict_1.copy()
    sum_dict.update(pol_dict_2)

    for sum_keys in sum_dict:
        sum_dict[sum_keys] = pol_dict_1.get(
            sum_keys, 0) + pol_dict_2.get(sum_keys, 0)
    return sum_dict


def get_pol_dict(k):
    pol_dict = {}

    while k != -1:
        kk = random.randint(0, 101)
        pol_dict[k] = kk
        k -= 1
    return pol_dict


def get_pol_from_file(file_name):
    with open(file_name, "r") as data:
        pol_str = data.read()
    return pol_str


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


file_1 = "file_1.txt"
file_2 = "file _2.txt"
file_3 = "file_3.txt"

k = abs(int(input("Введите натуральную степерь первого многочлена: ")))

polynom_dist = get_pol_dict(k)
wtite_pol_file(polynom_dist, file_1)

k = abs(int(input("Введите натуральную степерь второго многочлена: ")))

polynom_dist = get_pol_dict(k)
wtite_pol_file(polynom_dist, file_2)

polynom_string_1 = get_pol_from_file(file_1)
pol_dict_1 = get_kk(polynom_string_1)
print(pol_dict_1)

polynom_string_2 = get_pol_from_file(file_2)
pol_dict_2 = get_kk(polynom_string_2)
print(pol_dict_2)


sum_pol = sum_dict(pol_dict_1, pol_dict_2)

print(f"{'=' * 40}")

wtite_pol_file(sum_pol, file_3)

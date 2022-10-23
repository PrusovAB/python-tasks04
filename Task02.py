# 2.Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
def check_simp(num):
    for i in range(2, (num // 2 + 1)):
        if num % i == 0:
            return False
    return True


def simpl_mult(num):
    if num < 2:
        return -1
    simpl_num = []
    while num > 1:
        for i in range(2, num + 1):
            if num % i == 0:
                if check_simp(i):
                    simpl_num.append(i)
                    num //= i
                    break
    return simpl_num


num = abs(int(input("Введите число: ")))
print(f"список простых множителей числа {num} = {simpl_mult(num)}")

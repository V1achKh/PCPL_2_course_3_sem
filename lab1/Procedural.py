import sys
import math


def get_coef(index, prompt, can_be_zero=True):
    try:
        value = float(sys.argv[index])
        if can_be_zero or value != 0:
            return value
    except (IndexError, ValueError):
        pass
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print("Ошибка ввода. Пожалуйста, введите числовое значение.")
            continue
        if value == 0 and not can_be_zero:
            print("Коэффициент A не может быть равен нулю. Повторите ввод.")
            continue
        return value


def discr(A, B, C):
    D = B**2 - 4 * A * C
    if D < 0:
        return -1
    elif D == 0:
        return 0
    else:
        return D


def t_test(t):
    if t == 0:
        return [0]
    elif t > 0:
        x1 = math.sqrt(t)
        x2 = -math.sqrt(t)
        return [x1, x2]
    else:
        return []


def solution(A, B, C, D):
    if D < 0:
        print("Действительных корней нет")
        return None

    t = -B / (2 * A)
    if D == 0:
        t12 = t_test(t)
        if len(t12) == 0:
            print("Действительных корней нет")
        elif len(t12) == 1:
            print("1 корень: x = 0")
        else:
            print(f"2 корня: x1 = {round(t12[0], 2)}, x2 = {round(t12[1], 2)}")

    if D > 0:
        t1 = (-B + math.sqrt(D)) / (2 * A)
        t2 = (-B - math.sqrt(D)) / (2 * A)
        x12 = t_test(t1) + t_test(t2)
        if len(x12) == 0:
            print("Действительных корней нет")
        elif len(x12) == 1:
            print(f"1 корень: x = {round(x12[0], 2)}")
        else:
            print(f"{len(x12)} корня:", end="")
            for x in x12:
                print(f" x = {round(x, 2)}", end="")
            print()


def main():
    A = get_coef(1, "Введите коэффициент A: ", can_be_zero=False)
    B = get_coef(2, "Введите коэффициент B: ")
    C = get_coef(3, "Введите коэффициент C: ")
    solution(A, B, C, discr(A, B, C))


if __name__ == "__main__":
    main()
import sys
import math
from typing import NamedTuple


class BiquadraticResult:
    NoRoots = NamedTuple("NoRoots", [])
    OneRoot = NamedTuple("OneRoot", [("x", float)])
    TwoRoots = NamedTuple("TwoRoots", [("x1", float), ("x2", float)])
    ThreeRoots = NamedTuple("ThreeRoots", [("x1", float), ("x2", float), ("x3", float)])
    FourRoots = NamedTuple("FourRoots", [("x1", float), ("x2", float), ("x3", float), ("x4", float)])


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
            print('Ошибка ввода. Введите число.')
            continue
        if value == 0 and not can_be_zero:
            print('Этот коэффициент не может быть равен нулю.')
            continue
        return value


def get_t_values(a, b, c):
    d = b * b - 4 * a * c
    if d < 0:
        return ()
    if d == 0:
        return (-b / (2 * a),)
    sq_d = math.sqrt(d)
    return ((-b + sq_d) / (2 * a), (-b - sq_d) / (2 * a))


def roots_from_t(t):
    if t > 0:
        return (-math.sqrt(t), math.sqrt(t))
    if t == 0:
        return (0.0,)
    return ()


def get_roots(a, b, c):
    xs = tuple(sorted(x for t in get_t_values(a, b, c) for x in roots_from_t(t)))
    match xs:
        case ():
            return BiquadraticResult.NoRoots()
        case (x,):
            return BiquadraticResult.OneRoot(x)
        case (x1, x2):
            return BiquadraticResult.TwoRoots(x1, x2)
        case (x1, x2, x3):
            return BiquadraticResult.ThreeRoots(x1, x2, x3)
        case _:
            return BiquadraticResult.FourRoots(*xs)


def print_roots(result):
    match result:
        case BiquadraticResult.FourRoots(x1, x2, x3, x4):
            print(f'Четыре корня: {x1}, {x2}, {x3}, {x4}')
        case BiquadraticResult.ThreeRoots(x1, x2, x3):
            print(f'Три корня: {x1}, {x2}, {x3}')
        case BiquadraticResult.TwoRoots(x1, x2):
            print(f'Два корня: {x1} и {x2}')
        case BiquadraticResult.OneRoot(x):
            print(f'Один корень: {x}')
        case BiquadraticResult.NoRoots():
            print('Действительных корней нет')


def main():
    a = get_coef(1, 'Введите коэффициент A: ', can_be_zero=False)
    b = get_coef(2, 'Введите коэффициент B: ')
    c = get_coef(3, 'Введите коэффициент C: ')
    print_roots(get_roots(a, b, c))


if __name__ == "__main__":
    main()
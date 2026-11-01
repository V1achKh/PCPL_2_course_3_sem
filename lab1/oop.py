import sys
import math


class BiquadraticEquation:
    def __init__(self):
        self.coef_A = 0.0
        self.coef_B = 0.0
        self.coef_C = 0.0
        self.discriminant = 0.0
        self.roots_list = []

    def get_coef(self, index, prompt, can_be_zero=True):
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

    def get_coefs(self):
        self.coef_A = self.get_coef(1, 'Введите коэффициент A: ', can_be_zero=False)
        self.coef_B = self.get_coef(2, 'Введите коэффициент B: ')
        self.coef_C = self.get_coef(3, 'Введите коэффициент C: ')

    def calculate_roots(self):
        a, b, c = self.coef_A, self.coef_B, self.coef_C
        self.discriminant = b * b - 4 * a * c
        self.roots_list = []

        t_values = []
        if self.discriminant == 0:
            t_values.append(-b / (2 * a))
        elif self.discriminant > 0:
            sq_d = math.sqrt(self.discriminant)
            t_values.append((-b + sq_d) / (2 * a))
            t_values.append((-b - sq_d) / (2 * a))

        for t in t_values:
            if t > 0:
                self.roots_list.append(math.sqrt(t))
                self.roots_list.append(-math.sqrt(t))
            elif t == 0:
                self.roots_list.append(0.0)
        self.roots_list.sort()

    def print_roots(self):
        print(f'Дискриминант D = {self.discriminant}')
        n = len(self.roots_list)
        if n == 0:
            print('Действительных корней нет')
        elif n == 1:
            print(f'Один корень: {self.roots_list[0]}')
        else:
            roots = ', '.join(str(x) for x in self.roots_list)
            print(f'Корней: {n}: {roots}')


def main():
    eq = BiquadraticEquation()
    eq.get_coefs()
    eq.calculate_roots()
    eq.print_roots()


if __name__ == "__main__":
    main()
# itemgetter нужен для сортировки: itemgetter(2) == lambda x: x[2]
from operator import itemgetter


class Emp:
    """Сотрудник"""
    def __init__(self, id, fio, sal, dep_id):
        self.id = id            # первичный ключ сотрудника
        self.fio = fio          # фамилия
        self.sal = sal          # зарплата (количественный признак)
        self.dep_id = dep_id    # внешний ключ на отдел (связь один-ко-многим)


class Dep:
    """Отдел"""
    def __init__(self, id, name):
        self.id = id            # первичный ключ отдела
        self.name = name        # название отдела


class EmpDep:
    """
    'Сотрудники отдела' для реализации
    связи многие-ко-многим
    """
    def __init__(self, dep_id, emp_id):
        self.dep_id = dep_id    # id отдела
        self.emp_id = emp_id    # id сотрудника


# Отделы
deps = [
    Dep(1, 'отдел кадров'),
    Dep(2, 'архивный отдел ресурсов'),
    Dep(3, 'бухгалтерия'),
    # "другие" отделы нужны только для связи многие-ко-многим
    Dep(11, 'отдел (другой) кадров'),
    Dep(22, 'архивный (другой) отдел ресурсов'),
    Dep(33, '(другая) бухгалтерия'),
]

# Сотрудники (последнее число - id отдела, где сотрудник числится)
emps = [
    Emp(1, 'Артамонов', 25000, 1),
    Emp(2, 'Петров', 35000, 2),
    Emp(3, 'Иваненко', 45000, 3),
    Emp(4, 'Иванов', 35000, 3),
    Emp(5, 'Иванин', 25000, 3),
]

# Связи многие-ко-многим: EmpDep(id отдела, id сотрудника)
# Один сотрудник может быть в нескольких отделах, и наоборот
emps_deps = [
    EmpDep(1, 1),
    EmpDep(2, 2),
    EmpDep(3, 3),
    EmpDep(3, 4),
    EmpDep(3, 5),

    EmpDep(11, 1),
    EmpDep(22, 2),
    EmpDep(33, 3),
    EmpDep(33, 4),
    EmpDep(33, 5),
]


def main():
    """Основная функция"""

    # --- Соединение один-ко-многим ---
    # Перебираем все пары (отдел, сотрудник) и оставляем те,
    # где dep_id сотрудника совпадает с id отдела.
    # Результат: список кортежей (фамилия, зарплата, название отдела)
    one_to_many = [(e.fio, e.sal, d.name)
                   for d in deps
                   for e in emps
                   if e.dep_id == d.id]

    # --- Соединение многие-ко-многим (в два шага) ---
    # Шаг 1: отдел + запись связи -> (название отдела, id отдела, id сотрудника)
    many_to_many_temp = [(d.name, ed.dep_id, ed.emp_id)
                         for d in deps
                         for ed in emps_deps
                         if d.id == ed.dep_id]

    # Шаг 2: по id сотрудника находим самого сотрудника
    # Результат: (фамилия, зарплата, название отдела)
    many_to_many = [(e.fio, e.sal, dep_name)
                    for dep_name, dep_id, emp_id in many_to_many_temp
                    for e in emps
                    if e.id == emp_id]

    # --- Запрос 1: все связи, отсортированные по отделам ---
    print('Задание А1')
    res_11 = sorted(one_to_many, key=itemgetter(2))  # сортируем по названию отдела
    print(res_11)

    # --- Запрос 2: отделы с суммарной зарплатой ---
    print('\nЗадание А2')
    res_12_unsorted = []
    for d in deps:
        # Сотрудники этого отдела (фильтруем по названию отдела)
        d_emps = list(filter(lambda i: i[2] == d.name, one_to_many))
        if len(d_emps) > 0:                        # пустые отделы пропускаем
            d_sals = [sal for _, sal, _ in d_emps] # только зарплаты; _ = "не нужно"
            d_sals_sum = sum(d_sals)
            res_12_unsorted.append((d.name, d_sals_sum))
    # Сортировка по сумме, по убыванию
    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    print(res_12)

    # --- Запрос 3: отделы со словом «отдел» и их сотрудники (многие-ко-многим) ---
    print('\nЗадание А3')
    res_13 = {}   # словарь: название отдела -> список фамилий
    for d in deps:
        if 'отдел' in d.name:
            d_emps = list(filter(lambda i: i[2] == d.name, many_to_many))
            d_emps_names = [x for x, _, _ in d_emps]   # только фамилии
            res_13[d.name] = d_emps_names
    print(res_13)


# Запуск main() только при прямом запуске файла (не при импорте)
if __name__ == '__main__':
    main()
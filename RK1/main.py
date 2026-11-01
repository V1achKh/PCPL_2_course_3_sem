from operator import itemgetter

class Programm:
    def __init__(self, id, name, size, comp_id):
        self.id = id
        self.name = name
        self.size = size
        self.comp_id = comp_id #внешний ключ

class Comp:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class ProComp:
    def __init__(self, program_id, comp_id):
        self.program_id = program_id
        self.comp_id = comp_id

Programs =[
    Programm(1, '1C', 1200,  1),
    Programm(2, 'DbEaver', 315, 2),
    Programm(3, "Multisim", 238,  2),
    Programm(4, 'Claude', 1006, 4),
    Programm(5, 'Vscode', 2167, 5),
    Programm(6, 'Pycharm', 4589, 6),
    Programm(7, 'AutoCade', 9700, 7),
    Programm(8, 'Excel', 426, 3)
]

Comps = [
    Comp(1, 'Кристофари Нео'),
    Comp(2, 'Червоненкис'),
    Comp(3, 'Галушкин'),
    Comp(4, 'Ляпунов'),
    Comp(5, 'Кристофари'),
    Comp(6, 'Аврора'),
    Comp(7, 'Заяц'),
    Comp(8, 'Волк')
]

programms_comps = [
    ProComp(1, 1),
    ProComp(1, 4),
    ProComp(2, 2),
    ProComp(2, 5),
    ProComp(3, 3),
    ProComp(3, 7),
    ProComp(4, 4),
    ProComp(4, 6),
    ProComp(5, 5),
    ProComp(5, 8),
    ProComp(6, 6),
    ProComp(7, 7),
    ProComp(7, 1),
]

def main():
    one_to_many = [(p.name, p.size, c.name) 
                  for p in Programs 
                  for c in Comps
                  if p.comp_id == c.id]

    many_to_many_temp = [(c.name, pc.comp_id, pc.program_id) 
                         for c in Comps 
                         for pc in programms_comps
                         if c.id == pc.comp_id]

    many_to_many = [(comp_name, p.name, p.size)
                    for comp_name, comp_id, program_id in many_to_many_temp
                    for p in Programs
                    if p.id == program_id]
    
    print("Задание 1")

    res1 = {}
    for r in one_to_many:
        if r[2].startswith('А'):
            res1.setdefault(r[2], []).append(r[0])
    print(res1)

    print("Задание 2")

    res2_unsorted = []
    for c in Comps:
        lst = list(filter(lambda i: i[2] == c.name, one_to_many))
        if len(lst)>0:
            size_of_program_of_comp = [i[1] for i in lst]
            res2_unsorted.append((c.name, max(size_of_program_of_comp)))

    res_2 = sorted(res2_unsorted, key=itemgetter(1), reverse=True)
    print(res_2)

    print("Задание 3")

    res3 = sorted(many_to_many, key=itemgetter(0))
    print(res3)



if __name__ == '__main__':
    main()
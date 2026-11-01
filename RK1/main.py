class Programm:
    def __init__(self, id, name, comp_id):
        self.id = id
        self.name = name
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
    Programm(1, '1C', 1),
    Programm(2, 'DbEaver', 2),
    Programm(3, "Multisim", 2),
    Programm(4, 'Claude', 4),
    Programm(5, 'Vscode', 5),
    Programm(6, 'Pycharm', 6),
    Programm(7, 'AutoCade', 7),
    Programm(8, 'Excel', 3)
]

Comps = [
    Comp(1, 'Кристофари Нео'),
    Comp(2, 'Червоненкис'),
    Comp(3, 'Галушкин'),
    Comp(4, 'Ляпунов'),
    Comp(5, 'Кристофари'),
    Comp(6, 'Заяц'),
    Comp(7, 'Волк')
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
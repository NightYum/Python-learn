from string import ascii_letters

class Person:
    S_RUS = "ёйцукенгшщзхъфывапролджэячсмитьбю"
    S_RUS_UPPER = S_RUS.upper()
    LETTERS = ascii_letters + S_RUS + S_RUS_UPPER
    MIN_OLD = 18
    MAX_OLD = 110

    def __init__(self, fio, old, ps, weight):
        self.verify_fio(fio)
        self.verify_old(old)
        self.fio = fio
        self.old = old
        self.ps = ps
        self.weight = weight

    @classmethod
    def verify_fio(cls, fio):
        if not isinstance(fio, str):
            raise TypeError('fio must be a string')

        f = fio.split()
        if len(f) != 3:
            raise TypeError('fio must FIO')

        for s in f:
            if len(s) < 2:
                raise TypeError('len < 2')
            if len(s.strip(cls.LETTERS)) != 0:
                raise TypeError('')

    @classmethod
    def verify_old(cls, old: int):
        if not isinstance(old, int) or cls.MIN_OLD <= old <= cls.MAX_OLD:
            raise TypeError('old must be a integer ')

me = Person("Михаил Ерастов Алексеевич", 18, "1244 5345", 55)
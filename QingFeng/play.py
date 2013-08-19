class People(object):
    def __init__(self, name, hp=100, mp=100, mxhp=100, mxmp=100, attk=1, deff=1, exp=0):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.mxhp = mxhp
        self.mxmp = mxmp
        self.attk = attk
        self.deff = deff
        self.exp = exp

    def isdead(self):
        return self.hp <= 0

    @property
    def level(self):
        return self.exp/10+1

    def run(self):
        self.hp -= 1

    def equip(self, e):
        self.attk += 1

    def attack(self, enemy):
        x = self.attk - enemy.deff
        if x > 0:
            enemy.hp -= x
        self.exp += 1

    def use(self, magic, enemy):
        x = self.attk + magic.attk - enemy.deff
        if x > 0:
            enemy.hp -= x

class Hero(People):
    def eat(self, item):
       self.hp += item.hp
       self.mp += item.mp
       self.hp = min(self.hp, self.mxhp)
       self.mp = min(self.mp, self.mxmp)

class Item(object):
    def __init__(self, name, hp=0, mp=0):
        self.name = name
        self.hp = hp 
        self.mp = mp

class Bag(object):
    def __init__(self, limit):
        self.limit = limit
        self.slot = []

    def add(self, item):
        if len(self.slot) < self.limit:
            self.slot.append(item)
        else:
            return False

class Enemy(People):
    pass

class Equip(object):
    def __init__(self, name):
        self.name = name

class Magic(object):
    def __init__(self, name, attk):
        self.name = name
        self.attk = attk


class Fashi(Hero):
    def __init__(self, name, mp=50, mxmp=200, hp=50, mxhp=50, attk=100, deff=20,exp=0):
        self.mp = mp
        self.exp = exp
        self.name = name
        self.hp = hp
        self.mxmp = mxmp
        self.mxhp = mxhp
        self.attk = attk
        self.deff = deff

class Zhanshi(Hero):
    def __init__(self, name, mp=20, mxmp=50, hp=20, mxhp=200, attk=10, deff=20, exp=0):
        self.name = name
        self.exp = exp
        self.mp = mp
        self.hp = hp
        self.mxmp = mxmp
        self.mxhp = mxhp
        self.attk = attk
        self.deff = deff


import unittest
from play import Hero, Enemy, Equip, Magic, Bag, Item, Zhanshi, Fashi

class TestHero(unittest.TestCase):
    def test_hero_shuxing(self):
        hero1 = Hero(name="testhero", hp=100, mp=100, mxhp=100, mxmp=100)
        self.assertEqual(hero1.name, 'testhero')
        self.assertEqual(hero1.hp, 100)
        self.assertEqual(hero1.mp, 100)
        self.assertEqual(hero1.mxhp, 100)
        self.assertEqual(hero1.mxmp, 100)

    def test_hero_run(self):
        hero1 = Hero(name="testhero", hp=100, mp=100, mxhp=100, mxmp=100)
        self.assertEqual(hero1.hp, 100)
        hero1.run()
        self.assertEqual(hero1.hp, 99)

    def test_hero_equip(self):
        hero1 = Hero(name="qingfeng", hp=100, mp=100,
                        mxhp=100, mxmp=100, attk=1)
        self.assertEqual(hero1.attk, 1)
        gun = Equip(name="gun")
        hero1.equip(gun)
        self.assertEqual(hero1.attk, 2)

    def test_hero_attk(self):
        hero1 = Hero(name="qingfeng", hp=100, mp=100,
                     mxhp=100, mxmp=100, attk=1)
        enemy1 = Enemy(name="enemy1", hp=200, mp=200,
                       mxhp=200, mxmp=200, deff=2)
        self.assertEqual(hero1.hp, 100)
        hero1.attack(enemy1)
        self.assertEqual(enemy1.hp, 200)

    def test_hero_magic(self):
        hero1 = Hero(name="qingfeng", hp=100, attk=1)
        magic1 = Magic(name="huoqiu", attk=2)
        enemy1 = Enemy(name="enemy1", hp=200, deff=1)
        self.assertEqual(hero1.hp, 100)
        hero1.use(magic1, enemy1)
        self.assertEqual(enemy1.hp, 198)

    def test_is_dead(self):
        hero1 = Hero(name="qingfeng", hp=1000, attk=2)
        enemy1 = Enemy(name="enemy1", hp=800, deff=1)
        magic1 = Magic(name="Stone", attk=1)
        for i in range(399):
            hero1.use(magic1, enemy1)
        self.assertFalse(enemy1.isdead())
        hero1.use(magic1, enemy1)
        self.assertTrue(enemy1.isdead())

    def test_people_level(self):     
        hero1 = Hero(name="hero1", exp=0)
        self.assertEqual(hero1.level, 1)
        hero2 = Hero(name="hero2", exp=100)
        self.assertEqual(hero2.level, 11)
        enemy1 = Enemy(name="enemy1")
        for i in range(10):
            hero2.attack(enemy1)
        self.assertEqual(hero2.level, 12)

    def test_people_item(self):     
        hero1 = Hero(name="hero1", hp=100, mxhp=200, mp=100, mxmp=200)
        item1 = Item(name='xue', hp=120)
        hero1.eat(item1)
        self.assertEqual(hero1.hp, 200)
        item2 = Item(name='mxue', mp=220)
        hero1.eat(item2)
        self.assertEqual(hero1.mp, 200)

    def test_people_bag(self):     
        hero1 = Hero(name="hero1")
        bag1 = Bag(limit=3)
        for i in range(3):
            item = Item(name='mxue', mp=220)
            bag1.add(item)
        item2 = Item(name='mxue', mp=220)
        r = bag1.add(item2)
        self.assertFalse(r)

    def test_hero_fashi(self):
        fashi1 = Fashi(name="fashi1")
        self.assertEqual(fashi1.mxmp, 200)
        self.assertEqual(fashi1.mxhp, 50)
        self.assertEqual(fashi1.attk, 100)
        
    def test_hero_zhanshi(self):
        zhanshi1 = Zhanshi(name="zhanshi1")
        self.assertEqual(zhanshi1.mxmp, 50)
        self.assertEqual(zhanshi1.mxhp, 200)
        self.assertEqual(zhanshi1.attk, 10)
        
    def test_enemy_boss(self):
        boss1 = Enemy(name="boss1", hp=1000, mp=1000, mxhp=1000, mxmp=1000, attk=100, deff=20)
        hero1 = Fashi(name="zhanshi1")
        hero1.attack(boss1)
        self.assertFalse(boss1.isdead())

if __name__ == '__main__':
    unittest.main()



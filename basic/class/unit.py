class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("hp : {0}, ad : {1}".format(self.hp, self.damage))
        
unit1 = Unit("Marine", 40, 5)
unit2 = Unit("Tank", 200, 30)

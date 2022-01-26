class Unit:
    def __init__(self):
        print("Unit constructor.")
        
class Flyable:
    def __init__(self):
        print("Flyable constructor.")
        
class FlyableUnit(Unit, Flyable):
    def __init__(self):
        super().__init__()
        Unit()
        Flyable()
        
FlyableUnit()
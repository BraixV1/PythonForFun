class Weapons:
    """What type of combat is possible."""
    def __init__(self, type, damage, passive=None, durability=False) -> None:
        self.type = type
        self.damage = damage
        self.passive = passive
        self.durability = durability
        self.level_required = 0
        
        
    def add_durability(self, amount):
        pass
        
        
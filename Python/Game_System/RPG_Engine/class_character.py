
class Character:
    """Character class."""

    def __init__(self, name, level, xp, character_type, alive=True) -> None:
        self.name = name
        self.level = level
        self.xp = xp
        self.character_type = character_type
        self.alive = alive
        self.inventory = []
        self.weapons = []
        self.attacks = []
        self.to_level_up = self.xp_needed_to_level_up()

    def __repr__(self) -> str:
        return f"{self.name} class is {self.character_type}"


    def kill(self):
        self.alive = False
        
        
    def xp_needed_to_level_up(self):
        return self.level * 147
    
    def revive(self):
        if self.alive is False:
            self.alive = True
        
    def add_xp(self, amount):
        if self.xp + amount >= self.xp_needed_to_level_up():
            while int(self.xp + amount / self.xp_needed_to_level_up()) != 0:
                self.level += 1
                
    
    
            

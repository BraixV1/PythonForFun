"""EX12 adventure."""
import math


class Adventurer:
    """Class adventurer."""

    def __init__(self, name: str, class_type: str, power: int, experience: int = 0, status: bool = False):
        """Adventurer object constructor. Takes name, class_type power and experience.

        Status will show if adventurer is active and is False by default.
        if class type is not Fight Druid Wizard or Paladin the class type will be set to Fighter.
        if experience is smaller than 0 it will be set to default number 0.
        if power level is set higher than 99 it will be set back to default number 10.
        """
        self.name = name
        if power > 99:
            self.power = 10
        else:
            self.power = power
        if class_type not in ["Fighter", "Druid", "Wizard", "Paladin"]:
            self.class_type = "Fighter"
        else:
            self.class_type = class_type
        if experience < 0:
            self.experience = 0
        else:
            self.experience = experience
        self.status = status

    def __repr__(self):
        """Object Adventurer print."""
        return f"{self.name}, the {self.class_type}, Power: {int(self.power)}, Experience: {self.experience}."

    def add_power(self, amount: int):
        """Add given amount of power to the adventurer."""
        self.power += amount

    def add_experience(self, amount):
        """Add given amount of experience to adventurer and if it exceeds 100 then transform xp into combat power."""
        if amount < 0:
            pass
        else:
            self.experience += amount
            if self.experience > 99:
                self.power += int(math.floor(self.experience / 10))
                self.experience = 0


class Monster:
    """Class Monster."""

    def __init__(self, name: str, monster_type: str, power: int, status: bool = False):
        """Monster object constructor.

        Takes name, type and power. Status shows if monster is active or not and is False by default.
        """
        self.name = name
        self.type = monster_type
        self.power = power
        self.status = status
        if self.type == "Zombie":
            self.name = f"Undead {name}"

    def __repr__(self):
        """Object monster print."""
        return f"{self.name} of type {self.type}, Power: {self.power}."


class World:
    """Class world where game will take place. Game engine."""

    def __init__(self, name: str):
        """World object constructor.

        Saves graveyard, monsters and adventurers as lists. Default state of necromancers is False.
        """
        self.name = name
        self.graveyard = []
        self.monsters = []
        self.adventurers = []
        self.necromancers_status = False

    def get_python_master(self):
        """Return name of the world."""
        return self.name

    def get_graveyard(self):
        """Return list of items in graveyard."""
        return self.graveyard

    def necromancers_active(self, boole: bool):
        """Set necromancers status True or False."""
        self.necromancers_status = boole

    def revive_graveyard(self):
        """Revive all the characters in graveyard and turn them into zombies. Only if necromancer status is True."""
        if self.necromancers_status is True:
            for obj in self.graveyard:
                if isinstance(obj, Monster):
                    obj.type = "Zombie"
                    self.add_monster(obj)
                if isinstance(obj, Adventurer):
                    self.add_monster(Monster(f"Undead {obj.name}", f"Zombie {str(obj.class_type)}", obj.power))
            self.necromancers_status = False
            self.graveyard = []

    def add_monster(self, monster):
        """Add monster into monsters list."""
        if isinstance(monster, Monster):
            self.monsters.append(monster)

    def get_monster_list(self):
        """Return list of monsters whose status is not active."""
        result = []
        for monster in self.monsters:
            if monster.status is False:
                result.append(monster)
        return result

    def add_monster_by_name(self, name: str):
        """Activate monster whose name is equal to the name given."""
        for monster in self.monsters:
            if monster.name == name:
                monster.status = True

    def add_strongest_monster(self):
        """Activate monster with most amount of combat power."""
        filtered = self.monsters
        filtered.sort(key=lambda pw: pw.power, reverse=True)
        for obj in filtered:
            if obj.status is False:
                obj.status = True
                break

    def add_all_monsters_of_type(self, type: str):
        """Activate all the monsters whose monster type is equal to the type given."""
        for monster in self.monsters:
            if monster.type == type:
                monster.status = True

    def add_weakest_monster(self):
        """Activate monster with least amount of combat power."""
        filtered = self.monsters
        filtered.sort(key=lambda pw: pw.power)
        if self.monsters is not []:
            for item in filtered:
                if item.status is False:
                    item.status = True
                    break

    def get_active_monsters(self):
        """Return list of monsters whose status is active."""
        result = []
        for monster in self.monsters:
            if monster.status is True:
                result.append(monster)
        result.sort(key=lambda xp: xp.power, reverse=True)
        return result

    def add_all_monsters(self):
        """Turn all monster status into active."""
        for monster in self.monsters:
            if monster.status is False:
                monster.status = True

    # ------------------------------------------------------------------------------------------------------------------------------------------------------------

    # ------------------------------------------------------------------------------------------------------------------------------------------------------------

    def add_adventurer(self, adventurer):
        """Add new adventurer to the adventurers list."""
        if isinstance(adventurer, Adventurer):
            self.adventurers.append(adventurer)

    def get_adventurer_list(self):
        """Return all inactive adventurers."""
        result = []
        for adventurer in self.adventurers:
            if adventurer.status is False:
                result.append(adventurer)
        return result

    def add_strongest_adventurer(self, class_type):
        """Activate adventurer whose class type is the same as the given argument and has least amount of combat power."""
        filtered = self.adventurers
        filtered = list(filter(lambda ct: ct.class_type == class_type, filtered))
        if filtered is not []:
            filtered.sort(key=lambda pw: pw.power, reverse=True)
            for adventurer in filtered:
                if adventurer.status is False:
                    adventurer.status = True
                    break

    def add_weakest_adventurer(self, class_type):
        """Activate adventurer whose class type is the same as the given argument and has most amount of combat power."""
        filtered = self.adventurers
        filtered = list(filter(lambda ct: ct.class_type == class_type, filtered))
        if filtered is not []:
            filtered.sort(key=lambda pw: pw.power)
            for adventurer in filtered:
                if adventurer.status is False:
                    adventurer.status = True
                    break

    def add_most_experienced_adventurer(self, class_type):
        """Activate advneturer who has most amount of experience and has class type same as the parameter."""
        filtered = self.adventurers
        filtered = list(filter(lambda ct: ct.class_type == class_type, filtered))
        if filtered is not []:
            filtered.sort(key=lambda pw: pw.experience, reverse=True)
            for adventurer in filtered:
                if adventurer.status is False:
                    adventurer.status = True
                    break

    def add_least_experienced_adventurer(self, class_type):
        """Activate adventurer who has least amount of experience and class type is equal to the parameters given."""
        filtered = self.adventurers
        filtered = list(filter(lambda ct: ct.class_type == class_type, filtered))
        if filtered is not []:
            filtered.sort(key=lambda pw: pw.experience)
            for adventurer in filtered:
                if adventurer.status is False:
                    adventurer.status = True
                    break

    def add_adventurer_by_name(self, name):
        """Activate adventurer whose name is the same as given."""
        for adventurer in self.adventurers:
            if adventurer.name == name:
                adventurer.status = True

    def get_active_adventurers(self):
        """Return all adventurers with active status."""
        result = []
        for adventurer in self.adventurers:
            if adventurer.status is True:
                result.append(adventurer)
        result.sort(key=lambda xp: xp.experience, reverse=True)
        return result

    def add_all_adventurers_of_class_type(self, class_type: str):
        """Turn all adventurers active with given class_type."""
        for adventurer in self.adventurers:
            if adventurer.class_type == class_type and adventurer.status is False:
                adventurer.status = True

    def add_all_adventurers(self):
        """Turn all advneturers into active mode."""
        for adventurer in self.adventurers:
            adventurer.status = True

    # ------------------------------------------------------------------------------------------------------------------------------------------------------------

    # ------------------------------------------------------------------------------------------------------------------------------------------------------------
    def deactivate_adventurer(self, name: str):
        """Deactivate adventurers whose name is the same as given if name is all then deactivate all the adventurers."""
        if name == "all":
            for adventurer in self.adventurers:
                adventurer.status = False
        for adventurer in self.adventurers:
            if adventurer.name == name:
                adventurer.status = False

    def deactivate_monster(self, name: str):
        """Deactivate monster if input is all then deactivate all monsters."""
        if name == "all":
            for monster in self.monsters:
                monster.status = False
        for monster in self.monsters:
            if monster.type == name:
                monster.status = False

    def get_all_active_adventurer_combined_power(self):
        """Get all active adventurers power."""
        result = 0
        for adventurer in self.adventurers:
            if adventurer.status is True:
                result += adventurer.power
        return result

    def get_all_active_monster_combined_power(self):
        """Get all active monsters power."""
        result = 0
        for monster in self.monsters:
            if monster.status is True:
                result += monster.power
        return result

    def deactive_all(self):
        """Turn all monsters and adventurers status False."""
        self.deactivate_monster("all")
        self.deactivate_adventurer("all")

    def paladin_buff(self):
        """Return if paladin buff was given and give paladin buff."""
        paladin_buff = False
        if list(filter(
                lambda c: c.type in ["Zombie", "Zombie Fighter", "Zombie Druid", "Zombie Paladin", "Zombie Wizard"],
                self.get_active_monsters())):
            for paladin in list(filter(lambda c: c.class_type == "Paladin", self.get_active_adventurers())):
                paladin.power = paladin.power * 2
                paladin_buff = True
            if paladin_buff is True:
                return True
            else:
                return False

    def paladin_debuff(self, paladin_buff_status: bool):
        """Paladin temporary buff end."""
        if paladin_buff_status is True:
            for paladin in list(filter(lambda c: c.class_type == "Paladin", self.get_active_adventurers())):
                paladin.power = paladin.power / 2

    def druid(self):
        """Deactivate all animals type and ent type monsters if druid has been activated."""
        if list(filter(lambda c: c.class_type == "Druid", self.get_active_adventurers())):
            if list(filter(lambda c: c.type == "Animal", self.get_active_monsters())):
                self.deactivate_monster("Animal")
            if list(filter(lambda c: c.type == "Ent", self.get_active_monsters())):
                self.deactivate_monster("Ent")

    def add_xp(self, multiply: bool):
        """Add xp to all active adventurers."""
        monsters_power = self.get_all_active_monster_combined_power()
        active_adventurers = self.get_active_adventurers()
        if multiply is True:
            for adventurer in active_adventurers:
                adventurer.add_experience(math.floor(monsters_power / len(active_adventurers) * 2))
        else:
            for adventurer in active_adventurers:
                adventurer.add_experience(math.floor(monsters_power / len(active_adventurers)))

    def advneturers_are_stronger(self, deadly: bool, paladin_buff: bool):
        """Adventurers won the fight."""
        if deadly is False:
            self.paladin_debuff(paladin_buff)
            self.add_xp(deadly)
            self.deactive_all()
        if deadly is True:
            self.paladin_debuff(paladin_buff)
            self.add_xp(deadly)
            for monster in self.get_active_monsters():
                self.remove_character(monster.name)
            self.deactivate_adventurer("all")

    def monsters_are_stronger(self, deadly: bool, paladin_buff: bool):
        """Monsters won the fight."""
        if deadly is False:
            self.paladin_debuff(paladin_buff)
            self.deactive_all()
        if deadly is True:
            self.paladin_debuff(paladin_buff)
            self.deactivate_monster("all")
            for adventurer in self.get_active_adventurers():
                self.remove_character(adventurer.name)

    def draw(self, paladin_buff: bool):
        """Draw between monsters and adventurers."""
        self.paladin_debuff(paladin_buff)
        for adventurer in self.get_active_adventurers():
            adventurer.add_experience(
                math.floor(self.get_all_active_monster_combined_power() / len(self.get_active_adventurers()) / 2))
        self.deactive_all()

    def go_adventure(self, deadly: bool = False):
        """Get the outcome of the fight between active monsters and adventurers."""
        self.druid()
        paladin_buff = self.paladin_buff()
        if self.get_all_active_monster_combined_power() < self.get_all_active_adventurer_combined_power():
            self.advneturers_are_stronger(deadly, paladin_buff)

        if self.get_all_active_monster_combined_power() > self.get_all_active_adventurer_combined_power():
            self.monsters_are_stronger(deadly, paladin_buff)

        if self.get_all_active_monster_combined_power() == self.get_all_active_adventurer_combined_power():
            self.draw(paladin_buff)

    def remove_character(self, param):
        """Remove character from monster or advneturers list and add them to the graveyard. if character is already in graveyard then delete that object."""
        monster_temp = self.monsters
        adventure_temp = self.adventurers
        graveyard_temp = self.graveyard
        for adventurer in adventure_temp:
            if adventurer.name == param:
                self.adventurers.remove(adventurer)
                self.graveyard.append(adventurer)
                return
        for monster in monster_temp:
            if monster.name == param:
                self.monsters.remove(monster)
                self.graveyard.append(monster)
                return
        for graveyard in graveyard_temp:
            if graveyard.name == param:
                self.graveyard.remove(graveyard)
                return


if __name__ == "__main__":
    print("Kord oli maailm.")
    world = World("Sõber")
    print(world.get_python_master())  # -> "Sõber"
    print(world.get_graveyard())  # -> []
    print()
    print("Tutvustame tegelasi.")
    hero = Adventurer("Sander", "Paladin", 50)
    friend = Adventurer("Peep", "Druid", 25)
    another_friend = Adventurer("Toots", "Wizard", 40)
    annoying_friend = Adventurer("XxX_Eepiline_Sõdalane_XxX", "Tulevikurändaja ja ninja", 999999)
    print(hero)  # -> "Sander, the Paladin, Power: 50, Experience: 0."
    # Ei, tüütu sõber, sa ei saa olla tulevikurändaja ja ninja, nüüd sa pead fighter olema.
    # Ei maksa liiga tugevaks ka ennast alguses teha!
    print(annoying_friend)  # -> "XxX_Eepiline_Sõdalane_XxX, the Fighter, Power: 10, Experience: 0."
    print(friend)  # -> "Peep, the Druid, Power: 25, Experience: 0."
    print(another_friend)  # -> "Toots, the Wizard, Power: 40, Experience: 0."
    print()

    print("Peep, sa tundud kuidagi nõrk, ma lisasin sulle natukene tugevust.")
    friend.add_power(20)
    print(friend)  # -> "Peep, the Druid, Power: 45, Experience: 0."
    print()

    world.add_adventurer(hero)
    world.add_adventurer(friend)
    world.add_adventurer(another_friend)
    print(world.get_adventurer_list())  # -> Sander, Peep ja Toots

    world.add_monster(annoying_friend)
    # Ei, tüütu sõber, sa ei saa olla vaenlane.
    print(world.get_monster_list())  # -> []
    world.add_adventurer(annoying_friend)
    print()

    print("Oodake veidikene, ma tekitan natukene kolle.")
    zombie = Monster("Rat", "Zombie", 10)
    goblin_spear = Monster("Goblin Spearman", "Goblin", 10)
    goblin_archer = Monster("Goblin Archer", "Goblin", 5)
    big_ogre = Monster("Big Ogre", "Ogre", 120)
    gargantuan_badger = Monster("Massive Badger", "Animal", 1590)

    print(big_ogre)  # -> "Big Ogre of type Ogre, Power: 120."
    print(zombie)  # -> "Undead Rat of type Zombie, Power: 10."

    world.add_monster(goblin_spear)

    print()
    print("Mängime esimese seikluse läbi!")
    world.add_strongest_adventurer("Druid")
    world.add_strongest_monster()
    print(world.get_active_adventurers())  # -> Peep
    print(world.get_active_monsters())  # -> [Goblin Spearman of type Goblin, Power: 10.]
    print()

    world.go_adventure(True)

    world.add_strongest_adventurer("Druid")
    print(world.get_active_adventurers())  # -> [Peep, the Druid, Power: 45, Experience: 20.]
    print("Surnuaias peaks üks goblin olema.")
    print(world.get_graveyard())  # ->[Goblin Spearman of type Goblin, Power: 10.]

    print()

    world.add_monster(gargantuan_badger)
    world.add_strongest_monster()

    world.go_adventure(True)
    # Druid on loomade sõber ja ajab massiivse mägra ära.
    print(world.get_adventurer_list())  # -> Kõik 4 mängijat.
    print(world.get_monster_list())  # -> [Massive Badger of type Animal, Power: 1590.]

    world.remove_character("Massive Badger")
    print(world.get_monster_list())  # -> []
    print()

    print("Su sõber ütleb: \"Kui kõik need testid andsid sinu koodiga sama tulemuse "
          "mille ma siin ette kirjutasin, peaks kõik okei olema, proovi testerisse pushida! \" ")

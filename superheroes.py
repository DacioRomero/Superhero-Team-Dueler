import random

class Ability:
    def __init__(self, name, attack_strength):
        self.name = name
        self.attack_strength = attack_strength

    def attack(self):
        attack_lowest = self.attack_strength // 2
        attack_value = random.randint(attack_lowest, self.attack_strength)
        return attack_value

    def update_attack(self, attack_strength):
        self.attack_strength = attack_strength

class Weapon(Ability):
    def attack(self):
        return random.randint(0, self.attack_strength)

class Hero:
    def __init__(self, name):
        self.abilities = list()
        self.name = name

    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        attack_value = 0

        for ability in self.abilities:
            attack_value += ability.attack()

        return attack_value

class Team:
    def __init__(self, team_name):
        self.name = team_name
        self.heroes = list()

    def add_hero(self, hero):
        self.heroes.append(hero)

    def remove_hero(self, name):
        hero = self.find_hero(name)
        
        if hero:
            self.heroes.remove(hero)
        else:
            return 0

    def find_hero(self, name):
        for hero in self.heroes:
            if hero.name == name:
                return hero

        return 0

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)

if __name__ == "__main__":
    hero = Hero("Wonder Woman")
    print(hero.attack())
    ability = Ability("Divine Speed", 300)
    hero.add_ability(ability)
    print(hero.attack())
    new_ability = Ability("Super Human Strength", 800)
    hero.add_ability(new_ability)
    print(hero.attack())

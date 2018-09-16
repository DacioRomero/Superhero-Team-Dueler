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

if __name__ == "__main__":
    hero = Hero("Wonder Woman")
    print(hero.attack())
    ability = Ability("Divine Speed", 300)
    hero.add_ability(ability)
    print(hero.attack())
    new_ability = Ability("Super Human Strength", 800)
    hero.add_ability(new_ability)
    print(hero.attack())

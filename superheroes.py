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
    def __init__(self, name, health=100):
        self.abilities = []
        self.name = name
        self.armors = []
        self.start_health = health
        self.health = health
        self.deaths = 0
        self.kills = 0

    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        attack_value = 0

        for ability in self.abilities:
            attack_value += ability.attack()

        return attack_value

    def defend(self):
        if self.health == 0:
            return 0
        else:
            defense = sum(armor.defend() for armor in self.armors)
            return defense

    def take_damage(self, damage_amt):
        self.health -= damage_amt

        if self.health <= 0:
            self.health = 0
            self.deaths += 1

    def add_kill(self, num_kills):
        self.kills += num_kills

    def add_armor(self, armor):
        self.armors.append(armor)


class Team:
    def __init__(self, team_name):
        self.name = team_name
        self.heroes = []

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

    def attack(self, other_team):
        team_attack = sum(hero.attack() for hero in self.heroes)
        kills = other_team.defend(team_attack)

        for hero in self.heroes:
            hero.add_kill(kills)

    def defend(self, damage_amt):
        defense = sum(hero.defend() for hero in self.heroes)
        damage = damage_amt - defense

        if damage < 0:
            return 0

        return self.deal_damage(damage)

    def deal_damage(self, damage):
        team_damage = damage // len(self.heroes)
        dead_heroes = 0

        for hero in self.heroes:
            hero.take_damage(team_damage)

            if hero.health == 0:
                dead_heroes += 1

        return dead_heroes

    def revive_heroes(self):
        for hero in self.heroes:
            hero.health = hero.start_health

    def stats(self):
        for hero in self.heroes:
            print('{}: {} kills(s), {} death(s), {} health'
                  .format(hero.name, hero.kills, hero.deaths, hero.health))

    def is_alive(self):
        return any(hero.health > 0 for hero in self.heroes)

    def update_kills(self):
        pass

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)


class Armor:
    def __init__(self, name, defense):
        self.name = name
        self.defense = defense

    def defend(self):
        return random.randint(0, self.defense)


class Arena:
    def __init__(self):
        self.team_one = None
        self.team_two = None

    def build_team_one(self):
        self.team_one = Arena.build_team()

    def build_team_two(self):
        self.team_two = Arena.build_team()

    @staticmethod
    def build_team():
        team = Team(input_eof('Team name: '))

        for _ in range(int(input_eof('How many heroes? '))):
            print('-' * 32)

            hero = Hero(input_eof('Hero name: '))

            for _ in range(int(input_eof('How many abilities? '))):
                ability_name = input_eof('Ability name: ')
                ability_strength = int(input_eof('Strength: '))

                if input_eof('Weapon (y/n)? ') == 'y':
                    hero.add_ability(Weapon(ability_name, ability_strength))
                else:
                    hero.add_ability(Ability(ability_name, ability_strength))

            team.add_hero(hero)

        return team

    def team_battle(self):
        turn = 0

        while(self.team_one.is_alive() and self.team_two.is_alive()):
            print('Turn', turn)
            self.show_stats()

            if turn % 2 == 0:
                self.team_one.attack(self.team_two)
            else:
                self.team_two.attack(self.team_one)

            turn += 1
            input_eof('Press ENTER to continue')

        self.show_stats()

        if(self.team_one.is_alive()):
            print('Team 1 wins!')
        else:
            print('Team 2 wins!')

    def show_stats(self):
        print('Team:', self.team_one.name)
        self.team_one.stats()
        print('Team:', self.team_two.name)
        self.team_two.stats()


def input_eof(prompt=''):
    try:
        return input(prompt)
    except EOFError:
        return input_eof()


if __name__ == '__main__':
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    # Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:
        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        # Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            # Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()

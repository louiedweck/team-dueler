import random


class Ability:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        random_value = random.randint(0, self.max_damage)
        return random_value


class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        random_value = random.randint(0, self.max_block)
        return random_value


class Hero:
    def __init__(self, name, starting_health=100):
        '''Instance properties:
         abilities: List
         armors: List
         name: String
         starting_health: Integer
         current_health: Integer
     '''
        self.abilities = []
        self.armor = []
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.deaths = 0
        self.kills = 0

    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        '''Calculate the total damage from all ability attacks.
          return: total_damage:Int
        '''
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def add_armor(self, armor):
        self.armor.append(armor)

    def defend(self, damage_amt):
        total_blocked = 0
        for armor in self.armor:
            total_blocked += armor.block()
        return total_blocked

    def take_damage(self, damage):
        self.current_health -= damage

    def add_kill(self, num_kills):
        self.kills += num_kills

    def add_death(self, num_deaths):
        self.deaths += num_deaths

    def is_alive(self):
        if self.current_health > 0:
            return True
        else:
            return False

    def fight(self, opponent):
        if len(self.abilities) == 0 and len(opponent.abilities) == 0:
            print("Draw!")
        else:
            while self.is_alive() and opponent.is_alive():
                self.take_damage(opponent.attack())
                opponent.take_damage(self.attack())
                if not opponent.is_alive():
                    print(self.name + " defeated", opponent.name + '!')
                    self.add_kill(1)
                    opponent.add_death(1)
                    return self.name
                elif not self.is_alive():
                    print(opponent.name + " defeated", self.name + '!')
                    opponent.add_kill(1)
                    self.add_death(1)
                    return opponent.name

    def add_weapon(self, weapon):
        '''Add weapon to self.abilities'''
        # TODO: This method will append the weapon object passed in as an
        # argument to self.abilities.
        # This means that self.abilities will be a list of
        # abilities and weapons.
        self.abilities.append(weapon)


class Weapon(Ability):
    def attack(self):
        """  This method returns a random value
       between one half to the full attack power of the weapon.
       """
        return random.randint(self.max_damage//2, self.max_damage)


class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = list()

    def remove_hero(self, name):
        '''Remove hero from heroes list.
        If Hero isn't found return 0.
        '''
        foundHero = False
    # loop through each hero in our list
        for hero in self.heroes:
            # if we find them, remove them from the list
            if hero.name == name:
                self.heroes.remove(hero)
            # set our indicator to True
                foundHero = True
    # if we looped through our list and did not find our hero,
    # the indicator would have never changed, so return 0
        if not foundHero:
            return 0

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero)

    def add_heroes(self, hero):
        '''Add Hero object to self.heroes.'''
        self.heroes.append(hero)

    def stats(self):
        '''Print team statistics'''
        for hero in self.heroes:
            kd = hero.kills / hero.deaths
            print("{} Kill/Deaths:{}".format(hero.name, kd))

    def revive_heroes(self):
        for hero in self.heroes:
            if hero.is_alive() == False:
                hero.current_health == hero.starting_health

    def fight(self, opponent_team):
        living_heroes = []
        living_opponents = []

        for hero in self.heroes:
            living_heroes.append(hero)

        for hero in opponent_team.heroes:
            living_opponents.append(hero)

        while len(living_opponents) > 0 and len(living_heroes) > 0:
            hero = random.choice(living_heroes)
            opponent = random.choice(living_opponents)
            if hero.is_alive() and opponent.is_alive():
                hero.fight(opponent)


class Arena:
    def init(self, team_1, team_2):
        self.team_1 = []
        self.team_2 = []

    def create_ability(self):
        name = input("What is the ability name?  ")
        max_damage = int(input(
            "What is the max damage of the ability?  "))

        return Ability(name, max_damage)

    def create_weapon(self):
        name = input("What is the weapon's name?  ")
        max_damage = int(input(
            "What is the max damage of the weapon?  "))

        return Weapon(name, max_damage)

    def create_armor(self):
        name = input("What is the weapon's name?  ")
        max_block = int(input(
            "What is the max block of the armor?  "))

        return Armor(name, max_block)

    def create_hero(self):
        hero_name = input("Hero's name: ")
        hero = Hero(hero_name)
        add_item = None
        while add_item != "4":
            add_item = input(
                "[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
            if add_item == '1':
                hero.add_ability(self.create_ability())
            if add_item == '2':
                hero.add_weapon(self.create_weapon())
            if add_item == '3':
                hero.add_armor(self.create_armor())
            else:
                return hero

    def build_team_1(self):
        '''Prompt the user to build team_one '''
        # Using a loop to call self.create_hero() for the number
        # of heroes the user specified the team should have,
        # and then add the heroes to the team.
        self.team_1 = input("Enter a team name for team 1: ")
        num_heroes = int(input("Enter how many heroes this team has: "))
        for i in range(0, num_heroes):
            self.team_1.heroes.append(self.create_hero())

    def build_team_2(self):
        self.team_2 = input("Enter a team name for team 2: ")
        num_heroes = int(input("Enter how many heroes this team has: "))
        for i in range(0, num_heroes):
            self.team_2.heroes.append(self.create_hero())

    def team_battle(self):
        '''Battle team_one and team_two together.'''
        # TODO: This method should battle the teams together.
        # Call the attack method that exists in your team objects
        # for that battle functionality.
        pass


if __name__ == "__main__":
    # hero = Hero("Grace Hopper", 200)
    # hero.take_damage(150)
    # print(hero.is_alive())
    # hero.take_damage(15000)
    # print(hero.is_alive())
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 50)
    ability2 = Ability("Super Eyes", 50)
    ability3 = Ability("Wizard Wand", 50)
    ability4 = Ability("Wizard Beard", 50)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)
    # hero = Hero("Wonder Woman")
    # weapon = Weapon("Lasso of Truth", 90)
    # hero.add_weapon(weapon)
    # print(hero.attack())

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
                if self.is_alive():
                    print(self.name + " defeated", opponent.name + '!')
                    self.add_kill(1)
                    opponent.add_death(1)
                    return self.name
                elif opponent.is_alive():
                    print(opponent.name + " defeated", self.name + '!')
                    opponent.add_kill(1)
                    self.add_death(1)
                    return opponent.name

    def add_weapon(self, weapon):
        '''Add weapon to self.abilities'''
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
        self.heroes = []

    def __repr__(self):
        return self.name

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
            print(f"{hero.name} Kill/Deaths:{kd}")

    def revive_heroes(self):
        for hero in self.heroes:
            if hero.is_alive() == False:
                hero.current_health == hero.starting_health

    def fight(self, opponent_team):
        living_heroes = list()
        living_opponents = list()

        for hero in self.heroes:
            living_heroes.append(hero)

        for hero in opponent_team.heroes:
            living_opponents.append(hero)

        while len(living_opponents) > 0 and len(living_heroes) > 0:
            hero = random.choice(living_heroes)
            opponent = random.choice(living_opponents)
            if hero.is_alive() and opponent.is_alive():
                hero.fight(opponent)
                if hero.is_alive():
                    return hero
                else:
                    return opponent


class Arena:
    def init(self, team_1, team_2):
        self.team_1 = team_1
        self.team_2 = team_2

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
        add_item = ['1', '2', '3', '4']
        while add_item != '4':
            add_item = input(
                "[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
            if add_item == '1':
                hero.add_ability(self.create_ability())
            elif add_item == '2':
                hero.add_weapon(self.create_weapon())
            elif add_item == '3':
                hero.add_armor(self.create_armor())
            else:
                return hero

    def build_team_1(self):
        '''Prompt the user to build team_one '''
        self.team_1 = Team(input("Enter a team name for team 1: "))
        num_heroes = int(input("Enter how many heroes this team has: "))
        for _ in range(0, num_heroes):
            self.team_1.heroes.append(self.create_hero())

    def build_team_2(self):
        self.team_2 = Team(input("Enter a team name for team 2: "))
        num_heroes = int(input("Enter how many heroes this team has: "))
        for _ in range(0, num_heroes):
            self.team_2.heroes.append(self.create_hero())

    def team_battle(self):
        self.team_1.fight(self.team_2)
        return "hi"

    def who_is_alive(self):
        living_heroes_team_1 = []
        living_heroes_team_2 = []
        for hero in self.team_1.heroes:
            if hero.is_alive():
                living_heroes_team_1.append(hero)
        for hero in self.team_2.heroes:
            if hero.is_alive():
                living_heroes_team_2.append(hero)
        if len(living_heroes_team_1) > len(living_heroes_team_2):
            print(f"{self.team_1}'s team is the winner!")
        else:
            print(f"{self.team_2}'s team is the winner!")

    def get_team_stats(self, team):
        total_kills = sum(hero.kills for hero in team.heroes)
        total_deaths = sum(hero.deaths for hero in team.heroes)
        return total_kills, total_deaths


def make_teams(num_teams=2):
    team_names = [
        'Ikey', 'Louie', 'Jake', 'Marvel', 'DC',
    ]
    hero_names = [
        'Dr.Manhattan', 'Alan Moore', 'Silk-Spectre',
        'Nite-Owl', 'Ozymandias', 'Rorschach', 'Comedian', 'Iron-Man', 'Cap',
        'Spider-Man', 'Thanos', 'Pickachu', 'Charizard', 'Squirtle'
    ]
    abilities = [
        'Laser Vision', 'Ninja stars', 'Shrimp Rain'
    ]
    teams = []
    for _ in range(num_teams):
        t = Team(random.choice(team_names))
        t.heroes = [Hero(random.choice(hero_names)) for _ in range(5)]
        for hero in t.heroes:
            hero.add_ability(Ability(random.choice(
                abilities), random.randint(0, 100)))
        teams.append(t)
    return teams


if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    # Build Teams
    team_1, team_2 = make_teams()
    arena.team_1 = team_1
    arena.team_2 = team_2

    while game_is_running:

        arena.team_battle()
        team_1_kills, team_1_deaths = arena.get_team_stats(arena.team_1)
        team_2_kills, team_2_deaths = arena.get_team_stats(arena.team_2)
        print(f'''
        Stats:
                  |  Kills   |  Deaths 
        {arena.team_1.name.center(10, ' ')}|{str(team_1_kills).center(10, ' ')}|{str(team_1_deaths).center(10, ' ')}
        {arena.team_2.name.center(10, ' ')}|{str(team_2_kills).center(10, ' ')}|{str(team_2_deaths).center(10, ' ')}
        ''')
        arena.who_is_alive()
        play_again = input("Play Again? Y or N: ")

        # Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            # Revive heroes to play again
            arena.team_1.revive_heroes()
            arena.team_2.revive_heroes()
    # hero1 = Hero("Wonder Woman")
    # hero2 = Hero("Dumbledore")
    # ability1 = Ability("Super Speed", 50)
    # ability2 = Ability("Super Eyes", 50)
    # ability3 = Ability("Wizard Wand", 50)
    # ability4 = Ability("Wizard Beard", 50)
    # hero1.add_ability(ability1)
    # hero1.add_ability(ability2)
    # hero2.add_ability(ability3)
    # hero2.add_ability(ability4)
    # hero1.fight(hero2)

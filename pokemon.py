# Crea una classe Pokemon coi seguenti attributi:
# Nome, Salute e Forza.
# Implementa un metodo di attacco che permetta
# a un Pokemon di attaccarne un altro,
# riducendo la Salute dell'avversario.
# (al metodo passeremo come argomento un oggetto Pokemon)
# La Salute dell'avversario viene ridotta
# di un valore pari alla Forza dell'attaccante.
# Il metodo infine stampa un messaggio,
# con alcuni dettagli sull'attacco, ad esempio:
# Pikachu attacca Charizard causando 15 danni!

# Completata la classe, istanzia due Pokemon
# e falli attaccare l'un l'altro, quante volte desideri.
# Dopo il combattimento, stampa la Salute
# di entrambi, per vedere se è coerente con gli attacchi.

import random

attacchi = {
    "fire": {
        "water": 0.6,
        "electric": 1,
        "grass": 1.4,
        "fire": 1
    },
    "electric": {
        "water": 1.4,
        "grass": 0.6,
        "fire": 1,
        "electric": 1
    },
    "grass": {
        "fire": 0.6,
        "water": 1.4,
        "electric": 1,
        "grass": 1
    },
    "water": {
        "fire": 1.4,
        "grass": 0.6,
        "electric": 0.6,
        "water": 1
    }
}

class Pokemon:
    def __init__(self, name, of_type, health, power):
        self.name = name
        self.health = health
        self.power = power
        self.of_type = of_type

    def attack(self, pokemon):
     new_power = self.power * attacchi[self.of_type][pokemon.of_type]
     pokemon.health -= new_power
     print(f"{self.name} attack {pokemon.name} doing to it a damage of {new_power} health points")
     print(f"Now the {pokemon.name} health is of {pokemon.health} points")



pokemon_dict = {
    "blastoise": Pokemon("Blastoise", "water", 500, 50),
    "charizard": Pokemon("Charizard", "fire", 390, 60),
    "pikachu": Pokemon("Pikachu", "electric", 210, 35),
    "moltres": Pokemon("Moltres", "fire", 400, 70),
    "venosaur": Pokemon("Venosaur", "grass", 520, 55),
    "bulbasaur": Pokemon("Bulbasaur", "grass", 190, 30),
    "zapdos": Pokemon("Zapdos", "electric", 430, 68),
    "squirtle": Pokemon("Squirtle", "water", 200, 38)
}

choose = input(f"Hi dear champion! Choose one Pokemon and start the battle! Type its name:\n" 
               + "\n".join(pokemon_dict.keys()) + "\n").lower()

while choose not in pokemon_dict:
        print("Invalid Pokémon name. Please choose again.")

chosen_pokemon = pokemon_dict[choose]
print(f"Congratulation, nice move! You have chose {chosen_pokemon.name}")
computer_pokemon = random.choice(list(pokemon_dict.values()))
print(f"The computer chose {computer_pokemon.name}! Be carefull!")
      
while chosen_pokemon.health > 0 and computer_pokemon.health > 0:
      chosen_pokemon.attack(computer_pokemon)

      if computer_pokemon.health <= 0:
            print(f"{computer_pokemon.name} has been defeated! You have win!")
            defeat = True 
            break

      computer_pokemon.attack(chosen_pokemon)

      if chosen_pokemon.health <= 0:
            print(f"{chosen_pokemon.name} has been defeated! You have loose!")
            defeat = True
            break

      next_or_quit = int(input((f"Do you have attack {computer_pokemon.name}! Did you want go next or quit? Press 2 for quit or other for don't\n")))
      if next_or_quit == 2:
          print(f"Bye Bye!")
          break



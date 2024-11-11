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

class Pokemon:
    def __init__(self, name, of_type, health, power):
        self.name = name
        self.health = health
        self.power = power
        self.of_type = of_type

    def attack(self, pokemon):
     damage = self.power #danno base
     if self.of_type == "water" and pokemon.of_type == "fire":
        damage  *= 1.4 #applica il 40% del danno in più
        print(f"That luck {self.name}, {pokemon.name} is {pokemon.of_type} type ! Your damage is 40% more!")
     elif self.of_type == "water" and pokemon.of_type == "electric":
        damage  *= 0.6 #applica solo il 60% del danno
        print(f"That unluck {self.name}, {pokemon.name} is {pokemon.of_type} type ! Your damage is less than 40%!")
     elif self.of_type == "water" and pokemon.of_type == "grass":
        damage  *= 0.6 
        print(f"That unluck {self.name}, {pokemon.name} is {pokemon.of_type} type ! Your damage is less than 40%!")
     elif self.of_type == "fire" and pokemon.of_type == "grass":
        damage  *= 1.4 
        print(f"That luck {self.name}, {pokemon.name} is {pokemon.of_type} type ! Your damage is 40% more!")
     elif self.of_type == "fire" and pokemon.of_type == "water":
        damage  *= 0.6 
        print(f"That unluck {self.name}, {pokemon.name} is {pokemon.of_type} type ! Your damage is less than 40%!")    
     elif self.of_type == "grass" and pokemon.of_type == "water":
        damage  *= 1.4 
        print(f"That luck {self.name}, {pokemon.name} is {pokemon.of_type} type ! Your damage is 40% more!")
     elif self.of_type == "grass" and pokemon.of_type == "fire":
        damage  *= 0.6 
        print(f"That unluck {self.name}, {pokemon.name} is {pokemon.of_type} type ! Your damage is less than 40%!")    
     elif self.of_type == "electric" and pokemon.of_type == "water":
        damage  *= 1.4 
        print(f"That luck {self.name}, {pokemon.name} is {pokemon.of_type} type ! Your damage is 40% more!")
     elif self.of_type == "electric" and pokemon.of_type == "grass":
        damage *= 0.6 
        print(f"That unluck {self.name}, {pokemon.name} is {pokemon.of_type} type ! Your damage is less than 40%!")
        
     pokemon.health -= damage 
     print(f"{self.name} attack {pokemon.name} doing to it a damage of {damage} health points")
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

defeat = False

while not defeat:
   choose = input(f"Hi dear champion! Choose one Pokemon and start the battle! Type its name:\n" 
               + "\n".join(pokemon_dict.keys()) + "\n").lower()

   if choose in pokemon_dict:
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

        elif chosen_pokemon.health <= 0:
            print(f"{chosen_pokemon.name} has been defeated! You have loose!")
            defeat = True
            break

        next_or_quit = int(input((f"Do you have attack {computer_pokemon.name}! Did you want go next or quit? Press 1 or 2\n")))
        if next_or_quit == 1:
            computer_pokemon.attack(chosen_pokemon)
        elif next_or_quit == 2:
            print(f"Bye Bye!")
            break

   else:
        print("Invalid Pokémon name. Please choose again.")

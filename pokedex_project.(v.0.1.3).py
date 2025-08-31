#********************************************************************************************************************
#*                                                      $$\                                                         *
#*                                                      $$ |                                                        *
#*    $$$$$$\$$$$\  $$\   $$\  $$$$$$$\  $$$$$$\   $$$$$$$ | $$$$$$\      $$$$$$\  $$\   $$\  $$$$$$\               *
#*    $$  _$$  _$$\ $$ |  $$ |$$  _____|$$  __$$\ $$  __$$ |$$  __$$\    $$  __$$\ \$$\ $$  |$$  __$$\              *
#*    $$ / $$ / $$ |$$ |  $$ |$$ /      $$ /  $$ |$$ /  $$ |$$$$$$$$ |   $$$$$$$$ | \$$$$  / $$$$$$$$ |             *
#*    $$ | $$ | $$ |$$ |  $$ |$$ |      $$ |  $$ |$$ |  $$ |$$   ____|   $$   ____| $$  $$<  $$   ____|             *
#*    $$ | $$ | $$ |\$$$$$$$ |\$$$$$$$\ \$$$$$$  |\$$$$$$$ |\$$$$$$$\ $$\\$$$$$$$\ $$  /\$$\ \$$$$$$$\              *
#*    \__| \__| \__| \____$$ | \_______| \______/  \_______| \_______|\__|\_______|\__/  \__| \_______|             *
#*                  $$\   $$ |                                                                                      *
#*                  \$$$$$$  |                                                                                      *
#*                   \______/                                                                                       *
#*                                                                                                                  *
#********************************************************************************************************************
#
# Name: pokedex_project
# Version: v0.1.3
# Builder: mycode.exe
#
#   Potential Components:
#   [ ] - Use 'tkinter' for GUI, styled like the real Pokedex from the show
#   [x] - Have Pokemon's entries tied to other pokemon (if they are evolutions)
#   [ ] - Allow comparisons of Pokemon's stats (Height & Weights)
#   [ ] - Allow sorting/grouping of Pokemon by type & by weaknessess
#   [ ] - 
#   [ ] - 
#   [ ] - 
#   [ ] - 
#
#   Thoughts & Ideas:
#       - Used to experiment with 'tkinter' module for GUI
#       - 
#
#   References:
#       - https://www.pokemon.com/uk/pokedex
#       - For later image addition: https://stackoverflow.com/questions/53438133/using-an-image-as-an-class-object-attribute-then-opening-that-image-in-a-tkinte
#       - https://www.geeksforgeeks.org/python/how-to-add-an-image-in-tkinter/
#
#
#
#********************************************************************************************************************

class Pokemon:
    def __init__(self,
                 name: str,
                 pokedex_number:str,
                 height: float,
                 weight: float,
                 category: str,
                 abilities: list[str],
                 type: list[str],
                 weaknesses : list[str],
                 pre_evolution,
                 evolution,
                 image):
        self.name = name
        self.pokedex_number = pokedex_number
        self.height = height # in Metres (Format: float)
        self.weight = weight # in Kilograms (Format: float)
        self.category = category
        self.abilities = abilities # Use a [ list ]
        self.type = type # Use a [ list ]
        self.weaknesses = weaknesses # Use a [ list ]
        self.pre_evolution = pre_evolution # If n/a - Mark as ' None '
        self.evolution = evolution # If n/a - Mark as ' None '
        self.image = image # Pokedex image stored in 'pokedex_images' folder
    
    def __str__(self) -> str:
        return f"{self.name} is {self.height} metres tall, and weighs {self.weight} kilograms. It is a {self.type} and is weak against {self.weaknesses} types."
    
    def __repr__(self) -> str:
        return f'Pokemon(name="{self.name}", pokdex_numer="{self.pokedex_number}, height="{self.height}, weight="{self.height}, category="{self.category}, abilities="{self.abilities}, type="{self.type}, weaknesses={self.weaknesses}, pre_evolution="{self.pre_evolution}, evolution="{self.evolution})'
    
    

# Pokemon "data"
# region Data
bulbasaur = Pokemon("Bulbasaur", "0001", 0.7, 6.9, "Seed", ["Overgrow"], ["Grass", "Poison"], ["Fire", "Ice", "Flying", "Psychic"], None, "ivysaur", ...)
ivysaur = Pokemon("Ivysaur", "0002", 1.0, 13.0, "Seed", ["Overgrow"], ["Grass", "Poison"], ["Fire", "Ice", "Flying", "Psychic"], bulbasaur, "venusaur", ...)
venusaur = Pokemon("Venusaur", "0003", 2.0, 100.0, "Seed", ["Overgrow"], ["Grass", "Poison"], ["Fire", "Ice", "Flying", "Psychic"], ivysaur, None, ...)
charmander = Pokemon("Charmander", "0004", 0.6, 8.5, "Lizard", ["Blaze"], ["Fire"], ["Water", "Ground", "Rock"], None, "charmeleon", ...)
charmeleon = Pokemon("Charmeleon", "0005", 1.1, 19.0, "Flame", ["Blaze"], ["Fire"], ["Water", "Ground", "Rock"], charmander, "charizard", ...)
charizard = Pokemon("Charizard", "0006", 1.7, 90.5, "Flame", ["Blaze"], ["Fire"], ["Water", "Ground", "Rock"], "charmeleon", None, ...)
squirtle = Pokemon("Squirtle", "0007", 0.5, 9.0, "Tiny Turtle", ["Torrent"], ["Water"], ["Grass", "Electric"], None, "wartortle", ...)
wartortle = Pokemon("Wartortle", "0008", 1.7, 90.5, "Turtle", ["Torrent"], ["Water"], ["Grass", "Electric"], squirtle, "blastoise", ...)
blastoise = Pokemon("Blastoise", "0009", 1.7, 90.5, "Shellfish", ["Torrent"], ["Water"], ["Grass", "Electric"], "wartortle", None, ...) 
caterpie = Pokemon("Caterpie", "0010", 0.3, 2.9, "Worm", ["Shield Dust"], ["Bug"], ["Fire", "Flying", "Rock"], None, "metapod", ...) 
metapod = Pokemon("Metapod", "0011", 0.7, 9.9, "Cocoon", ["Shed Skin"], ["Bug"], ["Fire", "Flying", "Rock"], caterpie, "butterfree", ...)
butterfree = Pokemon("Butterfree", "0012", 1.1, 32.0, "Butterfly", ["Compound Eyes"], ["Bug", "Flying"], ["Fire", "Electric", "Ice", "Flying", "Rock"], metapod, None, ...)
weedle = Pokemon("Weedle", "0013", 0.3, 3.2, "Hairy Bug", ["Shield Dust"], ["Bug", "Poison"], ["Fire", "Flying", "Psychic", "Rock"], None, "kakuna", ...)
kakuna = Pokemon("Kakuna", "0014", 0.6, 10.0, "Cocoon", ["Shed Skin"], ["Bug", "Poison"], ["Fire", "Flying", "Psychic", "Rock"], weedle, "beedrill", ...)
beedrill = Pokemon("Beedrill", "0015", 1.0, 29.5, "Poison Bee", ["Swarm"], ["Bug", "Poison"], ["Fire", "Flying", "Psychic", "Rock"], kakuna, None, ...)
#endregion

# Pokemon "Data" into a dictionary
pokemon_database = {
    "bulbasaur" : bulbasaur,
    "ivysaur" : ivysaur,
    "venusaur" : venusaur,
    "charmander" : charmander,
    "charmeleon" : charmeleon,
    "charizard" : charizard,
    "squirtle" : squirtle,
    "wartortle" : wartortle,
    "blastoise" : blastoise,
    "caterpie" : caterpie,
    "metapod" : metapod,
    "butterfree" : butterfree,
    "weedle" : weedle,
    "kakuna" : kakuna,
    "beedrill" : beedrill
    }

# Debugging test - See which Pokemon were updateds
updated_pokemon_list: list = []

print(f"Bulbasaur evolves into {bulbasaur.evolution}, then it evolves eventually into {ivysaur.evolution}.")

# Automatically update any Pokemon's evolutions to link to the correct variable
def update_evolutions(pokemon_database):
    for pkmon in pokemon_database.values():
        if pkmon.evolution:
            pkmon.evolution = pokemon_database[pkmon.evolution]
            updated_pokemon_list.append(pkmon.evolution.name) # Adds the 

update_evolutions(pokemon_database)


print(bulbasaur.evolution.name)
print(f"Bulbasaur evolves into {bulbasaur.evolution.name}, then it evolves eventually into {ivysaur.evolution.name}.")

print(updated_pokemon_list)


#for key, value in pokemon_database.items():
#    if type(value.evolution) == str:
#        print(value.name)





"""
    Update Message/Notes (v0.1.3):
        - Figured out how to iterate over the dictionary and print out the necessary parts of the Pokemon class' objects that I'm looking to edit in the future. Now just to learn how to adjust those variables.
        - Changed the dictionary to store the pokemon by their names as their key, to mean that the loop to update evolutions *finally* works.
        - Also added a list for me to see which Pokemon were updated, and see if any obvious misses were made.
        - Learn that '__str__' and '__repr__' are useful tools when building a class, with 'str' being more useful for user, and 'repr' useful for developer. Added 'repr' method to display variable's instance rather than memory address for better clarity while I create the program. 

"""  


"""
    Research/Self-Ed/Realisations;
        - Unusure if to use '__repr__()' or '__str__()' to display class string objects
        - Need to specify <.evolution.name> when calling for Pokemon's pre & evolutions, to avoid getting <object at 0x00000...> etc.


"""


"""
        ** Code Graveyard **

# Blank Pokedex Entry
# = Pokemon("", "00", ., ., "", "", "", "", False, False)
# = Pokemon("", "00", 0.0, 0.0, "", "", ""+"", ""+"", False, False)


# Attribute Testing/Debugging code
print(ivysaur.pokedex_number)
print(ivysaur.evolution.name)
print(ivysaur.evolution.pokedex_number)
print(f"Ivysaur's evolution is {ivysaur.evolution.name}, and it's pre-evolution is {ivysaur.pre_evolution.name}") 

for x in pokemon_db:
    if pokemon_db.evolution is str:
        print("success")





pokemon_db = [bulbasaur, ivysaur, venusaur, charmander, charmeleon, charizard, squirtle, wartortle, blastoise]

pokemon_list = [bulbasaur, ivysaur, venusaur, charmander, charmeleon, charizard, squirtle, wartortle, blastoise]

pokemon_dict = {
    "0001" : bulbasaur,
    "0002" : ivysaur,
    "0003" : venusaur,
    "0004" : charmander,
    "0005" : charmeleon,
    "0006" : charizard,
    "0007" : squirtle,
    "0008" : wartortle,
    "0009" : blastoise}
    
    
pokemon_list = [bulbasaur, ivysaur, venusaur, charmander, charmeleon, charizard, squirtle, wartortle, blastoise]



print(pokemon_list.self.name())
for p in pokemon_list:
    if p.evolution == str in pokemon_list:
        print(Pokemon.HasEvolution)

#*********************************************************************************************************************************************************************************************************************
# Evolution Manual Updates
# region Data
'''
bulbasaur.evolution = ivysaur
ivysaur.evolution = venusaur 
charmander.evolution = charmeleon
charmeleon.evolution = charizard 
squirtle.evolution = wartortle
wartortle.evolution = blastoise
caterpie.evolution = metapod
metapod.evolution = butterfree
weedle.evolution = kakuna
kakuna.evolution = beedrill

'''
# endregion



# Evolution Manual Updates - Checking
'''
print(type(ivysaur.evolution)) # Output: <class 'str'>
print(ivysaur.evolution) # Output: venusaur 

# Evolution updates to object's attributes
ivysaur.evolution = venusaur # Changes the ivysaur .evolution object's attribute to the venusaur
charmeleon.evolution = charizard # Same idea for Charmeleon
wartortle.evolution = blastoise # And same again for Wartortle

print(ivysaur.pokedex_number) # Output: 0002
print(ivysaur.evolution.name) # Output: Venusaur
print(ivysaur.evolution.pokedex_number) # Output: 0003
print(f"Ivysaur's evolution is {ivysaur.evolution.name}, and it originally evolves from {ivysaur.pre_evolution.name}.") # Output: Ivysaur's evolution is Venusaur, and it originally evolves from Bulbasaur.
        
        
#*********************************************************************************************************************************************************************************************************************
        
# Failed iterators to go through the database for the pokedex and update it if needed
def evolution_needs_updating_1():
    for Pokemon in pokemon_db:
        if Pokemon.evolution in pokemon_db is type(str):
            print("Pokemon evolution needs updating")
        print("Correct evoltuion in place")

evolution_needs_updating_1()

def evolution_needs_updating_2():
    for Pokemon in pokemon_db:
        if Pokemon_db.evolution is str:
            print("Pokemon evolution needs updating")

evolution_needs_updating_2()

for pokemon in pokemon_db:
    if pokemon.evolution == str in pokemon_db:
        print(Pokemon.HasEvolution)
        

for p in pokemon_db.values():
    display_name = Pokemon.name()
    print(display_name)
    print(p)

for key, value in pokemon_database.items():
    if type(value.evolution) == str:
        for poke in pokemon_database:
            i2prop = getattr(pokemon_database, poke)
            if getattr(value.evolution, poke) != i2prop:
                setattr(value.name, poke, i2prop)
                print(value.evolution)
#        print(value.name)
#    print(value.weaknesses)
#    if Pokemon.height <= 1.5:
#        print(Pokemon.name)



# ** StackOverflow Potential Solutions:
# ** StackOverflow Question Post: https://stackoverflow.com/questions/79748293/how-to-update-string-attributes-to-object-instances-if-they-exist/79748343


# ** From "Neil Butcher";
#########################################################################


pokemon_db = {
    "0001" : bulbasaur,
    "0002" : ivysaur,
    "0003" : venusaur,
    "0004" : charmander,
    "0005" : charmeleon,
    "0006" : charizard,
    "0007" : squirtle,
    "0008" : wartortle,
    "0009" : blastoise}

def updated_evolution(current_evolution):
    for pokemon in pokemon_db :
        if pokemon.name == current_evolution:
            return pokemon
    return current_evolution
    

for key, pokemon in pokemon_db.items():
    pokemon.evolution = updated_evolution(pokemon.evolution)

#########################################################################




# ** From "Marce Puente";
#########################################################################
pokes = {
    "bulbasaur" : bulbasaur,
    "ivysaur" : ivysaur,
    "venusaur" : venusaur,
    "charmander" : charmander,
    "charmeleon" : charmeleon,
    "charizard" : charizard,
    "squirtle" : squirtle,
    "wartortle" : wartortle,
    "blastoise" : blastoise
}

def evolution_needs_updating():

      # we obtain the "keys" of "pokemon_db"
    keys = pokemon_db.keys()
 
    for key in keys:

          # obtain the "Pokemon"
        poke = pokemon_db.get(key)

          # only if "poke.evolution" is a string
        if type(poke.evolution) == str:
            print(f"Pokemon {poke.name} evolution needs updating")
               # we apply evolution
            poke.evolution = pokes.get(poke.evolution)
            print( f"  evolution -> {poke.evolution.name}")
        else:
            print( f"Pokemon {poke.name} correct evolution in place")
        print("N/A")

evolution_needs_updating()

#########################################################################




"""


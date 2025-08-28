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
# Version: v0.1.2
# Builder: mycode.exe
#
#   Potential Components:
#   [ ] - Use 'tkinter' for GUI, styled like the real Pokedex from the show
#   [ ] - Have Pokemon's entries tied to other pokemon (if they are evolutions)
#   [ ] - Allow comparisons of Pokemon's stats (Height & Weights)
#   [ ] - Allow sorting/grouping of Pokemon by type & by weaknessess
#   [ ] - 
#   [ ] - 
#   [ ] - 
#   [ ] - 
#
#   Thoughts & Ideas:
#       - Used to experiment with 'tkinter' module for GUI
#       - Need to research how best to store Pokemon's data (Class?)
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
    def __init__(self, name, pokedex_number, height, weight, category, abilities, type, weaknesses, pre_evolution, evolution, image):
        self.name = name
        self.pokedex_number = pokedex_number
        self.height = height # in Metres (Format: float)
        self.weight = weight # in Kilograms (Format: float)
        self.category = category
        self.abilities = abilities
        self.type = type
        self.weaknesses = weaknesses
        self.pre_evolution = pre_evolution # If n/a - Mark as ' False '
        self.evolution = evolution # If n/a - Mark as ' False '
        self.image = image # Pokedex image stored in 'pokedex_images' folder
    
    
    
    '''   
    def __repr__(self):
        return self.evolution
        return self.pre_evolution
    
    def HasPreEvolution(pokemon_db):
        for x in pokemon_db:
            if Pokemon.pre_evolution in pokemon_db:
                print()
    
    def HasEvolution(self):
        print(self.evolution)'''

# Pokemon "database"
# region Data
bulbasaur = Pokemon("Bulbasaur", "0001", 0.7, 6.9, "Seed", ["Overgrow"], ["Grass", "Poison"], ["Fire", "Ice", "Flying", "Psychic"], None, "ivysaur", ...)
ivysaur = Pokemon("Ivysaur", "0002", 1.0, 13.0, "Seed", ["Overgrow"], ["Grass", "Poison"], ["Fire", "Ice", "Flying", "Psychic"], bulbasaur, "venusaur", ...)
venusaur = Pokemon("Venusaur", "0003", 2.0, 100.0, "Seed", ["Overgrow"], ["Grass", "Poison"], ["Fire", "Ice", "Flying", "Psychic"], ivysaur, None, ...)
charmander = Pokemon("Charmander", "0004", 0.6, 8.5, "Lizard", ["Blaze"], ["Fire"], ["Water", "Ground", "Rock"], None, "charmeleon", ...)
charmeleon = Pokemon("Charmeleon", "0005", 1.1, 19.0, "Flame", ["Blaze"], ["Fire"], ["Water", "Ground", "Rock"], charmander, "charizard", ...)
charizard = Pokemon("Charizard", "0006", 1.7, 90.5, "Flame", ["Blaze"], ["Fire"], ["Water", "Ground", "Rock"], "charmeleon", None, ...)
squirtle = Pokemon("Squirtle", "0007", 0.5, 9.0, "Tiny Turtle", "Torrent", ["Water"], ["Grass", "Electric"], None, "wartortle", ...)
wartortle = Pokemon("Wartortle", "0008", 1.7, 90.5, "Turtle", "Torrent", ["Water"], ["Grass", "Electric"], squirtle, "blastoise", ...)
blastoise = Pokemon("Blastoise", "0009", 1.7, 90.5, "Shellfish", "Torrent", ["Water"], ["Grass", "Electric"], "wartortle", None, ...) 
caterpie = Pokemon("Caterpie", "0010", 0.3, 2.9, "Worm", "Shield Dust", ["Bug"], ["Fire", "Flying", "Rock"], None, "metapod", ...) 
metapod = Pokemon("Metapod", "0011", 0.7, 9.9, "Cocoon", "Shed Skin", ["Bug"], ["Fire", "Flying", "Rock"], caterpie, "butterfree", ...)
butterfree = Pokemon("Butterfree", "0012", 1.1, 32.0, "Butterfly", "Compound Eyes", ["Bug", "Flying"], ["Fire", "Electric", "Ice", "Flying", "Rock"], metapod, None, ...)
weedle = Pokemon("Weedle", "0013", 0.3, 3.2, "Hairy Bug", "Shield Dust", ["Bug", "Poison"], ["Fire", "Flying", "Psychic", "Rock"], None, "kakuna", ...)
kakuna = Pokemon("Kakuna", "0014", 0.6, 10.0, "Cocoon", "Shed Skin", ["Bug", "Poison"], ["Fire", "Flying", "Psychic", "Rock"], weedle, "beedrill", ...)
beedrill = Pokemon("Beedrill", "0015", 1.0, 29.5, "Poison Bee", "Swarm", ["Bug", "Poison"], ["Fire", "Flying", "Psychic", "Rock"], kakuna, None, ...)
#endregion

pokemon_db = {
    "0001" : bulbasaur,
    "0002" : ivysaur,
    "0003" : venusaur,
    "0004" : charmander,
    "0005" : charmeleon,
    "0006" : charizard,
    "0007" : squirtle,
    "0008" : wartortle,
    "0009" : blastoise,
    "0010" : caterpie,
    "0011" : metapod,
    "0012" : butterfree,
    "0013" : weedle,
    "0014" : kakuna,
    "0015" : beedrill
    }


# Evolution Manual Updates
# region Data
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
# endregion

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
'''






"""
    Update Message/Notes (v0.1.2):
        - Decided that I will need to allow each instance of the class to be created first, then circle the code back to tie up pre-evolutions/evolutions.
        - Added "# region Data" to tidy Pokemon database 
        - Decided to adjust the objects attributes manually, as after many hours of googling and trying to find a solution, I can't find one. And StackOverflow wasn't any help either. With my question posted just being met with "this doesn't make sense".
        - Before continuing with this project, I need to spend some serious time learning as much as I can about classes and related topics that might help me get my head around this, before moving onto the 'tkinter' aspect of the project

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

for p in pokemon_dict:
    if p.evolution in pokemon_dict:
        print(Pokemon.HasEvolution)
        
        
        
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


"""
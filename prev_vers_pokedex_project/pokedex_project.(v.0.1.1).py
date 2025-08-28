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
# Version: v0.1.1
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
        
#    def __repr__(self):
#        return self.evolution
#        return self.pre_evolution
    
#    def HasPreEvolution(pokemon_db):
#        for x in pokemon_db:
#            if Pokemon.pre_evolution in pokemon_db:
#                print()
                
    
    def HasEvolution(self):
        ...


# region Data
# Pokemon "database" 

bulbasaur = Pokemon("Bulbasaur", "0001", 0.7, 6.9, "Seed", "Overgrow", "Grass"+"Poison", "Fire"+"Ice"+"Flying"+"Psychic", None, "ivysaur", ...)
ivysaur = Pokemon("Ivysaur", "0002", 1.0, 13.0, "Seed", "Overgrow", "Grass"+"Poison", "Fire"+"Ice"+"Flying"+"Psychic", bulbasaur, "venusaur", ...)
venusaur = Pokemon("Venusaur", "0003", 2.0, 100.0, "Seed", "Overgrow", "Grass"+"Poison", "Fire"+"Ice"+"Flying"+"Psychic", ivysaur, None, ...)
charmander = Pokemon("Charmander", "0004", 0.6, 8.5, "Lizard", "Blaze", "Fire", "Water"+"Ground"+"Rock", None, "charmeleon", ...)
charmeleon = Pokemon("Charmeleon", "0005", 1.1, 19.0, "Lizard", "Blaze", "Fire", "Water"+"Ground"+"Rock", charmander, "charizard", ...)
charizard = Pokemon("Charizard", "0006", 1.7, 90.5, "Lizard", "Blaze", "Fire", "Water"+"Ground"+"Rock", "charmeleon", None, ...)
squirtle = Pokemon("Squirtle", "0007", 0.5, 9.0, "Tiny Turtle", "Torrent", "Water", "Grass"+"Electric", None, "wartortle", ...)
wartortle = Pokemon("Wartortle", "0008", 1.7, 90.5, "Lizard", "Blaze", "Fire", "Water"+"Ground"+"Rock", squirtle, "blastoise", ...)
blastoise = Pokemon("Blastoise", "0009", 1.7, 90.5, "Lizard", "Blaze", "Fire", "Water"+"Ground"+"Rock", "wartortle", None, ...) 
#endregion

# Blank Pokedex Entry
# = Pokemon("", "00", ., ., "", "", "", "", False, False)
# = Pokemon("", "00", 0.0, 0.0, "", "", ""+"", ""+"", False, False)

pokemon_db = {bulbasaur, ivysaur, venusaur, charmander, charmeleon, charizard, squirtle, wartortle, blastoise}


ivysaur.evolution = venusaur
print(venusaur)

print(ivysaur.pokedex_number)
print(ivysaur.evolution.name)
print(ivysaur.evolution.pokedex_number)
print(f"Ivysaur's evolution is {ivysaur.evolution.name}, and it's pre-evolution is {ivysaur.pre_evolution.name}")








"""
    Update Message/Notes (v0.1.1):
        - Decided that I will need to allow each instance of the class to be created first, then circle the code back to tie up pre-evolutions/evolutions.
        - Added "# region Data" to tidy Pokemon database 
        - 

"""  


"""
    Research/Self-Ed/Realisations;
        - Unusure if to use '__repr__()' or '__str__()' to display class string objects
        - Need to specify <.evolution.name> when calling for Pokemon's pre & evolutions, to avoid getting <object at 0x00000...> etc.


"""


"""
        ** Code Graveyard **




"""
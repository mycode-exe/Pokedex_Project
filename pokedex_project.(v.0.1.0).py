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
# Version: v0.1.0
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
# References:
#       -
#       -
#
#
#
#********************************************************************************************************************

class Pokemon:
    def __init__(self, name, pokedex_number, height, weight, category, abilities, type, weaknesses, has_pre_evolution, has_evolution):
        self.name = name
        self.pokedex_number = pokedex_number
        self.height = height # in Metres (Format: float)
        self.weight = weight # in Kilograms (Format: float)
        self.category = category
        self.abilities = abilities
        self.type = type
        self.weaknesses = weaknesses
        self.has_pre_evolution = has_pre_evolution # If n/a - Mark as ' False '
        self.has_evolution = has_evolution # If n/a - Mark as ' False '
        
        ...
    ...

# Pokemon "database"
bulbasaur = Pokemon("Bulbasaur", "0001", 0.7, 6.9, "Seed", "Overgrow", "Grass"+"Poison", "Fire"+"Ice"+"Flying"+"Psychic", False, "Ivysaur",)
ivysaur = Pokemon("Ivysaur", "0002", 1.0, 13.0, "Seed", "Overgrow", "Grass"+"Poison", "Fire"+"Ice"+"Flying"+"Psychic", bulbasaur, venusaur)
venusaur = Pokemon("Venusaur", "0003", 2.0, 100.0, "Seed", "Overgrow", "Grass"+"Poison", "Fire"+"Ice"+"Flying"+"Psychic", ivysaur, False)
charmander = Pokemon("Charmander", "0004", 0.6, 8.5, "Lizard", "Blaze", "Fire", "Water"+"Ground"+"Rock", False, charmeleon)
charmeleon = Pokemon("Charmeleon", "0005", 1.1, 19.0, "Lizard", "Blaze", "Fire", "Water"+"Ground"+"Rock", charmander, charizard)
charizard = Pokemon("Charizard", "0006", 1.7, 90.5, "Lizard", "Blaze", "Fire", "Water"+"Ground"+"Rock", charmeleon, False)

# Blank Pokedex Entry
# = Pokemon("", "00", ., ., "", "", "", "", False, False)
# = Pokemon("", "00", 0.0, 0.0, "", "", ""+"", ""+"", False, False)









"""
    Update Message/Notes (v0.1.0):
        - Initial 'Pokemon' class created, along with the first 6 Pokemon from the Pokedex.
        - Issue arrising from wanting to call on objects to interconnect with others, but before they have been created by the database. 
        - E.g. - Listing "Ivysaur" in the "Bulbasaur" object's instance, as it does not exist when the bulbasaur object is created/ran. Will need to address this

"""  



"""
        ** Code Graveyard **


"""
"""
    Cultural Evolution Simulation (Yummy_Recipe)

    Ali Fazeli

    Final Project of B.sc Level in Computer Engineering

    Task:           Simulate changes in recipes within a population of Agents over several
                    generations depending on different rule sets.

    Module Descr.:  Extracts & processes recipes from raw text resource from source:
                    http://mc6help.tripod.com/RecipeLibrary/RecipeLibrary.htm (access 26/02/16)
"""


import glob, re, os, sys
from Presets import *

recipes_dir = os.path.dirname(os.path.realpath(__file__)) + "/Recipes/"

recipes_raw = []        #list of unprocessed splitted recipe strings
recipes = []            #list of all recipe objects
recipesMeat = []        
recipesFish = []
recipesVeggi = []
all_ingredients = []    #list of all ingredients of all recipes

class recipe(object):
    def __init__(self, category, title, prep_time, ingredients):


        if category == "beef" or category == "lamb":
            category = "meat"
        elif category.startswith("veg"):
            category = "veggi"

            
        self.category = category    	# string of category
        self.title = title          	# string of recipe title
        self.prep_time = prep_time     	# string of format [0-9]:[0-5][0-9]
        self.rel_prep_time = self.retRelTime()	# string of relative time term
        self.ingredients = ingredients  # list 	 of ingredients
        self.mutate_history = []        # list   of mutate actions
        self.score = 0                  # score  of all points assigned in inter-Agent evaluation steps
        self.scoreList = []             # list   to keep track of all the awarded points
        # -----------------------------------------------
        self.counter = 0                    		# for testing only

    def __eq__(self, other):
        # since i use DEEPCOPYs we need a different way of comparing Recipes; just by title right now
        # test for equality according to our definition
        # question arises: when are two recipes equal = ReviewMe
        if type(self) == type(other):

            if self.title == other.title:
                return True
            else:
                return False
        else:
            return "Agent.__eq__() : Wrong type! Need 'Agent' type to compare."

    def retLength(self):
        return len(self.ingredients)

    def retRelTime(self):
        if self.prep_time <= timeDic["short"]:
            return "short"
        elif self.prep_time > timeDic["short"] and self.prep_time <= timeDic["medium"]:
            return "medium"
        else:
            return "long"

#CLEANUP OF INGREDIENTS STRINGS
def clean_ingredients(ingr_list):
    clean_list = []
    for ingredient in ingr_list:
        ingredient = re.sub("(\(.*\))|( -- .*)|(or .* and .*)|(\*|\;|--)", "", ingredient)
        ingredient = ingredient.split("  ") #splits ingredient from amount of ingredient
        ingredient = ingredient[-1].lower().strip()
        clean_list.append(ingredient)
    return clean_list

#GROUPING OF RECIPES
def recipeDiff(r):
    if r.category=="meat":
        recipesMeat.append(r)
    elif r.category=="fish":
        recipesFish.append(r)
    elif r.category==("veggi"):
        recipesVeggi.append(r)
    else:
        sys.exit("Error in recipe_extractor.py, lines 35, wrong recipe type handed over from source txt file.")


#GATERING ALL TEXT FILES:
file_list = glob.glob(recipes_dir + "*.txt")

#Windows OS
if os.name == "nt":

    for directory in file_list:

        #GET CATEGORY
        category = directory.split("\\") #split up dir path /Recipes/x.txt
        category = category[-1]         #take last level in directory
        category = category.strip(".txt").lower()

        #READ FILE & SLICE INTO RECIPES
        raw_text = open(directory, mode="r");
        all_recipes = raw_text.read()
        raw_text.close()

        separator = "* Exported from MasterCook *"
        recipes_raw = all_recipes.split(separator)

        for r in recipes_raw[1:]:

            #GET TITLE
            r1 = r.split("\n")
            title = r1[:3][-1].strip()

            #GET PREP TIME
            prep_time = r1[5]
            time_pattern = re.compile("\d:\d\d")
            r1 = time_pattern.findall(prep_time)
            prep_time = r1[0].strip()

            if prep_time == "0:00":
                pass
            else:

                separator2 = "\n--------  ------------  --------------------------------\n"
                ingredients_list = r.split(separator2)

                ingredients_list = ingredients_list[-1].split("\n\n")
                ingredients_list = ingredients_list[0].split("\n")
                ingredients_list = clean_ingredients(ingredients_list)

                r = recipe(category, title, prep_time, ingredients_list)
                recipeDiff(r)
                recipes.append(r)

                #ADDING INGREDIENTS TO GLOBAL INGREDIENTS LIST
                for ingredient in ingredients_list:
                    if ingredient not in all_ingredients:
                        all_ingredients.append(ingredient)

#Unix OS
else:

    for directory in file_list:

        #GET CATEGORY
        category = directory.split("/") #split up dir path /Recipes/x.txt
        category = category[-1]         #take last level in directory
        category = category.strip(".txt").lower()
        
        #READ FILE & SLICE INTO RECIPES
        raw_text = open(directory, mode="r"); 
        all_recipes = raw_text.read()
        raw_text.close()

        separator = "* Exported from MasterCook *"
        recipes_raw = all_recipes.split(separator)
        
        for r in recipes_raw[1:]:

            #GET TITLE
            r1 = r.split("\n")
            title = r1[:3][-1].strip()
            
            #GET PREP TIME
            prep_time = r1[5]
            time_pattern = re.compile("\d:\d\d")
            r1 = time_pattern.findall(prep_time)
            prep_time = r1[0].strip()   
            
            if prep_time == "0:00":
                pass
            else:
                
                separator2 = "\r\n--------  ------------  --------------------------------\r\n"
                ingredients_list = r.split(separator2)
                
                ingredients_list = ingredients_list[-1].split("\r\n\r\n")
                ingredients_list = ingredients_list[0].split("\r\n")
                ingredients_list = clean_ingredients(ingredients_list)
                
                r = recipe(category, title, prep_time, ingredients_list)
                recipeDiff(r)
                recipes.append(r)
                
                #ADDING INGREDIENTS TO GLOBAL INGREDIENTS LIST
                for ingredient in ingredients_list:
                    if ingredient not in all_ingredients:
                        all_ingredients.append(ingredient)


if __name__ == "__main__":
           
    for recipe in recipes:
        print("\n"+recipe.category)
        print(recipe.title)
        print(recipe.prep_time)
        print(recipe.ingredients)
        print(recipe.ing_size)
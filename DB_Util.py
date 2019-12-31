import sqlite3 as sql

def Init():
   """
   Initialize the database.  This database contains the following tables:
      - Recipes
        - Recipe names
        - Ingredients
        - Ingredient quantities
        - Ingredient units
   """

def AddIngredientColumn():
   """
   Adds an ingredient, quantity, and unit column.  Called when there are
   more ingredients than columns.
   """

def Exists():
   """
   Checks that the database exists.
   """

def Close():
   """
   Closes the database.
   """

def Open():
   """
   Opens the database.
   """

def AddIngredient():
   """
   Adds an ingredient, calling AddIngredientColumn if need be.
   """

def IsOpen():
   """
   Checks that the database is open.
   """

def GetIngredients(RecipeName):
   """
   Returns a data frame with ingredient names and quantities.
   """

def SetIngredients(Ingredients, RecipeName):
   """
   Sets the ingredients for a recipe.
   """

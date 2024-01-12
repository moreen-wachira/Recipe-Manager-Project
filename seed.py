# seed.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Recipe, Ingredient, RecipeIngredient  

DATABASE_URL = "sqlite:///recipes.db"  
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def seed_data():
    # Add some initial recipes and ingredients
    recipe1 = Recipe(title="Spaghetti Bolognese", instructions="Cook spaghetti and prepare Bolognese sauce")
    recipe2 = Recipe(title="Caesar Salad", instructions="Mix lettuce, croutons, and Caesar dressing")

    ingredient1 = Ingredient(name="Spaghetti")
    ingredient2 = Ingredient(name="Bolognese Sauce")
    ingredient3 = Ingredient(name="Lettuce")
    ingredient4 = Ingredient(name="Croutons")
    ingredient5 = Ingredient(name="Caesar Dressing")

    recipe1.ingredients.append(RecipeIngredient(quantity="200g", ingredient=ingredient1))
    recipe1.ingredients.append(RecipeIngredient(quantity="300g", ingredient=ingredient2))
    recipe2.ingredients.append(RecipeIngredient(quantity="1 head", ingredient=ingredient3))
    recipe2.ingredients.append(RecipeIngredient(quantity="1 cup", ingredient=ingredient4))
    recipe2.ingredients.append(RecipeIngredient(quantity="2 tbsp", ingredient=ingredient5))

    # Add the recipes and ingredients to the database
    session.add_all([recipe1, recipe2, ingredient1, ingredient2, ingredient3, ingredient4, ingredient5])
    session.commit()

if __name__ == "__main__":
    seed_data()

# recipe_manager/cli.py

from models import Recipe, Ingredient, RecipeIngredient
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
engine = create_engine('sqlite:///recipes.db')
Session = sessionmaker(bind=engine)
session = Session()

# 1. Use of Lists in add_recipe Function:
def add_recipe(title, instructions, ingredients):
    new_recipe = Recipe(title=title, instructions=instructions)
    
    for ingredient_name, quantity in ingredients:
        ingredient = session.query(Ingredient).filter_by(name=ingredient_name).first()
        if not ingredient:
            ingredient = Ingredient(name=ingredient_name)
        new_recipe.ingredients.append(RecipeIngredient(quantity=quantity, ingredient=ingredient))
    
    session.add(new_recipe)
    session.commit()
    print(f"Recipe '{title}' added successfully!")

# 2. Use of Dictionaries in view_recipes Function:
def view_recipes():
    recipes = session.query(Recipe).all()
    
    if recipes:
        for recipe in recipes:
            print(f"\nTitle: {recipe.title}\nInstructions: {recipe.instructions}")
            
            if recipe.ingredients:
                print("Ingredients:")
                for ri in recipe.ingredients:
                    print(f"- {ri.ingredient.name}: {ri.quantity}")
            else:
                print("No ingredients listed.")
            
            print("\n")
    else:
        print("No recipes available.")

# 3. Use of Tuples in search_recipe_by_ingredient Function:
def search_recipe_by_ingredient(ingredient):
    recipes = session.query(Recipe).filter(Recipe.ingredients.any(ingredient_id=session.query(Ingredient.id).filter_by(name=ingredient))).all()
    
    if recipes:
        for recipe in recipes:
            print(f"\nTitle: {recipe.title}\nInstructions: {recipe.instructions}")
            
            if recipe.ingredients:
                print("Ingredients:")
                for ri in recipe.ingredients:
                    print(f"- {ri.ingredient.name}: {ri.quantity}")
            else:
                print("No ingredients listed.")
            
            print("\n")
    else:
        print(f"No recipes found with '{ingredient}'.")


while True:
    print("\nRecipe Manager CLI:")
    print("1. Add Recipe")
    print("2. View Recipes")
    print("3. Search by Ingredient")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        title = input("Enter recipe title: ")
        instructions = input("Enter instructions: ")
        ingredients = []
        while True:
            ingredient_name = input("Enter ingredient name (or 'done' to finish): ")
            if ingredient_name.lower() == 'done':
                break
            quantity = input("Enter quantity: ")
            ingredients.append((ingredient_name, quantity))
        add_recipe(title, instructions, ingredients)

    elif choice == '2':
        view_recipes()

    elif choice == '3':
        ingredient = input("Enter ingredient to search: ")
        search_recipe_by_ingredient(ingredient)

    elif choice == '4':
        print("Exiting Recipe Manager. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")


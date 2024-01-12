# recipe_manager/main.py

from .cli import add_recipe, view_recipes, search_recipe_by_ingredient

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

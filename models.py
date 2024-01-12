# recipe_manager/models.py

from sqlalchemy import Column, Integer, String, Text, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship
from database import engine

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipes'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    instructions = Column(Text, nullable=False)
    ingredients = relationship('RecipeIngredient', back_populates='recipe')

class Ingredient(Base):
    __tablename__ = 'ingredients'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)

class RecipeIngredient(Base):
    __tablename__ = 'recipe_ingredients'
    id = Column(Integer, primary_key=True)
    recipe_id = Column(Integer, ForeignKey('recipes.id'))
    ingredient_id = Column(Integer, ForeignKey('ingredients.id'))
    quantity = Column(String, nullable=False)
    recipe = relationship('Recipe', back_populates='ingredients')
    ingredient = relationship('Ingredient')

Base.metadata.create_all(engine)

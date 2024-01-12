# recipe_manager/database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///recipes.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

from model import *


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,scoped_session


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = scoped_session(sessionmaker(bind=engine,autoflush=False))

def add_recipe(name,recipe,photo):
	product_objection = Recipe(	
		name=name,
		recipe=recipe,
		photo=photo
		)
	session.add(product_objection)
	session.commit()

def readmore_recipe(name,recipe):
	product_objection = added_recipe(	
		name=name,
		recipe=recipe)
	session.add(product_objection)
	session.commit()

def all_recipes():
	recipes = session.query(
		added_recipe).all()	
	return recipes

def allrecipes():
	recipes = session.query(
		Recipe).all()	
	return recipes

def query_by_name(their_name):

	recipe = session.query(
		Recipe).filter_by(
		name=their_name).first()
	return recipe


def query_by_id(their_id):

	recipe = session.query(
		Recipe).filter_by(
		id=their_id).first()
	return recipe
	
def delete_recipe(their_name):
 
   session.query(Recipe).filter_by(
       name=their_name).delete()
   session.commit()
add_recipe("Pancakes","1 egg, 1 tsp butter, 1 cup milk, 1 tsp,1 cup flour, 1 tsp sugar ","/static/Pancake.jpg")
add_recipe("Spanish Salad", "green apple, red onion, pine nuts, feta cheese", "/static/salad1.jpg")
#delete_recipe()
print(len(allrecipes()))
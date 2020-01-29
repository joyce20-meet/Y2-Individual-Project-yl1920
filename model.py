from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class added_recipe(Base):
	__tablename__ = 'added_recipes'
	recipe_id = Column(Integer, primary_key=True)
	name = Column(String)
	recipe = Column(String) 

	def __repr__(self):
		print_list=[self.name ,self.recipe]
		return str(print_list)

class Recipe(Base):
	__tablename__ = 'Recipe'
	id = Column(Integer, primary_key=True)
	name = Column(String)
	recipe = Column(String)
	photo= Column(String)
	
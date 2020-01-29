from flask import *
from database import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/')
def home():
	recipes = allrecipes()
	# delete_recipe=delete_recipe(id)

	return render_template('Home.html',recipes=recipes)
	
@app.route('/recipe')
def recipe():
	return render_template('recipe.html')



@app.route('/Specific_recipe/<int:id>')
def Specific_recipe(id):
	recipe=query_by_id(id)
	name=recipe.name
	Ingredients=recipe.recipe
	photo=recipe.photo

	return render_template('Specific_recipe.html', name = name, Ingredients=Ingredients, photo=photo)


@app.route('/added_recipe' , methods=['GET', 'POST'])
def added_recipe():
	if request.method == 'GET':
		z = all_recipes()
		print(z)
		return render_template('added_recipe.html')
	else:
		name = request.form['name']
		recipe = request.form['recipe']

		add_recipe(name,recipe) 

		return render_template('added_recipe.html',
			n = name,
			r = recipe) 


@app.route('/salad')
def salad():
	name = "Spanish Salad"
	Ingredients = "green apple, red onion, pine nuts, feta cheese"
	photo = "/static/salad1.jpg"
	return render_template('Specific_recipe.html', name = name, Ingredients=Ingredients, photo=photo)


@app.route('/Pancake')
def Pancake():
	name = "Pancakes"
	Ingredients = "1 egg, 1 tsp butter, 1 cup milk, 1 tsp,1 cup flour, 1 tsp sugar "
	photo = "/static/Pancake.jpg"
	return render_template('Specific_recipe.html',name= name, Ingredients=Ingredients , photo=photo)


if __name__ == '__main__':
	app.run(debug=True)
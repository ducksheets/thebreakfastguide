from flask import Flask, render_template
from food import *

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/recipes")
def recipes():
    return render_template('recipes.html')

@app.route("/recipes/<food_category>")
def foodcategory(food_category):
    food_list = foods[food_category]
    return render_template('foodcategory.html',food_category=food_category,food_list=food_list)


@app.route("/recipes/<food_category>/<int:food_num>")
def foodrecipe(food_category,food_num):
    food_recipe = foods[food_category][food_num]
    return render_template('foodrecipe.html',food_recipe=food_recipe)

if __name__=='__main__':
    app.run(debug=True)
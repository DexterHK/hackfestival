from flask import Flask, render_template, jsonify
import json
from sorting import sortFood

app = Flask(__name__,static_url_path='/static/')

# Load the JSON file
with open('static/sorted_food.json', 'r') as file:
    menu_data = json.load(file)

@app.route('/')
def indexing():
    return render_template('home_page.html')

@app.route('/menu')
def menu():
    sortFood()
    return render_template('menu.html', user= menu_data)

@app.route('/system')
def system():
    return render_template('system.html')

@app.route('/menu')
def fetching():
    return render_template('fetching.js', user= menu_data)

@app.route('/')
def login():
    return render_template('menu.html')    

if __name__ == '__main__':
    app.run(debug=True)

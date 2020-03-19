# import render_template function from the flask module
from flask import render_template
# import the app object from the ./application/__init__.py
from application import app
from application.models import Car

# define routes for / & /home, this function will be called when these are accessed
@app.route('/')
@app.route('/home')
def home():
 carData = Car.query.first()
 return render_template('home.html', title='Home', car=carData)

@app.route('/car')
def car():
 return render_template('car.html', title='car')

@app.route('/parts')
def parts():
 return render_template('parts.html', title='parts')

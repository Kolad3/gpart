from pkg import app 
from flask import render_template

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/team/')
def team():
    return render_template('team.html')

@app.route('/testimonials/')
def testimonials():
    return render_template('testimonials.html')
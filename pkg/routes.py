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

@app.route('/faq/')
def faq():  
    return render_template('faq.html')

@app.route('/pricing/')
def pricing():
    return render_template('pricing.html')

@app.route('/projects/all/')
def projects_all():
    return render_template('projects.html')

@app.route('/projects/single/')
def projects_single():
    return render_template('projects-single.html')

@app.route('/services/single/')
def service_single():
    return render_template('service-single.html')   

@app.route('/services/')
def services():
    return render_template('services.html')

@app.route('/contact/')
def contact():  
    return render_template('contact.html')

@app.route('/news/right/sidebar/')
def news_right_sidebar():
    return render_template('news-right-sidebar.html')

@app.route('/news/single/')
def news_single():
    return render_template('news-single.html')
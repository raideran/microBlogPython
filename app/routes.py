from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Jose'}
    posts = [
        {
            'author': {'username': 'Jhon'},
            'body': 'Beautiful day in Alajuelita'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'EndGame Movie was amazing'
        },
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
